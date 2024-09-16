import os, disnake, random, re
import disnake.ext
from discord.ext import commands
import google.generativeai as genai
from disnake.ext import tasks
from disnake.ext import commands
from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path


#Load Gemini Token and configure other variables
load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')
GOOGLE_AI_KEY = os.environ.get('GOOGLE_AI_KEY')
MAX_HISTORY  = 10
message_history = {}

# Configure the generative AI model-----------------------------------------------------------------------------------------------------------------------------------------------------------
genai.configure(api_key=GOOGLE_AI_KEY)
text_generation_config = {
    "temperature": 0.6,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 512,
}
image_generation_config = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 512,
}
# safety_settings = [{
#     "category": "HARM_CATEGORY_HARASSMENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
# }, {
#     "category": "HARM_CATEGORY_HATE_SPEECH",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
# }, {
#     "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
# }, {
#     "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
#     "threshold": "BLOCK_MEDIUM_AND_ABOVE"
# }]
text_model = genai.GenerativeModel(model_name="gemini-pro",
                                   generation_config=text_generation_config,
                                   #safety_settings=safety_settings
                                   )
image_model = genai.GenerativeModel(model_name="gemini-pro-vision",
                                    generation_config=image_generation_config,
                                    #safety_settings=safety_settings
                                    )
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Bot = commands.Bot(
    command_prefix=disnake.ext.commands.when_mentioned,
    activity=disnake.Activity(type=disnake.ActivityType.watching, name="dogroom fetcher")
)


#ID of channel where questions are posted
target = 1116378200096907264#fill in
target2 = 1116378196678545430

#ID of role that gets pinged when posting a question, leave blank string if no role should be pinged
pingrole = "1116378165284196484"

#Hour QOTD is to be posted
posttime = 16#fill in

embedcolor = disnake.Colour.green()

errorembedcolor = disnake.Colour.red()

#Question addition, not used for now, could be added later
questionsfile = Path(__file__).with_name('questions.txt')
linksfile = Path(__file__).with_name('questionlins.txt')
tempfile = Path(__file__).with_name('temp.txt')

#Adds a question to the text file when called.(Future functionality)
def question_add(question):
    with open(questionsfile, 'a') as questions:
        questions.write(question+'\n')

def remove_question(qotd):
    with open (questionsfile, "r") as input:
        with open (tempfile, "w") as output:
            for line in input:
                if line.strip("\n") != qotd:
                    output.write(line)
    os.replace(tempfile, questionsfile)
progress = 0
#===============================================================================Daily Riddle posting=======================================================================
 
async def question_post(channel, subject):
    """
    Parameters:
    - channel: The channel where the message will be sent.
    - subject: The topic for the riddle (e.g., 'Web Development', 'Cybersecurity','AI).
    """
    # Validate the subject to ensure it's one of the allowed topics
    # Sub commands/ options to choose from can be added later if required
    # allowed_subjects = ['Web Development', 'Cybersecurity', 'DSA','AI','ML','Programming history','Robotics','IOT']
    # if subject not in allowed_subjects:
    #     raise ValueError("Invalid subject. Allowed subjects are: 'Web Development', 'Cybersecurity', 'DSA'.")

    # Create the cleaned text based on the subject
    cleaned_text = f"send a daily riddle on the following topic: {subject}. Do not give the answer, only the question. The title should be \"Daily riddle - {subject}\":"
    
    # Generate the response text
    response_text = await generate_response_with_text(cleaned_text)
    
    # Add AI response to history
    await split_and_send_messages(channel, response_text, 1700)

    return
#==========================================================================================================================================================================
#================================================================================Chat summary function ===================================================================
async def summarise(channel,message):
      # Ignore messages sent by the bot
    cleaned_text = "Summarise the following chat in about 500 words and give details on who said what and respond with \"Chat Summary : \"+ (your response)  :" + message


    response_text = await generate_response_with_text(cleaned_text)
    #add AI response to history
    await split_and_send_messages(channel, response_text, 1700)
    return

#=====================================================================================================================================================================
async def generate_response_with_text(message_text):
  prompt_parts = [message_text]
  print("Got textPrompt: " + message_text)
  response = text_model.generate_content(prompt_parts)
  if (response._error):
    return "❌" + str(response._error)
  return response.text

async def split_and_send_messages(channel, text, max_length):

  # Split the string into parts
  messages = []
  for i in range(0, len(text), max_length):
    sub_message = text[i:i + max_length]
    messages.append(sub_message)

  # Send each part as a separate message
  for string in messages:
    await channel.send(string)


last_posted_date = None
#Scheduled to call question of the day.

 
#Example usage of daily riddle posting for different subjects
@tasks.loop(hours = 1)
async def task():
    global last_posted_date
    current_date = datetime.now().date()
    if datetime.now().hour == posttime and last_posted_date!=current_date:
        channel = Bot.get_channel(target2)
        await question_post(channel,'AI')
        await question_post(channel,'Programming history')
        await question_post(channel,'Cybersecurity')
        await question_post(channel,'Robotics')
        await question_post(channel,'Web Development')
        last_posted_date = current_date


#Make sure bot is online.
@Bot.event
async def on_ready():
    print(f'{Bot.user} has connected to Discord! It is '+ str(datetime.now()))
    await task.start()

#Reads for commands, which includes adding questions and testing
     
@Bot.slash_command(name="riddle", description="Sends riddle for testing")
# @commands.has_permissions(send_messages=True)
async def send(inter,subject):
    channel = Bot.get_channel(target)
    await question_post(channel,subject)
    embed = disnake.Embed(
        title = f"Success!",
        description = f"Sent a daily riddle.",
        colour = embedcolor,
    )
    await inter.send(embed=embed)

#Add question, can be added later
@Bot.slash_command(name="add", description="Add a QOTD to the list")
async def add(inter, question):
    embed = disnake.Embed(
        title = f"Added QOTD! Thank you for submitting.",
        description = f"'{question}'",
        colour = embedcolor,
    )
    await inter.send(embed=embed)
    question_add(question)
    print(f'{inter.author} has added "{question}"!')

if __name__ == '__main__':
   Bot.run(TOKEN)
