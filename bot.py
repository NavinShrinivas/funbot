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
    if "niv" in msgcon or "nivesh" in msgcon:
        await message.reply("Nivesh ? he is a pro but an agent hopper.")
             
    if message.content.startswith('$echo'):
        msgcon=[]
        msgcon=message.content.split(" ")
        string = ""
        for i in range(1,len(msgcon)):
            string+=msgcon[i]+" "
        await message.reply(string)
    
    if messag.content.startswith('$update'):
        retval=subprocess.call(["./update.sh"])
        if retval==0:
            await message.channel.send("No diff to update or merge.")
        else:
            await message.channel.send("Changes present , Updating...Will notify once done!")
        

client.run(TOKEN)