import discord
import os
from dotenv import load_dotenv
import subprocess
import os.path

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
    if message.content.startswith('$newtodo'):
        msg_con = message.content.split(' ')
        if len(msg_con)==1:
            await message.reply("Please mention a list name!")
        elif os.path.exists("./"+msg_con[1]+".txt"):
            await message.reply("List with the same name exists!")
        else:
            f=open(msg_con[1]+".txt","w+")
            await message.reply("List created!")

    if message.content.startswith('$deltodo'):
        msg_con=message.content.split(" ")
        if len(msg_con)==1:
            await message.reply("Please mention a list name!")
        elif os.path.exists("./"+msg_con[1]+".txt")==False:
            await message.reply("There exists no list as such")
        else:
            os.remove(msg_con[1]+".txt")
            await message.reply("List deleted!")
    if message.content.startswith('$addwork'):
        msg_con=message.content.split(",")
        if len(msg_con) < 3:
            await message.reply("To add work to a list follow this : ")
            await message.channel.send("$addwork,{listname},{work to do}")
        elif os.path.exists("./"+msg_con[1]+".txt")==False:
            await message.reply("There exist no path as such!")
        else:
            f=open(msg_con[1]+".txt","a")
            f.write(msg_con[2]+"\n")
            f.close()
            fr=open(msg_con[1]+".txt","r")
            await message.reply("Work added!")
            await message.channel.send("Work to do in the list currently : ")
            l=fr.read().split("\n")
            print(l)
            workcount=1
            for i in range(0,len(l)-1):
                await message.channel.send(str(workcount)+"."+l[i])
                workcount+=1
            fr.close()
            await message.channel.send("End of list :)")
    
    if message.content.startswith('$delwork'):
        msg_con=message.content.split(",")
        if len(msg_con) < 3:
            await message.reply("To add work to a list follow this : ")
            await message.channel.send("$delwork,{listname},{list index[1-N]}")
        elif os.path.exists("./"+msg_con[1]+".txt")==False:
            await message.reply("There exists no such list!")
        else:
            fr=open(msg_con[1]+".txt","r")
            f=open(msg_con[1]+".txt","w")
            l=fr.read().split("\n")
            if int(msg_con[2])>len(l) or int(msg_con[2])==0:
                await message.reply("Dear hooman , stop trying to break me with wrong index!")
            else:
                l.remove(l[int(msg_con[2])-1])
                fr.close()
                for i in l:
                    f.write(i)
                f.close()
                await message.reply("Work deleted!")
    if message.content.startswith('$listwork'):#still not added exists checking
        msg_con=message.content.split(" ")
        if len(msg_con)==1:
            await message.reply("Please mention a list name!")
        elif os.path.exists("./"+msg_con[1]+".txt")==False:
            await message.reply("There exists no list as such")
        else:
            fr=open(msg_con[1]+".txt","r")
            await message.reply("Work to do in the list currently : ")
            l=fr.read().split("\n")
            print(l)
            workcount=1
            for i in range(0,len(l)-1):
                await message.channel.send(str(workcount)+"."+l[i])
                workcount+=1
            await message.channel.send("End of list :)")






        

client.run(TOKEN)
