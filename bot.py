import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# الرتبة اللي تقدر تستخدم الأمر
ALLOWED_ROLE = "Administrators"

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def sendembed(ctx):
    # التأكد من الصلاحية
    if not any(role.name == ALLOWED_ROLE for role in ctx.author.roles):
        await ctx.send("🚫 ما عندك صلاحية استخدام هذا الأمر.")
        return

    # إعداد الإيمبد بشكل احترافي
    embed = discord.Embed(
        title="📢 عنوان الإعلان",
        description=(
            "🔹 هذا مثال على رسالة إيمبد منسقة.\n"
            "🔹 يمكنك تعديل هذا النص كما تريد.\n"
            "🔹 الإيمبد يحتوي على صورة وأزرار تفاعلية.\n"
        ),
        color=discord.Color.dark_theme()
    )

    embed.set_image(url="http://xxxxxxx.com")  # 🔗 غيّر رابط الصورة

    # 🎨 إيموجيات مخصصة للأزرار (تأكد أنها موجودة في السيرفر!)
    website_emoji = "<:webicon:1372334737263165510>"     # 🔁 غيّر الـ ID
    invite_emoji = "<:inviteicon:1372334739121504266>"   # 🔁 غيّر الـ ID
    custom_emoji = "<:gzlogo:1372334735761866825>"      # هذا اللي عطيتني إياه

    # إعداد الأزرار
    view = discord.ui.View()

    # زر الموقع
    view.add_item(discord.ui.Button(
        label="الزر1",
        url="https://www.xxxxxxx.com/", # غير الموقع 
        style=discord.ButtonStyle.gray,
        emoji=website_emoji
    ))

    # زر دعوة السيرفر
    view.add_item(discord.ui.Button(
        label="الزر2",
        url="https://www.google.com",
        style=discord.ButtonStyle.gray,
        emoji=invite_emoji
    ))

    # زر ثالث مخصص (اختياري - ضيفه لاحقاً)
    view.add_item(discord.ui.Button(
        label="الزر33",
        url="https://www.google.com",  # 🔁 غيّر الرابط حسب احتياجك
        style=discord.ButtonStyle.gray,
        emoji=custom_emoji
    ))

    await ctx.send(embed=embed, view=view)

bot.run("ضع_توكن_البوت_هنا")

