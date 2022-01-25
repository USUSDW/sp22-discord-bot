import os

import dotenv
import nextcord

# Needed for us to tell Discord what information our bot will want to access
myIntents = nextcord.Intents.default()
# Specifically note that we want access to member information
myIntents.members = True

# Create a Client object, the actual connection to Discord
client = nextcord.Client(intents=myIntents)

# This will load the `.env` file data as a system environment variable
dotenv.load_dotenv()

# Assign variable myToken to be the string in the 'token' environment variable; loaded in .env
myToken = os.getenv("token")

client.run(myToken)