# Pair-Matching-Puzzle-game

ABC Pairs is a memory game where you need to match pairs of tiles.Playing is very simple - you turn over one tile and then try to find a matching tile, i.e either the corresponding value or the picture.

## Installation
Please see the appropriate guide for your environment of choice:
- [Python 3.x](https://www.python.org/downloads/)

Please make sure, in this code is used Miscellaneous operating system interface functions. So recode to your based OS. Example: you are able to find **os.system('clear')** in this code. This suitable for Linux/macOS systems. If you are a windows user please turn that code into **os.system('cls')** 

## Introduction
- Game Level
	- There are 2 levels in this game. Level 1 which is the easiest level and the other the harder level.
		- Level 1 - you will have 60 seconds to match 6 pairs and 3 different numbers or pictures.
		- Level 2 - Grid will be revealed initially for 8 seconds and then you will have 60 seconds to match 6 pairs and 3 different numbers or pictures.

- Scoring
	- Each time you make a successful match you score 20 points.
	- If you fail to match and you should have been able to (a matching tile was previously shown), you
score (-5 * number of times match tile has been shown). So if a matching tile has been revealed
three times before, you will score -15.
	- At the end of a level, if successful, you score a bonus of the number of seconds remaining.
