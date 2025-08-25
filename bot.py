import os
import discord
from discord.ext import commands

# Bật quyền đọc nội dung tin nhắn (nhớ bật trong Developer Portal nếu cần)
intents = discord.Intents.default()
intents.message_content = True

# Tạo bot với tiền tố lệnh, ví dụ: !ping
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Đăng nhập thành công: {bot.user} (ID: {bot.user.id})")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

# Lấy token từ biến môi trường (khi deploy trên Render sẽ khai báo ở phần env)
bot.run(os.environ["DISCORD_TOKEN"])
