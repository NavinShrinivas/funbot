import discord
import os
from dotenv import load_dotenv
import subprocess

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')


@client.event
async def on_ready():
    print('I AM IN THE MATRIX [logged in]')


@client.event
async def on_message(message):
    print(message)
    if message.author == client.user:
        return

    msgcon=[]
    msgcon=message.content.split(" ")
    caplist=[i.upper() for i in msgcon]
    if "NIV" in caplist or "NIVESH" in caplist or "NIVI" in caplist :
        await message.reply("Nivesh ? he is a pro but an agent hopper.")
             
    if message.content.startswith('$echo'):
        msgcon=[]
        msgcon=message.content.split(" ")
        string = ""
        for i in range(1,len(msgcon)):
            string+=msgcon[i]+" "
        await message.reply(string)
    if message.content.startswith('$ping'):
        await message.channel.send("Pong!")
    if message.content.startswith('$update'):
        retval=subprocess.call(["./update.sh"])
        if retval=="0":
            await message.channel.send("No diff to update or merge.")
        else:
            await message.channel.send("Changes present , Updating...Will notify once done!")

        

client.run(TOKEN)
