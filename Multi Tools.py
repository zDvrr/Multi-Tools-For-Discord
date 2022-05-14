import discord
from discord.ext import commands
from pystyle import Anime, Colors, Colorate, System, Center, Write
import time
from discord_webhook import DiscordWebhook

ascii_art = r"""
 _______  _______  _       _________         
(  ____ \(  ____ \( (    /|\__   __/|\     /|
| (    \/| (    \/|  \  ( |   ) (   ( \   / )
| (__    | (__    |   \ | |   | |    \ (_) / 
|  __)   |  __)   | (\ \) |   | |     ) _ (  
| (      | (      | | \   |   | |    / ( ) \ 
| )      | (____/\| )  \  |___) (___( /   \ )
|/       (_______/|/    )_)\_______/|/     \|
                                                                                                                                   
                                                                                                                     
"""[1:]

ascii_art_raid_tools = r"""
  _____               _____   _____      _______    ____     ____    _         _____ 
 |  __ \      /\     |_   _| |  __ \    |__   __|  / __ \   / __ \  | |       / ____|
 | |__) |    /  \      | |   | |  | |      | |    | |  | | | |  | | | |      | (___  
 |  _  /    / /\ \     | |   | |  | |      | |    | |  | | | |  | | | |       \___ \ 
 | | \ \   / ____ \   _| |_  | |__| |      | |    | |__| | | |__| | | |____   ____) |
 |_|  \_\ /_/    \_\ |_____| |_____/       |_|     \____/   \____/  |______| |_____/ 
                                                                                     
                                                                                     
"""[1:]

ascii_art_spam_tools = r"""
   _____   _____               __  __     _______    ____     ____    _         _____ 
  / ____| |  __ \      /\     |  \/  |   |__   __|  / __ \   / __ \  | |       / ____|
 | (___   | |__) |    /  \    | \  / |      | |    | |  | | | |  | | | |      | (___  
  \___ \  |  ___/    / /\ \   | |\/| |      | |    | |  | | | |  | | | |       \___ \ 
  ____) | | |       / ____ \  | |  | |      | |    | |__| | | |__| | | |____   ____) |
 |_____/  |_|      /_/    \_\ |_|  |_|      |_|     \____/   \____/  |______| |_____/ 
                                                                                      
"""[1:]

ascii_art_webhook_tools = r"""
 __          __  ______   ____    _    _    ____     ____    _  __    _______    ____     ____    _         _____ 
 \ \        / / |  ____| |  _ \  | |  | |  / __ \   / __ \  | |/ /   |__   __|  / __ \   / __ \  | |       / ____|
  \ \  /\  / /  | |__    | |_) | | |__| | | |  | | | |  | | | ' /       | |    | |  | | | |  | | | |      | (___  
   \ \/  \/ /   |  __|   |  _ <  |  __  | | |  | | | |  | | |  <        | |    | |  | | | |  | | | |       \___ \ 
    \  /\  /    | |____  | |_) | | |  | | | |__| | | |__| | | . \       | |    | |__| | | |__| | | |____   ____) |
     \/  \/     |______| |____/  |_|  |_|  \____/   \____/  |_|\_\      |_|     \____/   \____/  |______| |_____/ 
                                                                                                                  
                                                                                                                                                                                         
                                                                                                
"""[1:]

def systeme():
  Anime.Fade(text=Center.Center(ascii_art), color=Colors.red_to_yellow, mode=Colorate.Horizontal, enter=True)

def init():
    System.Clear()
    System.Size(160, 50)
    System.Title("Discord Multi Tools by Anthoxdu13")
    print(Colorate.Horizontal(color=Colors.red_to_yellow, text=Center.XCenter(ascii_art)))
    mode = int(input(Colorate.Horizontal(Colors.yellow_to_red, "\nQue voulez-vous faire ?\n1 - WebHook Spammer\n2 - Raid Tools\n3 - Messages privée Spammer\n4 - Advenced Webhook Spammer\n\n-> ")))
    if mode == 1:
        webhook_spammer()
    elif mode == 2:
        raid()
    elif mode == 3:
        dm_spammer()
    elif mode == 4:
        advenced_webhook_spammer()

def webhook_spammer():
    System.Title("Multi Tools WebHook Spammer by anthoxdu13")
    print(Colorate.Horizontal(color=Colors.red_to_yellow, text=Center.XCenter(ascii_art_webhook_tools)))
    url = input(Colorate.Horizontal(Colors.yellow_to_red, "\n WebHook Url -> "))
    Msg = input(Colorate.Horizontal(Colors.yellow_to_red, "\n Votre Message -> "))
    print(Colorate.Horizontal(Colors.yellow_to_red, "\n/!\ Le Message Va Être Spam Tant Que Le Tools Est Ouvert !"))
    print(Colorate.Horizontal(Colors.yellow_to_red, "\n/!\ Je Décline Toute Responsabilité Pour Ce Que Vous En Faites."))
    a = input(Colorate.Horizontal(Colors.yellow_to_red, "\nVoulez-Vous Continuer (O/N) -> "))
    if a =="O":
      while True:
        webhook = DiscordWebhook(url=url, content=Msg+" (with Vidar Tools for Discord)")
        response = webhook.execute()
        time.sleep(1)
        print(Colorate.Horizontal(Colors.yellow_to_red, "Le message est partie"))
    else:
      systeme()

def advenced_webhook_spammer():
    System.Title("Multi Tools Advenced WebHook Spammer by anthoxdu13")
    print(Colorate.Horizontal(color=Colors.red_to_yellow, text=Center.XCenter(ascii_art_webhook_tools)))
    print(Colorate.Horizontal(Colors.yellow_to_red, "\n/!\ Vous demandera 3 fois des lien de webhook"))
    url = input(Colorate.Horizontal(Colors.yellow_to_red, "\n WebHook Url 1 -> "))
    url1 = input(Colorate.Horizontal(Colors.yellow_to_red, "\n WebHook Url 2 -> "))
    url2 = input(Colorate.Horizontal(Colors.yellow_to_red, "\n WebHook Url 3 -> "))
    webhook_urls = [url, url1, url2]
    Msg = input(Colorate.Horizontal(Colors.yellow_to_red, "\n Votre Message -> "))
    print(Colorate.Horizontal(Colors.yellow_to_red, "\n/!\ Le Message Va Être Spam Tant Que Le Tools Est Ouvert !"))
    print(Colorate.Horizontal(Colors.yellow_to_red, "\n/!\ Je Décline Toute Responsabilité Pour Ce Que Vous En Faites."))
    a = input(Colorate.Horizontal(Colors.yellow_to_red, "\nVoulez-Vous Continuer (O/N) -> "))
    if a =="O":
      while True:
        webhook = DiscordWebhook(url=webhook_urls, content=Msg)
        response = webhook.execute()
        time.sleep(0.3)
        print(Colorate.Horizontal(Colors.yellow_to_red, "Les messages sont partie"))
    else:
      systeme()

def raid():
    bot = commands.Bot(command_prefix="*")
    System.Title("Multi Tools Raid by anthoxdu13")
    print(Colorate.Horizontal(color=Colors.red_to_yellow, text=Center.XCenter(ascii_art_raid_tools)))
    TOKEN = input(Colorate.Horizontal(Colors.yellow_to_red, "\n Token -> "))
    print(Colorate.Horizontal(Colors.yellow_to_red, "\n Bot préfix '*' !"))
    Nom = input(Colorate.Horizontal(Colors.yellow_to_red, "\n Nom des channels -> "))

    @bot.event
    async def on_ready():
        await bot.change_presence(activity=discord.Streaming(name="[FREE] Vidar Tools", url="https://github.com/anthoxdu13/Vidar-Tools"))
        print(Colorate.Horizontal(Colors.yellow_to_red, "\n Bot Online !"))
        
    @bot.command()
    async def raid(ctx):
        time.sleep(0.3)
        await ctx.message.guild.create_text_channel(f"{Nom}")
        await ctx.message.guild.create_text_channel("With Raids Tools for Discord")
        print(Colorate.Horizontal(Colors.yellow_to_red, "\n Un Channel Créer !"))
        while True:
            await ctx.message.guild.create_text_channel(f"{Nom}")
            time.sleep(0.3)

    bot.run(TOKEN)
    
def dm_spammer():
    System.Title("Multi Tools Dm Spammer")
    print(Colorate.Horizontal(color=Colors.red_to_yellow, text=Center.XCenter(ascii_art_spam_tools)))

systeme()
init()
