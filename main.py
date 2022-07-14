import discord
import time
# imports the module that allows you to connect to discord + the token that is like the password
TOKEN = ''

client = discord.Client()
# below is the event for when the bot turns on, it sends a message in client that it is on.
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# returns information from messages into the client always
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')
    
# ensures that it doesnt pick up on its own messages
    if message.author == client.user:
        return

 # saves inputs as a file with the time as the title.   
    if message.channel.name == 'bot-testing':
        userInputs = open('currentinput.sh', 'w', newline='')
# need to add functionality to make a new line. basically i can make a bash file but then there is no line break>
        userInputs.write("#!/bin/bash")
#        
        userInputs.write("\n"+user_message+"\n")
        userInputs.close()
        time.sleep(5)
        terminalOutput = open('currentoutput.txt', 'r')

        f = terminalOutput.read()
        await message.channel.send(f'{f}')
        terminalOutput.close()


client.run(TOKEN)