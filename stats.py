import random

def club_one_stats():
    goals = random.randint(65, 85)
    assists = random.randint(30, 50)
    games_played = random.randint(140, 160)
    ratio_calc = (goals + assists) / games_played
    ratio = round(ratio_calc, 2)