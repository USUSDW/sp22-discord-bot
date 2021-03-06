import os

import dotenv
import nextcord

# Needed for us to tell Discord what information our bot will want to access
myIntents = nextcord.Intents.default()
# Specifically note that we want access to member information
myIntents.members = True

# Create a Client object, the actual connection to Discord
client = nextcord.Client(intents=myIntents)

# Tell the client to actually connect to Discord using the API Token provided in ...
client.run(...)