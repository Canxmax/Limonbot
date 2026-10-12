import discord
from config import token

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Giriş yapıldı:  {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

@bot.event
async def on_member_join(member):
    # Karşılama mesajı gönderme
    for channel in member.guild.text_channels:
        await channel.send(f’ Hoş geldiniz: , {member.mention}!')

async def on_message(message):
    if message.author == bot.user:
        return

    if "patates" in message.content.lower() and not message.content.startswith("!"):
        await message.channel.send("BİRİ PATATES Mİ DEDİ?! 🥔🥔🥔")

    await bot.process_commands(message)                           

client.run(token)
