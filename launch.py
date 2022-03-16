import requests
import os
from time import sleep
from dotenv import load_dotenv
from discord_webhook import DiscordWebhook,DiscordEmbed
import datetime
from Ressources.code.save import *
from Ressources.code.functions import *

load_dotenv()

print('''
           _    _                         _____       _           
          | |  | |                       / ____|     (_)          
          | |__| | ___  _ __   ___ _   _| |  __  __ _ _ _ __      
          |  __  |/ _ \| '_ \ / _ \ | | | | |_ |/ _` | | '_ \     
          | |  | | (_) | | | |  __/ |_| | |__| | (_| | | | | |    
          |_|__|_|\___/|_| |_|\___|\__, |\_____|\__,_|_|_|_|_|___ 
          |  __ \(_)                __/ || | |  _ \ / __ \__   __|
          | |  | |_ ___  ___ ___  _|___/_| | | |_) | |  | | | |   
          | |  | | / __|/ __/ _ \| '__/ _` | |  _ <| |  | | | |   
          | |__| | \__ \ (_| (_) | | | (_| | | |_) | |__| | | |   
          |_____/|_|___/\___\___/|_|  \__,_| |____/ \____/  |_|   
                                                         
                                                         ''')
###### MAIN #####
while True:
  if datetime.now(timezone.utc).strftime("%M") == "00":
    webhook = DiscordWebhook(url=str(os.getenv('DISCORD_CHANNEL')), 
                            username=str(os.getenv('BOT_USERNAME')))
    ######## DEVICE ##############
    response = requests.get("https://dashboard.honeygain.com/api/v2/devices",
    headers={
      "Authorization": "Bearer "+str(os.getenv('JWT_TOKEN'))
    }
    )
    print(response)
    device_data = response.json()
    #print(device_data)
    total_item = device_data['meta']['pagination']['total_items']

    #Android,Windows,MacOS,iOS,Linux,other
    platform_name=["android","windows","macos","ios","linux"]
    platform_nb=[0,0,0,0,0,0]
    active_item=0

    for i in range(total_item):
      if device_data['data'][i]['status']=="active":
        try:
          ind = platform_name.index(device_data['data'][i]['platform'])
          platform_nb[ind]=platform_nb[ind]+1
        except ValueError:
          platform_nb[5]=platform_nb[5]+1
        active_item=active_item+1


    ######## BALANCE ##############
    response = requests.get("https://dashboard.honeygain.com/api/v1/users/balances",
    headers={
      "Authorization": "Bearer "+str(os.getenv('JWT_TOKEN'))
    }
    )
    balance_data = response.json()

    min_payout=convert_cents_to_dollars(balance_data['data']['min_payout']['usd_cents'])
    balance=convert_cents_to_dollars(balance_data['data']['payout']['usd_cents'])



    ######## STATS AJD ##############
    response = requests.get("https://dashboard.honeygain.com/api/v1/earnings/today",
    headers={
      "Authorization": "Bearer "+str(os.getenv('JWT_TOKEN'))
    }
    )
    stats_data = response.json()

    cdn=convert_credits_to_money(stats_data['cdn']['credits'])
    gathering=convert_credits_to_money(stats_data['gathering']['credits'])
    other=convert_credits_to_money(stats_data['other']['credits'])
    referrals=convert_credits_to_money(stats_data['referral']['credits'])
    winnings=convert_credits_to_money(stats_data['winning']['credits'])
    diff_balance=str(difference("balance",balance))
    embed = DiscordEmbed(
        title="Data Update ! ["+diff_balance+"$]", color='03b2f8'
    )
    embed.set_thumbnail(
                url="https://pbs.twimg.com/profile_images/1214149002700083200/CYslnxfM_400x400.jpg")
    embed.set_footer(text="Min Payout "+str(min_payout)+"$ | You are earning with "+str(active_item)+"/"+str(total_item)+" Devices")
    # Set `inline=False` for the embed field to occupy the whole line
    embed.add_embed_field(name="Gathering", value=str(gathering)+"$ ("+str(difference("gathering",gathering))+"$)")
    embed.add_embed_field(name="Winnings", value=str(winnings)+"$ ("+str(difference("winnings",winnings))+"$)")
    embed.add_embed_field(name="Referrals", value=str(referrals)+"$ ("+str(difference("referrals",referrals))+"$)")
    embed.add_embed_field(name="Content Delivery", value=str(cdn)+"$ ("+str(difference("cdn",cdn))+"$)")
    embed.add_embed_field(name="Other", value=str(other)+"$ ("+str(difference("other",other))+"$)")
    embed.add_embed_field(name="Current Balance", value=str(balance)+"$ ("+diff_balance+"$)")
    embed.add_embed_field(name="Lifetime", value=str(get_value('all','lifetime'))+"$")
    #embed.add_embed_field(name="Min Payout", value=str(min_payout)+"$")

    webhook.add_embed(embed)
    response = webhook.execute()
    sleep(60)
  sleep(10)
