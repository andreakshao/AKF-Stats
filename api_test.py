from riotwatcher import LolWatcher, ApiError
import pandas as pd
#import json

api_key = 'I dont wanna get hacked your key here'
watcher = LolWatcher(api_key)
region = 'na1'

player = watcher.summoner.by_name(region, 'jankykf')
print (player)
player_name = player ['name']
player_icon = int (player ['profileIconId'])
player_level = player ['summonerLevel']
print(player_name, player_icon, player_level)

player_ranked_stats = watcher.league.by_summoner(region, player['id'])
print(player_ranked_stats)
