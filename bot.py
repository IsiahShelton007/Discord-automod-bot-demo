import discord # Import discord.py
from discord.ext import commands # Import commands
from discord.ext.commands import Bot # Import bot from discord.py
form token import token # Import token from token.py
from better_profanity import profanity # Import profanity filter

bot = commands.Bot(command_prefix='/')  # Set the command prefix to /

@bot.event # When the bot is ready
async def on_ready(): # When the bot is ready
    print('Bot is ready.') # Print 'Bot is ready.'

@bot.command() # When the command /badwords is used
async def badwords(): 
    await bot.say('You can find a list of bad words here: LINK') # Send a message with a link to a list of bad words
@bot.event # When a message is sent
async def on_message(message):
    if profanity.contains_profanity(message.content): # If the message contains a bad word
        await bot.delete_message(message) # Delete the message
        await bot.send_messages('You can\'t say bad words in this server!') # Send a message saying that bad words are not allowed
    else: # If the message does not contain a bad word
        return 0 # Do nothing
@bot.command() # When the command /ping is used
async def ping():
    await bot.say('Pong!') # Send a message saying 'Pong!'

bot.run(token) # Run the bot with the token
