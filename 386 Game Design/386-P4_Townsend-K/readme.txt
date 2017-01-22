Kendall's Battle Dice
Kendall Townsend
CPSC 386-01
CWID: 894121409

Game Description:
This is a game based off my project 2. There are some variations because I'm not super familiar with python so I made due with what help I could find online. There were a few people that posted online code to use for general purpose coding. I used the class Buttons from the author Simon H. Larsen where I got from this url: http://www.pygame.org/project-Button+drawer-2541-.html. I used his code to create buttons catered to my game. I also used a simple dice game developed by Ranchi, Jharkhand as a reference for how to setup dices for my RNG involved in my game, and I used his images for the dice I got his code from http://www.pygame.org/project-Pygame+Dice-1287-.html. The game is very simple you have three different moves Attack, Block, and Do nothing. Unlike my game for project 2 I had a hard time finding out how to let the user decide their attack, and calculate the AP accordingly.Each person has three stats the first is AP or action points that is decided by what the dice rolls for them, the second is HP which is their health points pretty self explanatory, and the last is their multiplier which determines how many action points it cost to use block. Most of the textboxes I found didn't work properly with the buttons I was using for one reason or another. So instead of letting the user decide their attack power I just made all attacks have a power of 5, and therefore cost 5 AP. I used the same concept for blocking as I did in project 2 it starts out only costing 1 AP, and each use doubles the cost. I also used the same concept for "doing nothing" which will reset the multiplier on your block.


How To Run:
I used Ubuntu to create this game. In order to compile it in Ubuntu you just need to enter the directory for the folder, and put "python Game.py" into the terminal to compile it.

Files Needed:
Needed for Dice:
1.png
2.png
3.png
4.png
5.png
6.png
Files:
Times_New_Roman_Normal.ttf - needed for font
Game.py - has code for the game
Button.py - has the class for the buttons made by Simon H. Larsen

Features:
1. Has simple AI that randomly generates a number, and determines its move based off of it, and how much AP it has.
2. Has preventative measures for invalid moves.

Features to Add:
1. Menu Screen
2. Better Visuals
3. More complex AI
