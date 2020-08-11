from riotwatcher import LolWatcher, ApiError
import pandas as pd
#import json

api_key = 'RGAPI-fe1de2e8-a919-470a-a7c8-6c86a3f2d74c'
watcher = LolWatcher(api_key)
region = 'na1'

player = watcher.summoner.by_name(region, 'jankykf')
#use jankykf for flex and solo stats, ashaowowow for none, and RozeZeal for just solo
print (player)
player_name = player ['name']
player_icon = int (player ['profileIconId'])
player_level = player ['summonerLevel']
print(player_name, player_icon, player_level)

try:
    player_solo_stats, player_flex_stats = watcher.league.by_summoner(region, player['id'])
except ValueError:
    try:
        if (watcher.league.by_summoner(region, player['id'])[0]['queueType'] == 'RANKED_SOLO_5x5'):
            player_solo_stats = watcher.league.by_summoner(region, player['id'])
            player_solo_rank = player_solo_stats [0]['tier']
            player_solo_rank_num = player_solo_stats [0]['rank']
            player_solo_wins = int (player_solo_stats [0]['wins'])
            player_solo_losses = int (player_solo_stats [0]['losses'])
            player_solo_lp = int (player_solo_stats [0]['leaguePoints'])
            print (player_solo_rank, player_solo_rank_num, player_solo_wins, player_solo_losses, player_solo_lp)

        elif (watcher.league.by_summoner(region, player['id'])[0]['queueType'] == 'RANKED_FLEX_SR'):                               
            player_flex_stats = watcher.league.by_summoner(region, player['id'])
            player_flex_rank = player_flex_stats [0]['tier']
            player_flex_rank_num = player_flex_stats [0]['rank']
            player_flex_wins = int (player_flex_stats [0]['wins'])
            player_flex_losses = int (player_flex_stats [0]['losses'])
            player_flex_lp = int (player_flex_stats [0]['leaguePoints'])
            print (player_flex_rank, player_flex_rank_num, player_flex_wins, player_flex_losses, player_flex_lp)

    except IndexError:
        print('no ranked stats')
else: 
    player_solo_rank = player_solo_stats ['tier']
    player_solo_rank_num = player_solo_stats ['rank']
    player_solo_wins = int (player_solo_stats ['wins'])
    player_solo_losses = int (player_solo_stats ['losses'])
    player_solo_lp = int (player_solo_stats ['leaguePoints'])
    print (player_solo_rank, player_solo_rank_num, player_solo_wins, player_solo_losses, player_solo_lp)


    player_flex_rank = player_flex_stats ['tier']
    player_flex_rank_num = player_flex_stats ['rank']
    player_flex_wins = int (player_flex_stats ['wins'])
    player_flex_losses = int (player_flex_stats ['losses'])
    player_flex_lp = int (player_flex_stats ['leaguePoints'])
    print (player_flex_rank, player_flex_rank_num, player_flex_wins, player_flex_losses, player_flex_lp)


    print(player_solo_stats, player_flex_stats)

player_matches = watcher.match.matchlist_by_account(region, player['accountId'])
last_match = player_matches['matches'][0]
match_detail = watcher.match.by_id(region, last_match['gameId'])
print(match_detail)
# start a for loop from here analizing the players stats for each game for trends like killstealing, not warding, etc...
# can write functions to check for each trait 


