# FOOTY FEVER

Footy Fever is a Python terminal game that runs on Heroku.

The live project can be viewed [here]().

Inspiration for this game comes from an existing game called New Star Soccer, which can be downloaded from the App Store and the Google Play Store. In this game you also climb the ranks of football and also take decisions into your own hands.

This game (Footy Fever) was chosen to appeal to its intended target audience, which is football fans of all ages. The game is designed to be a simple and fun game for its target audience. 

### How To Play 

In this game Footy Fever, users will be playing to reach the heights of their footballing career. By starting just out of a youth club and potentially ending up in a whole different continent by the end of the game. Along the way the user will chose clubs that they’ll play for and even take part in salary negotiations. Upon finishing their time at a certain club, they’ll be presented with their stats as a player and all the trophies they’ve won!

* The user can chose the club they want to transfer to once their time with their current club expires. 
* The user can engage in contract negotiations to potentially increase their weekly wages, but risking these negotiations can backfire. 
* The user can chose if they like to sign on to a sponsorship deal. 
* Along the way the user can pick up prestigious footballing awards. 
* The user will be presented with in-game scenarios and they must take control of their actions. 
* By the end of the game the user should have achieved footballing stardom, with incredible personal and team accolades.

## User Experience (UX)

### User Stories

Target Audience: The target audience for this game is anyone that has a keen interest in football and wants to play an online command-line interface fun game. 

As a User I want to:

* play a quick and fun game around an interest of mine
* be able to make decision in a game
* know when i have entered something incorrectly 
* play a game on different devices
* understand how to play the game
* be able to restart the game once finished 
* play a game that is not repetitive if I play it again and again 

### User Experience in this Game

This game will take into consideration the user stories as mentioned above to create a positive UX. The users experience will be shown in deeper detail with examples within the below sections. 


## Libraries & Technologies Used

### Built-in Python Libraries 

* random 

The random library was imported to access the built-in method of generating a random number selection using the randint() method. This was used when it came to displaying the following: Weekly Salary, Transfer Amount, Transfer teams, opponents, awards, Trophies Won, In-Game Scenario Outcomes, Player Stats such as Goals, Assists, Games Played and Ratio. 

* time

The time library was imported to access the built-in method of suspending the execution of the current thread for a given number of seconds using the sleep() method. This was used to give the game some structure in how it’s to be presented to the user. If this method wasn’t used, the user would be thrown a large chunk of text all in one go. Using the sleep() method means that the user can digest the text of the game in smaller parts and not lose track of the flow of the game. 

* os 

The os library was imported to create a function to utilise the os.system to clear the terminal. At the end of the game, if the user decided to play again, the terminal will be cleared and the game will start from the beginning. This function will provide a positive user experience as it will make the new game clearer and more structured. 

### External Python Libraries  

* [Colorama](https://pypi.org/project/colorama/) for adding colour to fonts. 

* [Pyfiglet](https://pypi.org/project/pyfiglet/0.7/) for adding ascii art to the game title. 

### Other 

* [LucidCharts](https://lucid.co/) was used to create the Flowchart.