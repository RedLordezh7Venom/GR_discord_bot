import disnake
from dotenv import load_dotenv
import os
from datetime import datetime
from disnake.ext import commands

#configure Bot and environment variables
intents = disnake.Intents.default()
Bot = commands.Bot(
    command_prefix=disnake.ext.commands.when_mentioned
)
load_dotenv()
TOKEN = os.environ.get('DISCORD_TOKEN')

current_time = datetime.now().strftime("%H:%M")

# bot_icon_url = 'https://iconape.com/wp-content/png_logo_vector/random.png' #Change this to the logo

# Global variables to hold bot information
bot_name = None                       #varx          #Customizable or keep None for default name
bot_icon_url = None                   #varx


#Links to be displayed 
global_options = [
        disnake.SelectOption(
            label="Twitter",
            description="Geek Room's Official Twitter Page",
            emoji="✖️",
            value="twitter-linkspanel"
        ),
        disnake.SelectOption(
            label="Whatsapp Group",
            description="Join Geek Room's Whatsapp",
            emoji="💬",
            value="whatsapp-linkspanel"
        ),
        disnake.SelectOption(
            label="Discord Server",
            description="Join the Official server",
            emoji="🎮",
            value="discord-linkspanel"
        ),
        disnake.SelectOption(
            label="Nas.io Community",
            description="Geek Room's Nas.io community page",
            emoji="🎯",
            value="nasio-linkspanel"
        ),
        disnake.SelectOption(
            label="LinkedIn",
            description="Geek room's Official Linkedin ",
            emoji="ℹ️",
            value="linkedin-linkspanel"
        ),
        disnake.SelectOption(
            label="Instagram",
            description="Geek Room's Official Instagram",
            emoji="📸",
            value="insta-linkspanel"
        )
    ]

# Bot ready event to fetch bot details
@Bot.event
async def on_ready():
    global bot_name, bot_icon_url
    bot_name = Bot.user.name
    bot_icon_url = Bot.user.display_avatar.url if Bot.user.display_avatar else Bot.user.default_avatar.url
    print(f'Logged in as {bot_name}')

async def handle_insta(inter: disnake.MessageInteraction):
    await inter.response.defer()
    
    # Create the action row for the select menu
    row2 = disnake.ui.ActionRow(
        disnake.ui.Select(
            placeholder="❌┆Links",
            options=global_options,
            custom_id="Bot-linkspanel"
        )
    )

    # Create the action row for the bot invite button
    row = disnake.ui.ActionRow(
        disnake.ui.Button(
            label="Geek Room official Instagram",
            url="https://instagram.com/geekr00m",
            style=disnake.ButtonStyle.link
        )
    )

    # Create the embed
    embed = disnake.Embed(
        title="📸・Geek Room's Instagram",
        description="Follow Geek Room's Instagram for resources, posts and new events",
        color=0x3498db,
        url = "https://instagram.com/geekr00m"
    )
    embed.set_author(name=f"@geekroom",icon_url="https://ugc.production.linktr.ee/2a6c8d7a-a38a-45c4-9e9f-4a14b6c88714_GR-Logo.png?io=true&size=avatar-v3_0")
    embed.set_image(url="https://i.pinimg.com/736x/24/37/73/2437730f7e3a5705e205e67fa2cd1020.jpg")
    embed.set_footer(text= f"Dogroom • Today at {current_time}",icon_url=bot_icon_url)
    
    # Edit the original message with the new embed and action rows
    await inter.message.edit(embed=embed, components=[row2, row])

async def handle_twitter(inter: disnake.MessageInteraction):
    await inter.response.defer()
    
    # Create the action row for the select menu
    row2 = disnake.ui.ActionRow(
        disnake.ui.Select(
            placeholder="❌┆Links",
            options=global_options,
            custom_id="Bot-linkspanel"
        )
    )

    # Create the action row for the bot invite button
    row = disnake.ui.ActionRow(
        disnake.ui.Button(
            label="Geek Room Twitter",
            url="https://twitter.com/geek__room_",
            style=disnake.ButtonStyle.link
        )
    )

    # Create the embed
    embed = disnake.Embed(
        title="✖️・Geek Room Twitter",
        description="Follow Geek Room on Twiter for latest updates ",
        color=0x3498db,
        url = "https://twitter.com/geek__room_"
    )
    embed.set_author(name=f"@geekroom",icon_url="https://ugc.production.linktr.ee/2a6c8d7a-a38a-45c4-9e9f-4a14b6c88714_GR-Logo.png?io=true&size=avatar-v3_0")
     
    embed.set_footer(text= f"Dogroom • Today at {current_time}",icon_url=bot_icon_url)
    
    # Edit the original message with the new embed and action rows
    await inter.message.edit(embed=embed, components=[row2, row])


async def handle_whatsapp(inter: disnake.MessageInteraction):
    await inter.response.defer()
    
    # Create the action row for the select menu
    row2 = disnake.ui.ActionRow(
        disnake.ui.Select(
            placeholder="❌┆Links",
            options=global_options,
            custom_id="Bot-linkspanel"
        )
    )

    # Create the action row for the bot invite button
    row = disnake.ui.ActionRow(
        disnake.ui.Button(
            label="Geek Room Whatsapp",
            url="https://chat.whatsapp.com/EPDLVRHU1AM1HQ76NFWIDW",
            style=disnake.ButtonStyle.link
        )
    )

    # Create the embed
    embed = disnake.Embed(
        title="💬・Geek Room Whatsapp",
        description="Join the official Geek Room community Whatsapp ",
        color=0x3498db,
        url = "https://chat.whatsapp.com/EPDLVRHU1AM1HQ76NFWIDW"
    )
    embed.set_author(name=f"@geekroom",icon_url="https://ugc.production.linktr.ee/2a6c8d7a-a38a-45c4-9e9f-4a14b6c88714_GR-Logo.png?io=true&size=avatar-v3_0")
     
    embed.set_footer(text= f"Dogroom • Today at {current_time}",icon_url=bot_icon_url)

    # Edit the original message with the new embed and action rows
    await inter.message.edit(embed=embed, components=[row2, row])

async def handle_nas(inter: disnake.MessageInteraction):
    await inter.response.defer()
    
    # Create the action row for the select menu
    row2 = disnake.ui.ActionRow(
        disnake.ui.Select(
            placeholder="❌┆Links",
            options=global_options,
            custom_id="Bot-linkspanel"
        )
    )

    # Create the action row for the bot invite button
    row = disnake.ui.ActionRow(
        disnake.ui.Button(
            label="Geek Room Nas.io Community",
            url="https://nas.io/geekroom",
            style=disnake.ButtonStyle.link
        )
    )

    # Create the embed
    embed = disnake.Embed(
        title="🔽・Geek Room Nas.io",
        description="Get access to Geek Room's community events, resources, products and many more on Nas.io  ",
        color=0x3498db,
        url = "https://nas.io/geekroom"
    )
    embed.set_author(name=f"@geekroom",icon_url="https://ugc.production.linktr.ee/2a6c8d7a-a38a-45c4-9e9f-4a14b6c88714_GR-Logo.png?io=true&size=avatar-v3_0")
    
    embed.set_footer(text= f"Dogroom • Today at {current_time}",icon_url=bot_icon_url)
 

    # Edit the original message with the new embed and action rows
    await inter.message.edit(embed=embed, components=[row2, row])


async def handle_discord(inter: disnake.MessageInteraction):
    await inter.response.defer()
    
    # Create the action row for the select menu
    row2 = disnake.ui.ActionRow(
        disnake.ui.Select(
            placeholder="❌┆Links",
            options=global_options,
            custom_id="Bot-linkspanel"
        )
    )

    # Create the action row for the bot invite button
    row = disnake.ui.ActionRow(
        disnake.ui.Button(
            label="Geek Room Discord Server",
            url="https://discord.com/invite/7TEVm4pmMv",
            style=disnake.ButtonStyle.link
        )
    )

    # Create the embed
    embed = disnake.Embed(
        title="🎮・Geek Room Discord Server",
        description="Join Geek Room's official Discord server",
        color=0x3498db,
        url = "https://discord.com/invite/7TEVm4pmMv"
    )
    embed.set_author(name=f"@geekroom",icon_url="https://ugc.production.linktr.ee/2a6c8d7a-a38a-45c4-9e9f-4a14b6c88714_GR-Logo.png?io=true&size=avatar-v3_0")
     
    embed.set_footer(text= f"Dogroom • Today at {current_time}",icon_url=bot_icon_url)
   

    # Edit the original message with the new embed and action rows
    await inter.message.edit(embed=embed, components=[row2, row])


async def handle_linkedin(inter: disnake.MessageInteraction):
    await inter.response.defer()
    
    # Create the action row for the select menu
    row2 = disnake.ui.ActionRow(
        disnake.ui.Select(
            placeholder="❌┆Links",
            options=global_options,
            custom_id="Bot-linkspanel"
        )
    )

    # Create the action row for the bot invite button
    row = disnake.ui.ActionRow(
        disnake.ui.Button(
            label="Geek Room LinkedIn",
            url="https://www.linkedin.com/company/geekr00m/",
            style=disnake.ButtonStyle.link
        )
    )

    # Create the embed
    embed = disnake.Embed(
        title="Geek Room's LinkedIn Page",
        description="Follow Geek Room on LinkedIn to stay connected with the community",
        color=0x3498db,
        url = "https://www.linkedin.com/company/geekr00m/"
    )
    embed.set_author(name=f"@geekroom",icon_url="https://ugc.production.linktr.ee/2a6c8d7a-a38a-45c4-9e9f-4a14b6c88714_GR-Logo.png?io=true&size=avatar-v3_0")
    embed.set_footer(text= f"Dogroom • Today at {current_time}",icon_url=bot_icon_url)

    # Edit the original message with the new embed and action rows
    await inter.message.edit(embed=embed, components=[row2, row])

if __name__ == '__main__':
    Bot.run(TOKEN)