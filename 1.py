#!/usr/bin/python3
sum_1 = 0   # first answer
sum_2 = 0   # second answer

with open("input_1.txt") as inputFile:
    for line in inputFile:
        
        number_1 = []
        number_2 = []

        p1 = 0
        while p1 < len(line):
            if line[p1].isdigit():
                number_1.append(int(line[p1]))
                number_2.append(int(line[p1]))
            
            else:
                # one, two, six
                if p1 < len(line) - 3:
                    if line[p1:p1 + 3] == "one":
                        number_2.append(1)
                    if line[p1:p1 + 3] == "two":
                        number_2.append(2)
                    if line[p1:p1 + 3] == "six":
                        number_2.append(6)
                
                # four, five, nine
                if p1 < len(line) - 4:
                    if line[p1:p1 + 4] == "four":
                        number_2.append(4)
                    if line[p1:p1 + 4] == "five":
                        number_2.append(5)
                    if line[p1:p1 + 4] == "nine":
                        number_2.append(9)
                
                # three, seven, eight
                if p1 < len(line) - 5:
                    if line[p1:p1 + 5] == "three":
                        number_2.append(3)
                    if line[p1:p1 + 5] == "seven":
                        number_2.append(7)
                    if line[p1:p1 + 5] == "eight":
                        number_2.append(8)
                   
            p1 += 1
        
        sum_1 += number_1[0] * 10 + number_1[-1]
        sum_2 += number_2[0] * 10 + number_2[-1]

print(sum_1)
print(sum_2)
        
        
        