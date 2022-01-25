import dotenv
import os
import random # added for the repeat command to choose a random integer 

import nextcord
# from nextcord.ext import commands

# Needed for us to tell Discord what information our bot will want to access
myIntents = nextcord.Intents.default()
# Specifically note that we want access to member information
myIntents.members = True

client = nextcord.Client(intents=myIntents)

### Defining client functionalities
@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("----" * 20)

@client.event
async def on_message(message):
    if message.author == client.user: return
    print(f"""\
Just got a message from {message.author} at {message.created_at}, saying...

{message.content}

{message=}
{'----' * 20}
""")

    if message.content.startswith("$ "):
        cont = message.content.lstrip("$ ")
        cmd = cont.split(maxsplit=1)[0]
        if cmd == "echo":
            cont = cont.split(maxsplit=1)[1:]
            await message.channel.send(*cont)
        if cmd == "repeat":
            cont = cont.split(maxsplit=1)[1:]
            for i in range(random.randint(2, 5)):
                await message.channel.send(*cont)


### The following concerns cleint startup; not needed to execute until the very end
# This will load the `.env` file data as a system environment variable
dotenv.load_dotenv()

# Assign variable myToken to be the string in the 'token' environment variable; loaded in .env
myToken = os.getenv("token")

client.run(myToken)
