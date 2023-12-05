#!/usr/bin/python3
"""
Advent of Code 2023
Day 4
"""
# Constants
INPUT_FILE = "input_4.txt"

# Initializing variables
sum_wins = 0  # first answer
sum_scratchcards = 0  # second answer

currCard = 0
gameCards = []
cardsSum = []

with open(INPUT_FILE, encoding="utf-8") as scratchCardsFile:
    for line in scratchCardsFile:
        gameCards.append(line.strip())

# Initializing number of scratch cards
for i in range(0, len(gameCards)):
    cardsSum.append(1)

for game in gameCards:
    localWins = 0
    addCards = 0
    numbers = game.split(": ")[1]
    winningNumbers = numbers.split(" | ")[0].split()
    playedNumbers = numbers.split(" | ")[1].split()
    winSet = set()
    winners = set()

    # Putting winning numbers in set to reduce lookup complexity
    for n in winningNumbers:
        winSet.add(n)

    for n in playedNumbers:
        if n in winSet:
            # first question
            winners.add(n)
            if localWins == 0:
                localWins = 1
            else:
                localWins *= 2

            # second question
            addCards += 1
            if cardsSum[currCard + addCards]:
                cardsSum[currCard + addCards] += cardsSum[currCard]

    sum_wins += localWins
    currCard += 1

# Summing up all the scratchcards
for n in cardsSum:
    sum_scratchcards += n

print(f"First question: {sum_wins}")
print(f"Second question: {sum_scratchcards}")
