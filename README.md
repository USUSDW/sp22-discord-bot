# Sp22 Discord Bot Presentation

## Table Of Contents

*   [Setting Up Our Project's Environment](#setting-up-our-projects-environment)
    *   [Managing Dependencies With `requirements.txt`](#setting-up-our-projects-environment)
*   [Virutal Environment](#virtual-environment)
    *   [Virtual Environment Setup Commands](#virtual-environment-setup-commands)
    *   [Inside the Virtual Environment](#inside-the-virutal-environment)
*   [Choose A License](#choose-a-license)
*   [Initial Setup of `main.py`](#initial-setup-of-mainpy)
    *   [Neccessary Imports](#necessary-imports)
    *   [Discord's `Intents`](#discords-intents)
    *   [Client Object](#client-object)
*   [Getting Your Discord API Token](#getting-your-discord-client-api-token)
    *   [Create an Application](#create-an-application)
    *   [Invite the Bot to a Server](#invite-the-bot-to-a-server)
    *   [Copying the Bot's API Key](#copying-the-bots-api-key)
*   [Connecting Your Discord Client](#connecting-your-discord-client)
    *   [Protecting Your API Key](#connecting-your-discord-client)
        *   [`.env` files](#connecting-your-discord-client)   
        *   [Loading `.env` files with `python-dotenv`](#connecting-your-discord-client)
*   [Discord Client Events](#connecting-your-discord-client)
    *   [`on_ready`](#connecting-your-discord-client)
    *   [`on_message`](#connecting-your-discord-client)
*   [Discord `commands.Bot` Client Subclass](#connecting-your-discord-client)
    *   [`commands.Bot` Default Help Command](#connecting-your-discord-client)
    *   [`on_message` Event With `commands.Bot` class](#connecting-your-discord-client)


# Setting Up Our Project's Environment
To first create a Discord bot, we must create an environment we can create this Discord bot in!

## Managing Dependencies With **`requirements.txt`**
A `requirements.txt` file is a file that contains a list of packages needed for a project. We will use pip to install these packages directly from this file, so long as it's formatted correctly. By convention, this file is called `requirements.txt`; it can be called whatever you'd like! 

### `requirements.txt` for this project
```
nextcord>=2.0.0
python-dotenv>=0.19.0
```

### Installing Packages In A `requirements.txt`
To install all these packages run the command `python -m pip install -r requirements.txt`

<hr/>

## **Virtual Environment**

### *What is a virtual enviornment?*
A *virtual environment* is a copy of your python environment that is unique to that project to assist in managing project dependencies. You can install packages inside this virtual environment and not have the packages installed to your system-wide Python interpreter.

### Virtual Environment Setup Commands
- `python -m venv --help`
    - this command returns a list of help items that explain the tool that will create a virtual environment
- `python -m venv path/to/venv`
    -   The `path/to/venv` is the location where you want the virtual environment to be created in. This is generally called `venv` in the root of your project, and is usually `.gitignore`d.
- Startup:
    - *Assume virtual environment was created in `venv` directory*
    - Linux, MacOS, *Nix: 
        -   `source venv/bin/activate`   
    - Windows: 
        -   `venv/Scripts/activate.bat`
    - The activation script updates your shell to point to the virutal Python enviornment when `python` and `pip` are invoked instead of your system's `python` environment
    - You should see `(venv)` in front of your *terminal prompt*
        ```
        [jaxtonw@Loki ~/discord-bot]
        $ source venv/bin/activate
        (venv) [jaxtonw@Loki ~/discord-bot]
        $ # you're now in the virtual environment!
        ```

### Inside The Virutal Environment
- `deactivate` : Exit the virtual environment
    -   The `deactivate` function should be available in your current shell session, and will reset your Python interpreter to the one before running the `activate` script 
- `python` : Virtual Environment Python Interpreter
    -   When invoked inside the virtual environment, this will be the `python` version installed inside the virtual environment. *Not* your system's `python` version. Their versionings may be the same, but settings and installed packages differ.
- `pip` *or* `python -m pip` : Virtual Environment Package Management
    -   Manage python packages inside the virtual environment
    -   `pip list` 
        -   Will return all installed python packages *inside* the virtual environment
<hr/>

## Choose A License
It's always a good idea to put a `LICENSE.txt` file in any publically available project. Various licenses exist for various purposes. This project chose to use the Apache 2.0 license. More information can be found on this license at [TLDR Legal](https://tldrlegal.com/license/apache-license-2.0-(apache-2.0)) and the [Apache 2.0 license official site](https://www.apache.org/licenses/LICENSE-2.0). [This repositories' license can be found in the `LICENSE.txt` file](LICENSE.txt).

# Setup Our Discord Client In `main.py` 

## Necessary `import`s
-   `nextcord`
    -   The Python package that serves as our interface to the Discord API. Contains all the Discord functionality we use.
-   `dotenv`.
    -   Will be used to load environment variables stored in a special file to store the API `token`.
-   `os`
    -   Used to access the `token` environment variable loaded by the `dotenv` package.
## Discord's `Intents`
Intents in Discord is a way to allow Discord to know what information you are to be requesting from it. Intents answer the question, *"What information is your bot going to need to access?"* Discord's API requires the intents to be known when any client connects to it. For our purposes, we want access to messages and the server members. The message intent is set in the `default()` intents constructor, and we can manually set the `members` intent to `True`.

```
myIntents = nextcord.Intents.default()
myIntents.members = True
```
### Intents Resources
*   [`nextcord` Docs : Intents](https://nextcord.readthedocs.io/en/latest/api.html?highlight=intents#nextcord.Intents)


## Client Object
A client object contains the functionality that interacts with Discord. To create one, we invoke
```
client = nextcord.Client(intents=myIntents)
```
where `myIntents` is the intents object dictating the information that the bot requires access to.

Out of the box, a `Client` object has all of the functionality to connect to Discord and change our bot account's status to online. We will need some additional information--the API Token--before we can make that connection though. That token will be aquired momentarily.

We can prepare to run the client with
```py
client.run(...)
```

We will place the API Token for our Discord Bot User in place of the `...` in the previous command. We will then quickly find a better way to supply our bot with an API Token *without* putting our API Token into the source code.

### Client Object Documentation
*   [`nextcord` Docs : Client](https://nextcord.readthedocs.io/en/latest/api.html?highlight=events#client)

# Getting Your Discord Client API Token
This section will detail how to go about creating an application and bot account on Discord and obtaining your bot's API token.

Navigate to [the **Discord Developer Portal** at https://discord.com/developers](https://discord.com/developers) to begin the process of registering an application and bot account.

## Create An Application
After logging in to the Discord Developer Portal, select the "new application" button on the ["Applications"](https://discord.com/developers/applications) page. This application is a collection of Discord services tied to your Discord account. We aim to create the bot account to this application.

On the left, select `Bot`. You may customize the Bot account here, and may even find the `TOKEN` associated with the bot. We will get this token later; other changes must be handled first.

For our test purposes, we will deselect the `Public Bot` option to ensure the application owner is the only one who can invite the bot to servers. This may be changed at a later time. 

We must now select which intents and permissions our bot needs. For our purposes, we want the `Server Members` and  `Message Content` intents enabled. We also want to select that we want `Administrator` permissions for our bot, such that it has access to all necessary operation we aim to develop.

## Invite The Bot To A Server
From within the `Applicaton` page we just generated, we aim to generate an URL that can be used to invite the Discord Bot profile associated with this application to servers.

0.  Click on `OAuth2`
1.  Click on `URL Generator`
2.  In `Scopes`, select `bot`
3.  In `Bot Permissions`, select `Administrator`
4.  Copy the Generated URL below the bot permissions box
    -   Looks something like https://discord.com/api/oauth2/authorize?client_id=WHOLE_LOTTA_NUMBERS_HERE&permissions=0&scope=bot
5.  Paste URL into browser
6.  Invite Bot to server of choice that you **have administrator privileges on**

After completing this, you should see the bot as a member of your server. At this time, it should be offline.

## Copying The Bot's API Key
In the application you just created, navigate to the `Bot` page. Here you will find the `TOKEN`. Copy this token to your clipboard, or choose to regenerate this token if you believe it has leaked. This token is how a Discord client like the one we are building with Python "log's in" to the Discord Bot account we just created. 

# Connecting Your Discord Client
Now with a Discord Bot account setup, added to a server, and it's token copied, we can connect our current `main.py` file to Discord and enable our bot account to log in. The API Key you copied earlier is inputted as a string argument to the `client.run()` method.

```py
client.run("API TOKEN HERE")
```

This *could* be done by just inputting the API Key as a string literal in your source code. At this point, we can run our Python Discord client and see that our created Discord Bot account comes online.

## Protecting Your API Key
Adding the API key to the source code exposes us to massive credential leaks, leading to breaches in security for our system. Especially so if we `git commit` this file with this API Token inside. Plenty of better and safer ways exist for us to store our API Token. In comes the `.env` file and `python-dotenv` package!

### `.env` Files 
`.env` files are a great way to set environment variables that your system can depend on without needing to set these environment variables system-wide. One defines the environment variables in these files with the pattern of `ENV_VARIABLE=VALUE`. To store our API token, we aim to create a `.env` file that allows the user to easily set the `token` environment variable.

```
token=YOUR TOKEN HERE
```

To safely utilize this `.env` file with Git, we can commit this file in it's current state *without* the API Token inputted, and then tell Git to not track any changes to this file from now on. To do so, we use the command `git update-index --assume-unchanged .env`. From here on out, we can instruct our user to safely put their API Token in place of `YOUR TOKEN HERE`. 

### Loading `.env` files with `python-dotenv`
The `python-dotenv` package exists to make working with `.env` files more convenient. We can use this package to *load* the contents of `.env` as environment variables into the current Python process, and then access them with `os.getenv("ENV_VARIABLE")`. 

To load the `token` environment variable from our `.env` file, we modify:
```py
client.run("API TOKEN STRING LITERAL")
``` 
to be:
```py
dotenv.load_dotenv()
myToken = os.getenv("token")
client.run(myToken)
```

This loads the token string from the environment running our Discord bot, adding an additional layer of protection that keeps our private API Token private.

# Discord Client Events

## `on_ready`
*   Register with `client.event` decorator!
*   Must be an [`async`ronous function](https://docs.python.org/3/library/asyncio-task.html)
```py
@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("----" * 20)
```
*   We print to the client's server's console information about our client as soon as the client has logged in and successfully connected to Discord

## `on_message`
*   Register with `client.event` decorator
*   Must be an [`async`ronous function](https://docs.python.org/3/library/asyncio-task.html)
```py
@client.event
async def on_message(message):
    print(f"""\
Just got a message from {message.author} at {message.created_at}, saying...

{message.content}

{message=}
{'----' * 20}
""")
```
*   This event will log received messages to the client's server's console
*   We can add the following check at the start of the function to ensure we don't log any messages our bot sends
```py
if message.author == client.user: return
```

Now, we aim to make our bot process messages as commands. Let us design something that works like the following:
*   If a message begins with the string `"$ "`...
    *   Check the first word after `"$ "`; this is the command
    *   If the command is `echo`
        *   Send a message to the Discord server containing everything after the command
    *   If the command is `repeat`
        *   Send `randint(2, 5)` messages to the Discord server containing everything after the command

We could attach this fucntionality 
```py
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
```
*   We must use `await` to `send` a message; we must wait for the message to send before continuing our program's execution 

There has to be a better way to define and add commands like this, right...?

# Discord `commands.Bot` Client Subclass
The commands.Bot class was designed for this exact command pattern we attempted above. It can easily be used to define a Discord bot command interface. The `commands.Bot` class is a subclass of the `Client` class, meaning it has *all* the functionalities of the `Client` class we were working with earlier, and more! The `commands.Bot` subclass overrides the `on_message` event to define functionality that processes commands sent to it. This subclass has many additional helpful attributes and methods defined on it.

We can set the following attributes on a `commands.Bot` object.
*   `command_prefix` : The string that a message must start with to be processed as a command
*   `description` : A description of the bot used in it's help message
*   `intents` : The same intents object given to the previously defined `Client`

We must ensure that the `on_message` event is *not* defined on this `commands.Bot` client.  
```py
from nextcord.ext import commands
...
# Replace client = nextcord.Client(...)
bot = commands.Bot(command_prefix="$ ", intents=myIntents, description="Test Bot!")
# Any reference to `client` is now changed to `bot`; `bot` has all attributes and methods of a client!
...
# Remove the `on_message` function entirely; THIS IS VERY IMPORTANT
...
```

We can now start defining commands for our bot to process, utilizing the [`bot.command()`](https://nextcord.readthedocs.io/en/latest/ext/commands/api.html?highlight=bot%20command#nextcord.ext.commands.Bot.command) decorator. 

```py
...
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
...
# Run the bot the same way we ran the client with bot.run(token)
```

At this point, we have a fully functioning Discord bot with numerous commands that can be interfaced with. 

# LECTURER NOTES
At this point, the code should match `main_bot.py`

## `commands.Bot` Default Help Command
We can get information about the commands we have defined on our bot by sending the message `$ help`. We can ask for help information on specific commands with `$ help [command]`.

```
DiscordUser> $ help
Discord Bot>
​No Category:
  add     Adds two integers together
  doc     pins the incredibly important message you just sent
  echo    Repeats a given message
  help    Shows this message
  members List all members
  ping    Will respond with the message 'pong'
  repeat  Repeats a message num times

Type $ help command for more info on a command.
You can also type $ help category for more info on a category.
DiscordUser> $ help repeat
Discord Bot>
$ repeat <num> <msg>

Repeats a message num times
```

## `on_message` Event With `commands.Bot` Class
Sometimes you want to still have access to controlling your bot's behavior when a message is received. If one were to naively implement the event `on_message` on a `commands.Bot` client, the functionality to parse commands will break. Instead, one can attach another function to *listen* to the existing `on_message` event; allowing you to add functionality on a message without effecting the command processing.

```py
# The *wrong* way to add an on_message event to the bot class
#   This will override the actual command interface functionality of the commands.Bot class
#   @bot.event
#   async def on_message(message):
#       print(message.content)

# Allows the following function to respond to the same event that triggers on_message
#   I can attach my own on_message functionality without breaking the command.Bot functionality
@bot.listen('on_message')
async def my_on_message(message):
    # Could log messages to external file here if desired
    print(message.content)
```
