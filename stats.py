import random

total_league_titles = 0
total_domestic_cups = 0
total_european_cups = 0


def club_one_stats():
    goals = random.randint(65, 85)
    assists = random.randint(30, 50)
    games_played = random.randint(140, 160)
    ratio_calc = (goals + assists) / games_played
    ratio = round(ratio_calc, 2)

    print(f"""Your stats the last five seasons:
  
Games Played: {games_played} 
Goals Scored: {goals} 
Assists: {assists} 
Total Goal Involvments per 90: {ratio}""")


def club_titles():