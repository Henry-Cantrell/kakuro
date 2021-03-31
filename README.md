# kakuro
## Synopsis:

A simple Python puzzle solver for 3x3 board sizes. Kakuro is a popular Japanese puzzle game that is widely played within the country. 

## What this program does:

This Python program solves 3x3 Kakuro puzzles. It intelligently generates legal boards and also uses an intelligent process to solve its generated boards. Nothing has been hardcoded pertaining to board selection and computer solutions; simple algorithms handle those processes instead. 
 
## Rules of Kakuro:
 
To win a game of Kakuro, there are several conditions that must be met. This program happens to use 3x3 sized boards, so the win conditions and rules for a 3x3 board will be described.
 
Firstly, the two numbers directly below a top number must sum to the top number. 

Then, the two numbers preceding a side number must sum to that side number. 

Once these conditions have been fulfilled for all 4 top numbers and lefthand numbers, the game is legally won.

These conditions create some overlap between the selected player choice numbers. The challenge of the game for the player is accordingly to select numbers that fulfill the win conditions, while not selecting the same numbers for a single sum. So, the same player choice number is actually permitted to be used twice, so long as it has a diagonal relationship (not used in the same sum) to the other player choice numbers.
 
