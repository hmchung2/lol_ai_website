# # sudo apt-get install chromium-chromedriver
# import os
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import requests

main_api_key = "your api key"



all_lanes = ["TOP100" , "JUNGLE100" , "MID100" , "SUPPORT100" , "ADC100" , "TOP200" , "JUNGLE200" , "MID200" , "SUPPORT200" , "ADC200"  ]
tiers = ["MASTER",
"CHALLENGER",
"GRANDMASTER",
"GOLD",
"PLATINUM",
"DIAMOND",
"SILVER",
"BRONZE"]


main_features = ['target',
 'champ',
 'summonerLevel',
 'tier',
 'rank',
 'wins',
 'losses',
 'veteran',
 #'inactive',
 'freshBlood',
 'hotStreak',
 'champion_levels',
 'champion_points',
 'tokens',
 'ranking_favorite_list',
 'avg_champion_levels',
 'avg_champion_points',
 'avg_tokens',
 'total_champion_games',
 'win_or_loss',
 'kills',
 'deats',
 'assists',
 'total_damage',
 'damage_to_champ',
 'damage_to_objects',
 'champ_level',
 'gold_earned',
 'vision_score',
 'minionskilled',
 'neutral_minions_killed',
 'wards_placed',
 'wards_killed',
 'damage_taken']

feature_relations = {'target':'target',
  'champ':'categ_var',
  'summonerLevel':'good',
  'tier':'good_categ',
  'rank':'bad_categ',
  'wins':'good',
  'losses':'bad',
  'veteran':'good_categ',
  #'inactive':'bad_categ',
  'freshBlood':'bad_categ',
  'hotStreak':'good_categ',
  'champion_levels':'good',
  'champion_points':'good',
  'tokens':'good_categ',
  'ranking_favorite_list':'bad',
  'avg_champion_levels':'good',
  'avg_champion_points':'good',
  'avg_tokens':'good',
  'total_champion_games':'good',
  'win_or_loss':'good',
  'kills':'good',
  'deats':'bad',
  'assists':'good',
  'total_damage':'good',
  'damage_to_champ':'good',
  'damage_to_objects':'good',
  'champ_level':'good',
  'gold_earned':'good',
  'vision_score':'good',
  'minionskilled':'good',
  'neutral_minions_killed':'good',
  'wards_placed':'good',
  'wards_killed':'good',
  'damage_taken':'good'}



feature_relations2 =  {'good': ['summonerLevel',
  'wins',
  'champion_levels',
  'champion_points',
  'avg_champion_levels',
  'avg_champion_points',
  'avg_tokens',
  'total_champion_games',
  'win_or_loss',
  'kills',
  'assists',
  'total_damage',
  'damage_to_champ',
  'damage_to_objects',
  'champ_level',
  'gold_earned',
  'vision_score',
  'minionskilled',
  'neutral_minions_killed',
  'wards_placed',
  'wards_killed',
  'damage_taken'],
 'bad': ['losses', 'ranking_favorite_list', 'deats'],
 'good_categ': ['tier', 'veteran', 'hotStreak', 'tokens'],
 'bad_categ': ['rank', 'freshBlood']}



class Config(object):
    import os
    root_path = os.getcwd()
    season = "13"
