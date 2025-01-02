import logging, os, random
import asyncio

from pyrogram import filters, enums, Client, __version__ as pyro_version
from pyrogram.types import *

import requests

log = logging.getLogger(__name__)


# enable logging
FORMAT = "[Nekos-Best-Bot] %(message)s"
logging.basicConfig(
    level=logging.INFO, format=FORMAT
)
  

API_ID = os.environ.get("API_ID", 29593257)
API_HASH = os.environ.get("API_HASH", "e9a3897c961f8dce2a0a88ab8d3dd843")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7106418611:sjsjkskekek")
SUPPORT = os.environ.get("SUPPORT", "NandhaSupport")
UPDATES = os.environ.get("UPDATES", "NandhaBots")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "NekosBestBot") 
BOT_URL = f"https://t.me/{BOT_USERNAME}"
PORT = int(os.environ.get("PORT", 8080))
BIND_ADDRESS = str(os.environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))



bot = Client(
  name="nekosbest",
  api_id=int(API_ID),
  api_hash=API_HASH,
  bot_token=BOT_TOKEN
)


buttons = [[
            InlineKeyboardButton("➕ Add Me To Group ➕", url=f"t.me/{BOT_USERNAME}?startgroup"),
],[
            
            InlineKeyboardButton("🆘 Help Plugin", callback_data="help_back"),
          
],[
            InlineKeyboardButton("👥 Support", url=f"https://t.me/{SUPPORT}"),
            InlineKeyboardButton("📢 Updates", url=f"https://t.me/{UPDATES}")]]



PM_START_TEXT = """
**Welcome** {}~kun ฅ(≈>ܫ<≈)
`I'm A Neko Themed Telegram Bot Using Nekos.best! `
**Make Your Groups Active By Adding Me There! ××**
"""




####################################################################################################

# some funny entertainment plugins

@bot.on_message(filters.command("meme"))
async def meme(_, message):
      response = requests.get("https://nandhabots-api.vercel.app/meme")
      if response.status_code == 200:
           response_json = response.json()
           caption = response_json["title"]
           photo = response_json["image"]
           meme_id = response_json["meme_id"]
           return await message.reply_photo(
                photo=photo,
                caption=f"**{caption}** — `{meme_id}`")
      else:
         return await m.reply("🙀 Error...")



####################################################################################################

# developer plugins

import sys
import io
import time
import os
import subprocess
import traceback
import pyrogram as pyro

async def aexec(code, bot, message, my, m, r, ru):
    exec(
        "async def __aexec(bot, message, my, m, r, ru): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](bot, message, my, m, r, ru)


 
def p(*args, **kwargs):
    print(*args, **kwargs)


@bot.on_message(filters.command('sh') & filters.user([5696053228]))
async def shell_command(bot, message):
     if len(message.text.split()) < 2:
         return await message.reply("🤔 Shell command to execute??")
     command = message.text.split(maxsplit=1)[1]

     msg = await message.reply("**--> Shell command processing....**", quote=True)
     shell_output = subprocess.getoutput(command)
  
     if len(shell_output) > 4000:
          with open("shell.txt", "w+") as file: 
               file.write(shell_output)
          await msg.delete()
          await message.reply_document(
              document="shell.txt",
              quote=True
          )
          os.remove("shell.txt"); return
     else:
         await msg.edit_text(f"```py \n{shell_output}```")
          
              


@bot.on_message(filters.command('e') & filters.user([5696053228]))
async def evaluate(bot, message):
    
    status_message = await message.reply("`Running Code...`")
    try:
        cmd = message.text.split(maxsplit=1)[1]
    except IndexError:
        await status_message.delete()
        return
    start_time = time.time()

    r = message.reply_to_message	
    m = message
    my = getattr(message, 'from_user', None)
    ru = getattr(r, 'from_user', None)

    if r:
        reply_to_id = r.id
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None
    try:
        await aexec(
		   code=cmd, 
    	 message=message,
    	 my=my,
		m=message, 
		r=r,
		ru=ru,
		bot=bot
	)
    except Exception:
        exc = traceback.format_exc()
    stdout = redirected_output.getvalue()
    stderr = redirected_error.getvalue()
    sys.stdout = old_stdout
    sys.stderr = old_stderr
    evaluation = ""
    if exc:
        evaluation = exc
    elif stderr:
        evaluation = stderr
    elif stdout:
        evaluation = stdout
    else:
        evaluation = "Success"
    taken_time = round((time.time() - start_time), 3)
    output = evaluation.strip()
    format_text = "<pre>Command:</pre><pre language='python'>{}</pre> \n<pre>Takem Time: {}'s:</pre><pre language='python'> {}</pre>"
    final_output = format_text.format(cmd, taken_time, output)
	
    if len(final_output) > 4096:
        filename = "output.txt"
        with open(filename, "w+") as out_file:
            out_file.write(str(final_output))
        await message.reply_document(
            document=filename,
            caption=f'`{cmd}`',
            quote=True,
            
        )
        os.remove(filename)
        await status_message.delete()
        return
    else:
        await status_message.edit(final_output, parse_mode=enums.ParseMode.HTML)
        return 
      


####################################################################################################




####################################################################################################

#inline for @nekosBestBot


NEKOS_BEST = {"neko":{"format":"png"},"waifu":{"format":"png"},"husbando":{"format":"png"},"kitsune":{"format":"png"},"lurk":{"format":"gif"},"shoot":{"format":"gif"},"sleep":{"format":"gif"},"shrug":{"format":"gif"},"stare":{"format":"gif"},"wave":{"format":"gif"},"poke":{"format":"gif"},"smile":{"format":"gif"},"peck":{"format":"gif"},"wink":{"format":"gif"},"blush":{"format":"gif"},"smug":{"format":"gif"},"tickle":{"format":"gif"},"yeet":{"format":"gif"},"think":{"format":"gif"},"highfive":{"format":"gif"},"feed":{"format":"gif"},"bite":{"format":"gif"},"bored":{"format":"gif"},"nom":{"format":"gif"},"yawn":{"format":"gif"},"facepalm":{"format":"gif"},"cuddle":{"format":"gif"},"kick":{"format":"gif"},"happy":{"format":"gif"},"hug":{"format":"gif"},"baka":{"format":"gif"},"pat":{"format":"gif"},"nod":{"format":"gif"},"nope":{"format":"gif"},"kiss":{"format":"gif"},"dance":{"format":"gif"},"punch":{"format":"gif"},"handshake":{"format":"gif"},"slap":{"format":"gif"},"cry":{"format":"gif"},"pout":{"format":"gif"},"handhold":{"format":"gif"},"thumbsup":{"format":"gif"},"laugh":{"format":"gif"}}



def get_InputMediaType(data):
       format = data['format']
  
       if format == "png":
            return InlineQueryResultPhoto
       elif format == "gif":
            return InlineQueryResultAnimation
         
       raise Exception(f'Unkown media type found for get_InputMediaType: {format}')



def convert_button(data, columns):
    buttons = [InlineKeyboardButton(switch_inline_query_current_chat=q) for q in data]
    result = []
    
    for i in range(0, len(buttons), columns):
        result.append(buttons[i:i + columns])
    
    # If the last row has fewer columns, append it to the result
    if len(result[-1]) < columns:
        result[-1].extend(buttons[len(result[-1]):])

    # If still, there are buttons left, add a new row with them
    if len(result[-1]) > columns:
        extra_buttons = result[-1][columns:]
        result[-1] = result[-1][:columns]
        result.append(extra_buttons)
    
    return result




NEKOS_BUTTONS = convert_button(
    [InlineKeyboardButton(q, switch_inline_query_current_chat=q) for q in list(NEKOS_BEST)],
    columns=3
)


@bot.on_inline_query()
async def inline(bot, query):
    q = query.query
    inline_query_id = query.id

    if not q:
        results = [
            InlineQueryResultArticle(
                title="Query Not Found! 🚫",
                input_message_content=InputTextMessageContent(message_text="Query not found! I needed an endpoint senpai 🔎"),
                reply_markup=InlineKeyboardMarkup(NEKOS_BUTTONS)
            )
        ]
        return await bot.answer_inline_query(inline_query_id, results)

    pattern = q.split()[0]
    src = NEKOS_BEST.get(pattern)
    if not src:
        results = [
            InlineQueryResultArticle(
                title="Given Query Not Found! 😅",
                input_message_content=InputTextMessageContent(message_text="Given query is not found! Please use a valid endpoint senpai 🔎"),
                reply_markup=InlineKeyboardMarkup(NEKOS_BUTTONS)
            )
        ]
        return await bot.answer_inline_query(inline_query_id, results)

    results = []
    api_url = f"https://nekos.best/api/v2/{pattern}?amount=20"
    api_result = requests.get(api_url).json()
    data_result = api_result['results']
    media_type = get_InputMediaType(src)
    for data in data_result:
        buttons = [
            [InlineKeyboardButton('🔎 Source', url=data.get('source_url', BOT_URL)),
             InlineKeyboardButton('👤 Artist', url=data.get('artist_href', BOT_URL))],
            [InlineKeyboardButton(pattern, switch_inline_query_current_chat=pattern)]
        ]
        text = (
            f"✨ **Result for {pattern}**\n\n"
            f"📛 **Artist**: {data.get('artist_name', BOT_USERNAME)}\n"
            f"❤️ **By @{BOT_USERNAME}**"
        )
        results.append(
            media_type(
                data['url'],
                reply_markup=InlineKeyboardMarkup(buttons)
            )
        )
    return await bot.answer_inline_query(inline_query_id, results, cache_time=2)


                                  

####################################################################################################


@bot.on_message(filters.command(["start","help"]))
async def start(_, m):
       url = "https://nekos.best/api/v2/neko"
       r = requests.get(url)
       e = r.json()
       NEKO_IMG = e["results"][0]["url"]
       await m.reply_photo(photo=NEKO_IMG,caption=PM_START_TEXT.format(m.from_user.mention),
             reply_markup=InlineKeyboardMarkup(buttons))

HELP_TEXT = """
**Anime Themed SFW:**
• Kiss : /kiss To Kiss A Person
• Highfive : /highfive To Highfive A Person
• Happy : /happy To Makes A Person Happy
• Laugh : /laugh To Makes A Person Laugh
• Bite : /bite To Bite A Person
• Poke : /poke To Poke A Person
• Tickle : /tickle To Tickle A Person
• Wave : /wave To Wave A Person
• Thumbsup : /thumbsup To Thumbsup A Person
• Stare : /stare To Makes A Person Stare
• Cuddle : /cuddle To Cuddle A Person
• Smile : /smile To Makes A Person Smile
• Baka : /baka To Say A Person Baka
• Blush : /blush To Makes A Person Blush

✨ **Press 'More' for know more commands.**
"""

@bot.on_callback_query(filters.regex("help_back"))
async def helpback(_, query: CallbackQuery):
           query = query.message
           await query.edit_caption(HELP_TEXT,
             reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("More", callback_data="more_help_text"),
                InlineKeyboardButton("Info", callback_data="about_back")]]))

ABOUT_TEXT = """
**Hello Dear Users!**
`I'm A Neko Themed Telegram Bot Using Nekos.best! `

**My Pyro version**: `{}`
**My Updates**: @NandhaBots
**My Support**: @NandhaSupport

⚡ **Source**: 
https://github.com/NandhaXD/nekosBestBot
"""

@bot.on_callback_query(filters.regex("about_back"))
async def about(_, query: CallbackQuery):
           query = query.message
           await query.edit_caption(ABOUT_TEXT.format(str(pyro_version)),
             reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Back", callback_data="help_back")]]))

MORE_HELP_TEXT = """
**Anime themed SFW:**
• Think : /think To Makes A Person Think
• Pout : /pout To Makes A Person Pout
• Facepalm : /facepalm To Makes A Person Facepalm
• Wink : /wink To Makes A Person Wink
• Smug : /smug To Makes A Person Smug
• Cry : /cry To Makes A Person Cry
• Dance : /dance To Makes A Person Dance
• Feed : /feed To Feed A Person
• Shrug : /shrug To Shrug A Person
• Bored : /bored To Makes A Person Bored
• Pat : /pat To Pat A Person
• Hug : /hug To Hug A Person
• Slap : /slap To Slap A Person
• Cute : /cute To Say Me Cute
• Waifu : /waifu To Send Random Waifu Image
• Kitsune : /kitsune To Send Random Kitsune Image
• Sleep : /sleep To Say I Am Going To Sleep
• Neko : /neko To Get Random Neko quotes with image
• OWO : /owo To Get Random Neko owo quotes
• MEME: /meme get random meme.
"""

@bot.on_callback_query(filters.regex("more_help_text"))
async def helpmore(_, query: CallbackQuery):
           query = query.message
           await query.edit_caption(MORE_HELP_TEXT,
             reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton("Back", callback_data="help_back")]]))


OWO = (
    "*Neko pats {} on the head.",
    "*gently rubs {}'s head*.",
    "*Neko mofumofus {}'s head*",
    "*Neko messes up {}'s head*",
    "*Neko intensly rubs {}'s head*",
    "*{}'s waifu pats their head*",
    "*{}'s got free headpats*",
    "No pats for {}!",
    "*Neko gives {} a gentle headbutt*",
    "*{} gets a surprise headpat*",
    "*Neko nuzzles {}'s cheek*",
    "*{} receives a soft paw tap*",
    "*Neko curls up on {}'s lap*",
    "*{} gets a playful ear flick*",
    "*Neko purrs loudly for {}*",
    "*{} gets a warm kitty hug*",
    "*Neko boops {}'s nose*",
    "*{} gets a fluffy tail swish*",
    "*Neko snuggles close to {}*",
    "*{} gets a loving head rub*",
    "*Neko gives {} a playful nip*",
    "*{} gets a gentle paw poke*",
    "*Neko wraps tail around {}*",
    "*{} gets a soft whisker tickle*",
    "*Neko gazes lovingly at {}*",
    "*{} gets a cozy nap buddy*",
    "*Neko gives {} a sweet meow*",
    "*{} gets a friendly paw shake*",
    "*Neko licks {}'s hand*",
    "*{} gets a playful pounce*",
    "*Neko rolls over for {}*",
    "*{} gets a happy kitty dance*",
    "*Neko chirps at {}*",
    "*{} gets a gentle tail flick*",
    "*Neko gives {} a soft nuzzle*",
    "*{} gets a curious head tilt*",
    "*Neko purrs contentedly for {}*",
    "*{} gets a warm kitty cuddle*"
)

neko_text = (
    "(*)^(*) *lazy arrival* zzzZZ(Z){}-kun I'm hungry...",
    "OwO why are calling me *wags tail in excitement* {} Do you have have cookies?",
    "^~^ *peeks by wall* Oh! {} Meowwww",
    "Ara Ara! {} Do you wanna play? *raises cat ears* ^attentive^",
    "($^$) *money face* {} are you rich UwU?",
    "Hello UwU {} I'm here to play, Meow",
    "(*_*) {}-sama, I'm feeling sleepy... *yawn*",
    "OwO {} Is it snack time yet? *tail swishes happily*",
    "^v^ *waves paw* Hello {}! Are you ready for an adventure?",
    "UwU {} Have you seen my ball of yarn? *looks around*",
    "(*_*) {}-nyan, can we cuddle? *purrs softly*",
    "OwO {}-chan, let's chase butterflies in the garden!",
    "^-^ *sniffs air* I smell food! Is it you, {}?",
    "Ara Ara! {}-sama, can you pet me? *ears perk up*",
    "($.$) {}-kun, do you have some shiny coins for me?",
    "Meowww! {}-nyan, let's climb some trees! *stretches*",
    "(^-^) *licks paw* Hey {}! What are you doing?",
    "OwO {}-chan, let's play hide and seek! *wags tail*",
    "(*u*) {}-sama, will you share your lunch with me?",
    "Ara Ara! {}-kun, your lap looks comfy! *jumps on lap*",
    "(*_*) {}-nyan, it's time for a catnap. Join me?",
    "OwO {}-chan, I found a new toy! Want to see?",
    "^~^ *peeks from corner* Hi {}! Can we play?",
    "Ara Ara! {}-sama, do you want to hear a purr-fect story?",
    "(*_*) {}-nyan, let's watch the sunset together.",
    "UwU {}-kun, can you scratch behind my ears? *leans in*"
)


@bot.on_message(filters.command("kiss"))
async def kiss(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/kiss"
       r = requests.get(url)
       e = r.json()
       kissme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(kissme, caption="*{} kisses {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/kiss"
      r = requests.get(url)
      e = r.json()
      kissme = e["results"][0]["url"]
      await message.reply_video(kissme, caption="*Kisses u with all my love*~")
      return

@bot.on_message(filters.command("highfive"))
async def highfive(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/highfive"
       r = requests.get(url)
       e = r.json()
       highfiveme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(highfiveme, caption="*{} highfives {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/highfive"
      r = requests.get(url)
      e = r.json()
      highfiveme = e["results"][0]["url"]
      await message.reply_video(highfiveme, caption="*Highfives U With All My Friendship*~")
      return

@bot.on_message(filters.command("happy"))
async def happy(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/happy"
       r = requests.get(url)
       e = r.json()
       happyme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(happyme, caption="*{} Is So Happy Today Did You Know {} ?*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/happy"
      r = requests.get(url)
      e = r.json()
      happyme = e["results"][0]["url"]
      await message.reply_video(happyme, caption="*U So Happy Today But Why*~")
      return

@bot.on_message(filters.command("laugh"))
async def laugh(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/laugh"
       r = requests.get(url)
       e = r.json()
       laughme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(laughme, caption="*{} Is Laughed By {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/laugh"
      r = requests.get(url)
      e = r.json()
      laughme = e["results"][0]["url"]
      await message.reply_video(laughme, caption="*I Can't Control Laughing*~")
      return

@bot.on_message(filters.command("bite"))
async def bite(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/bite"
       r = requests.get(url)
       e = r.json()
       biteme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(biteme, caption="*{} Bites {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/bite"
      r = requests.get(url)
      e = r.json()
      biteme = e["results"][0]["url"]
      await message.reply_video(biteme, caption="*Bites u with all my strength*~")
      return

@bot.on_message(filters.command("poke"))
async def poke(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/poke"
       r = requests.get(url)
       e = r.json()
       pokeme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(pokeme, caption="*{} pokes {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/poke"
      r = requests.get(url)
      e = r.json()
      pokeme = e["results"][0]["url"]
      await message.reply_video(pokeme, caption="*Poking You Continuously*~")
      return

@bot.on_message(filters.command("tickle"))
async def tickle(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/tickle"
       r = requests.get(url)
       e = r.json()
       tickleme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(tickleme, caption="*{} tickles {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/tickle"
      r = requests.get(url)
      e = r.json()
      tickleme = e["results"][0]["url"]
      await message.reply_video(tickleme, caption="*Tickling You Continuously Don't Laugh*~")
      return

@bot.on_message(filters.command("wave"))
async def wave(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/wave"
       r = requests.get(url)
       e = r.json()
       waveme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(waveme, caption="*{} waves {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/wave"
      r = requests.get(url)
      e = r.json()
      waveme = e["results"][0]["url"]
      await message.reply_video(waveme, caption="*My Hand Waving To You*~")
      return

@bot.on_message(filters.command("thumbsup"))
async def thumbsup(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/thumbsup"
       r = requests.get(url)
       e = r.json()
       thumbsupme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(thumbsupme, caption="*{} thumbsups with {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/thumbsup"
      r = requests.get(url)
      e = r.json()
      thumbsupme = e["results"][0]["url"]
      await message.reply_video(thumbsupme, caption="*Hey Come Let's Thumbsup*~")
      return

@bot.on_message(filters.command("stare"))
async def stare(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/stare"
       r = requests.get(url)
       e = r.json()
       stareme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(stareme, caption="*{} stares {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/stare"
      r = requests.get(url)
      e = r.json()
      stareme = e["results"][0]["url"]
      await message.reply_video(stareme, caption="*What You Said Say It Again*~")
      return

@bot.on_message(filters.command("cuddle"))
async def cuddle(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/cuddle"
       r = requests.get(url)
       e = r.json()
       cuddleme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(cuddleme, caption="*{} cuddles {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/cuddle"
      r = requests.get(url)
      e = r.json()
      cuddleme = e["results"][0]["url"]
      await message.reply_video(cuddleme, caption="*Cuddle u with all my love*~")
      return

@bot.on_message(filters.command("smile"))
async def smile(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/smile"
       r = requests.get(url)
       e = r.json()
       smileme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(smileme, caption="*{} smiles by seeing {}'s face*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/smile"
      r = requests.get(url)
      e = r.json()
      smileme = e["results"][0]["url"]
      await message.reply_video(smileme, caption="*Is Smiles Looking Beautiful ?*~")
      return

@bot.on_message(filters.command("baka"))
async def baka(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/baka"
       r = requests.get(url)
       e = r.json()
       bakame = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(bakame, caption="*{} said {} is baka*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/baka"
      r = requests.get(url)
      e = r.json()
      bakame = e["results"][0]["url"]
      await message.reply_video(bakame, caption="*You A Stupid Baka!*~")
      return

@bot.on_message(filters.command("blush"))
async def blush(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/blush"
       r = requests.get(url)
       e = r.json()
       blushme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(blushme, caption="*{} blushes by seeing {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/blush"
      r = requests.get(url)
      e = r.json()
      blushme = e["results"][0]["url"]
      name1 = message.from_user.first_name
      await message.reply_video(blushme, caption="*Oh {}~kun I Luv You*~".format(name1))
      return

@bot.on_message(filters.command("think"))
async def think(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/think"
       r = requests.get(url)
       e = r.json()
       thinkme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(thinkme, caption="*{} thoughts about {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/think"
      r = requests.get(url)
      e = r.json()
      thinkme = e["results"][0]["url"]
      name = message.from_user.first_name
      await message.reply_video(thinkme, caption="*{}~kun Do You Love Me?*~".format(name))
      return

@bot.on_message(filters.command("pout"))
async def pout(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/pout"
       r = requests.get(url)
       e = r.json()
       poutme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(poutme, caption="*{} pouts {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/pout"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.first_name
      poutme = e["results"][0]["url"]
      await message.reply_video(poutme, caption="*Oi {}~kun*~".format(name))
      return

@bot.on_message(filters.command("facepalm"))
async def facepalm(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/facepalm"
       r = requests.get(url)
       e = r.json()
       facepalmme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(facepalmme, caption="*{} Made {} To Facepalm*~".format(name2, name1))
       return
    else:
      url = "https://nekos.best/api/v2/facepalm"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.first_name
      facepalmme = e["results"][0]["url"]
      await message.reply_video(facepalmme, caption="*Oh Shit {}~kun*~".format(name))
      return

@bot.on_message(filters.command("wink"))
async def wink(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/wink"
       r = requests.get(url)
       e = r.json()
       winkme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(winkme, caption="*{} winks {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/wink"
      r = requests.get(url)
      e = r.json()
      winkme = e["results"][0]["url"]
      await message.reply_video(winkme, caption="*Winks u with all my love*~")
      return

@bot.on_message(filters.command("smug"))
async def smug(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/smug"
       r = requests.get(url)
       e = r.json()
       smugme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(smugme, caption="*{} sumgs {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/smug"
      r = requests.get(url)
      e = r.json()
      smugme = e["results"][0]["url"]
      await message.reply_video(smugme, caption="*Hehehehehehehehe*~")
      return

@bot.on_message(filters.command("cry"))
async def cry(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/cry"
       r = requests.get(url)
       e = r.json()
       cryme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(cryme, caption="*{} is cried did you know {}?*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/cry"
      r = requests.get(url)
      e = r.json()
      cryme = e["results"][0]["url"]
      await message.reply_video(cryme, caption="*I Can't Stop Crying*~")
      return

@bot.on_message(filters.command("dance"))
async def dance(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/dance"
       r = requests.get(url)
       e = r.json()
       danceme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(danceme, caption="*{} danced with {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/dance"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.first_name
      danceme = e["results"][0]["url"]
      await message.reply_video(danceme, caption="*{}~kun. Can You Dance With Me*~".format(name))
      return

@bot.on_message(filters.command("feed"))
async def feed(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/feed"
       r = requests.get(url)
       e = r.json()
       feedme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(feedme, caption="*{} feeds {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/feed"
      r = requests.get(url)
      e = r.json()
      feedme = e["results"][0]["url"]
      name = message.from_user.first_name
      await message.reply_video(feedme, caption="*Open You Mouth {}~kun*~".format(name))
      return

@bot.on_message(filters.command("shrug"))
async def shrug(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/shrug"
       r = requests.get(url)
       e = r.json()
       shrugme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(shrugme, caption="*{} shrugs to {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/shrug"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.first_name
      shrugme = e["results"][0]["url"]
      await message.reply_video(shrugme, caption="*I Don't Know About It {}~kun*~".format(name))
      return

@bot.on_message(filters.command("bored"))
async def bored(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/bored"
       r = requests.get(url)
       e = r.json()
       boredme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(boredme, caption="*{} bored to see {}*~".format(name1, name2))
       return
    else:
      url = "https://nekos.best/api/v2/bored"
      r = requests.get(url)
      e = r.json()
      name = message.from_user.first_name
      boredme = e["results"][0]["url"]
      await message.reply_video(boredme, caption="*Today Was So Boring {}~kun Any Idea?*~".format(name))
      return


@bot.on_message(filters.command("pat"))
async def pat(_, message):
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/pat"
       r = requests.get(url)
       e = r.json()
       patme = e["results"][0]["url"]
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(patme, caption="*{} pats {}*~".format(name1, name2))
    else:    
      name = (
          message.reply_to_message.from_user.first_name
          if message.reply_to_message
          else message.from_user.first_name
      )
      url = "https://nekos.best/api/v2/pat"
      r = requests.get(url)
      e = r.json()
      patme = e["results"][0]["url"]
      await message.reply_video(patme, caption=random.choice(OWO).format(name))

@bot.on_message(filters.command("hug"))
async def hug(_, message):
    
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/hug"
       r = requests.get(url)
       e = r.json()
       hugme = e["results"][0]["url"]
       
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(hugme, caption="*{} hugs {}*".format(name1, name2))
    else:
       url = "https://nekos.best/api/v2/hug"
       r = requests.get(url)
       e = r.json()
       hugme = e["results"][0]["url"]
       
       await message.reply_video(hugme, caption="*Hugs u with all my love*~")

@bot.on_message(filters.command("slap"))      
async def slap(_, message):
    
    if message.reply_to_message:
       url = "https://nekos.best/api/v2/slap"
       r = requests.get(url)
       e = r.json()
       slapme = e["results"][0]["url"]
       
       name1 = message.from_user.first_name
       name2 = message.reply_to_message.from_user.first_name
       await message.reply_to_message.reply_video(slapme, caption="*{} slaps {}*".format(name1, name2))
    else:
       url = "https://nekos.best/api/v2/slap"
       r = requests.get(url)
       e = r.json()
       slapme = e["results"][0]["url"]
       
       await message.reply_video(slapme, caption="Here... Take this from me.")

@bot.on_message(filters.command("cute"))
async def cute(_, message):
    name = message.from_user.first_name         
    url = f"https://nekos.best/api/v2/neko"
    r = requests.get(url)
    e = r.json()
    cuteme = e["results"][0]["url"]
    await message.reply_photo(
        cuteme, caption="Thank UwU {}-Kun  *smiles and hides ^~^*".format(name)
    )

@bot.on_message(filters.command("waifu"))
async def waifu(_, message):
    name = message.from_user.first_name         
    url = f"https://nekos.best/api/v2/waifu"
    r = requests.get(url)
    e = r.json()
    waifume = e["results"][0]["url"]
    await message.reply_photo(
        waifume, caption="Here I Am {}-Kun's *Waifu*".format(name)
    )

@bot.on_message(filters.command("kitsune"))
async def kitsune(_, message):
    name = message.from_user.first_name         
    url = f"https://nekos.best/api/v2/kitsune"
    r = requests.get(url)
    e = r.json()
    kitsuneme = e["results"][0]["url"]
    await message.reply_photo(
        kitsuneme, caption="Did You Called Me {}-Kun's *?*".format(name)
    )

@bot.on_message(filters.command("sleep"))
async def sleep(_, message):
    sleep_type = random.choice(("Text", "Gif", "Video"))
    if sleep_type == "Gif":
        try:
            url = "https://nekos.best/api/v2/sleep"
            r = requests.get(url)
            e = r.json()
            sleepme = e["results"][0]["url"]
            await message.reply_video(sleepme)
          
        except BadRequest:
            sleep_type = "Text"

    if sleep_type == "Video":
        try:
            bed = "https://telegra.ph/file/f0fb71c72e059de34b565.mp4"
            await message.reply_video(bed)
        except BadRequest:
            sleep_type = "Text"

    if sleep_type == "Text":
        z = ". . . (∪｡∪)｡｡｡zzzZZ"
        await message.reply_text(z)


@bot.on_message(filters.command("owo"))
async def owo(_, message):
    name = message.from_user.first_name
    ke = random.choice(OWO)
    await message.reply_text(
        ke.format(name)
    )


@bot.on_message(filters.command("neko"))
async def neko(_, message):
    name = message.from_user.first_name
    ke = random.choice(neko_text)
    url = "https://nekos.best/api/v2/neko"
    r = requests.get(url)
    e = r.json()
    img = e["results"][0]["url"]
    await message.reply_photo(photo=img,
        caption=ke.format(name)
    )






from web import keep_alive, web_server
from aiohttp import web

async def start_services():        
        server = web.AppRunner(web_server())
        await server.setup()
        await web.TCPSite(server, BIND_ADDRESS, PORT).start()
        log.info("Web Server Initialized Successfully")
        log.info("=========== Service Startup Complete ===========")
  
        asyncio.create_task(keep_alive())
        log.info("Keep Alive Service Started")
        log.info("=========== Initializing Web Server ===========")
        

if __name__ == "__main__":
     loop = asyncio.get_event_loop()
     loop.run_until_complete(start_services())
     bot.run()
     log.info('Bot Started!')
     
