import nextcord
from nextcord.ext import commands
import dotenv
import os

# Needed for us to tell Discord what information our bot will want to access
myIntents = nextcord.Intents.default()
# Specifically note that we want access to member information
myIntents.members = True

# Create a Client object, the actual connection to Discord
bot = commands.Bot(command_prefix="$ ", intents=myIntents, description="Test Bot!")

### Defining client functionalities
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("----" * 20)

@bot.command()
async def ping(ctx):
    # Takes no arguments to the ping command
    """Will respond with the message 'pong'""" 
    await ctx.send("pong")

@bot.command()
async def echo(ctx, *, msg):
    # By adding the parameters '*, msg', everything after the command in the message is consumed into the `msg` parameter
    """Repeats a given message"""
    await ctx.send(msg)

@bot.command()
async def repeat(ctx, num: int, *, msg):
    # Takes an integer parameter 'num' dictating how many times to repeat the 'msg'
    """Repeats a message num times"""
    if num < 1: num = 1
    for i in range(num):
        await ctx.send(msg)

@bot.command()
async def add(ctx, a: int, b: int):
    # By using type hinting, the command.Bot class will implicitly convert a and b into actual integers!
    """Adds two integers together"""
    await ctx.send(f"{a} + {b} = {a+b}")

# This command is named 'doc', but can also be invoked with 'pin', 'document', and 'documentation' 
@bot.command(name='doc', aliases=['pin', 'document', 'documentation'])
async def doc(ctx):
    """Pins the incredibly important message you just sent"""
    await ctx.message.pin()

@bot.command(aliases=['list_members'])
async def members(ctx):
    '''List all members'''
    memberString = ''
    for member in ctx.guild.members:
        memberString += str(member)
        if member == bot.user:
            memberString += "  <--- That's me!"
        memberString += "\n" 
    await ctx.send(f"All members in {ctx.guild}:\n{memberString}")

# Tell the client to actually connect to Discord using the API Token provided in ...
dotenv.load_dotenv()
myToken = os.getenv("token")
bot.run(myToken)