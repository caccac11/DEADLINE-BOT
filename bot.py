import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True  # nhớ bật Message Content Intent trong Developer Portal

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Đăng nhập thành công: {bot.user} (ID: {bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

if __name__ == "__main__":
    keep_alive()  # khởi động web keep-alive
    bot.run(os.environ["DISCORD_TOKEN"])
