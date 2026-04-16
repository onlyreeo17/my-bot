import discord
from discord.ext import tasks
from datetime import datetime

T = 'MTQ5Mji3NDE4NzExMTM2Njcx.Gy4p1I.s2CjJh2R'
ID = 149227418711136671

intents = discord.Intents.all()
client = discord.Client(intents=intents)
start = datetime.now()

@tasks.loop(minutes=6)
async def timer():
    try:
        channel = client.get_channel(int(ID))
        if channel:
            now = datetime.now()
            diff = now - start
            days = diff.days
            hours, rem = divmod(diff.seconds, 3600)
            minutes, _ = divmod(rem, 60)
            name = f"Time: {days}d {hours}h {minutes}m"
            await channel.edit(name=name)
    except:
        pass

@client.event
async def on_ready():
    print('online!')
    timer.start()

client.run(T)
