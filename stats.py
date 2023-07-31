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

    club_titles()


def club_two_stats():
    goals = random.randint(150, 175)
    assists = random.randint(80, 100)
    games_played = random.randint(200, 230)
    ratio_calc = (goals + assists) / games_played
    ratio = round(ratio_calc, 2)

    print(f"""Your stats the last five seasons:
  
Games Played: {games_played} 
Goals Scored: {goals} 
Assists: {assists} 
Total Goal Involvments per 90: {ratio}""")

    club_titles()


def club_three_stats():
    goals = random.randint(200, 250)
    assists = random.randint(130, 150)
    games_played = random.randint(230, 250)
    ratio_calc = (goals + assists) / games_played
    ratio = round(ratio_calc, 2)

    print(f"""Your stats the last five seasons:
  
Games Played: {games_played} 
Goals Scored: {goals} 
Assists: {assists} 
Total Goal Involvments per 90: {ratio}""")

    club_titles()


def club_four_stats():
    goals = random.randint(120, 150)
    assists = random.randint(50, 70)
    games_played = random.randint(170, 190)
    ratio_calc = (goals + assists) / games_played
    ratio = round(ratio_calc, 2)

    print(f"""Your stats the last five seasons:
  
Games Played: {games_played} 
Goals Scored: {goals} 
Assists: {assists} 
Total Goal Involvments per 90: {ratio}""")


def club_titles():
    global total_league_titles
    global total_domestic_cups
    global total_european_cups

    league_titles = random.randint(0, 5)
    domestic_cups = random.randint(0, 5)
    european_cups = random.randint(0, 5)

    print(f"""The trophies you've won over the last five seasons: 
    
{league_titles} League Title(s)
{domestic_cups} Domestic Cup Title(s)
{european_cups} European Cup Title(s)""")