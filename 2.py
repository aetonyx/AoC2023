#!/usr/bin/python3

gameCounter = 1 # game counter
validGames = 0
powerGames = 0

# 12 red cubes, 13 green cubes, and 14 blue cubes
red_max = 12
green_max = 13
blue_max = 14

#line = "Game 12: 1 green, 8 red, 5 blue; 6 red, 12 blue; 2 blue, 15 red; 14 blue, 15 red, 1 green; 8 red, 9 blue"

def isGamePossible(gameLine):
    gameDraws = gameLine.strip().split(': ')[1]
    for draw in gameDraws.split('; '):
        cubes = draw.split(", ")
        for color in cubes:
            a = color.split(" ")
            if a[1] == "green" and int(a[0]) > green_max: return False
            if a[1] == "red" and int(a[0]) > red_max: return False
            if a[1] == "blue" and int(a[0]) > blue_max: return False
    return True

def getPowerSet(gameLine):
    bluePower = 1
    greenPower = 1
    redPower = 1
    gameDraws = gameLine.strip().split(': ')[1]
    for draw in gameDraws.split('; '):
        cubes = draw.split(", ")
        for color in cubes:
            a = color.split(" ")
            if a[1] == "green": greenPower = max(greenPower, int(a[0]))
            if a[1] == "blue": bluePower = max(bluePower, int(a[0]))
            if a[1] == "red": redPower = max(redPower, int(a[0]))
    return bluePower * greenPower * redPower

with open("input_2.txt") as gamesFile:
    for game in gamesFile:
        # first part
        if isGamePossible(game):
            validGames += gameCounter
        
        # second part
        powerGames += getPowerSet(game)
        
        #incrementing game counter so I don't need to parse game number for first part
        gameCounter += 1
        
print('Sum of valid games: ' + str(validGames))
print('Sum of power games: ' + str(powerGames))
