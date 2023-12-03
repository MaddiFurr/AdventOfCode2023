from word2number import w2n
with open('Day1/input.txt','r') as f:
    lines = f.readlines()
numbers = []

#print(lines)

matchcase = ["one", "two", "three", "four", "five", "six", "seven", "eight","nine","1","2","3","4","5","6","7","8","9"]
def check_string(string):
    stringnumbs = []
    l = 0
    for l in range(len(string)):

        i = 0
        for i in range(len(matchcase)):

            if(string[l:].startswith(matchcase[i])):
                stringnumbs.append(w2n.word_to_num(matchcase[i]))

        
    return stringnumbs[0], stringnumbs[-1]

for i in range(len(lines)):
    line = lines[i]
    firstnum, lastnum = check_string(line)

    finalnum = str(firstnum)+str(lastnum)

    numbers.append(int(finalnum))
finalnumber = 0

for i in range(len(numbers)):
        finalnumber += int(numbers[i])

print(finalnumber)

def part1codethatisntneededanymore():
    i = 0
    for i in range(len(lines)):

        line = lines[i]
        linechars = [*line]
        firstnum = None
        lastnum = None

        # Count how many numbers exist in the line were checking
        intcount = 0
        j = 0
        for j in range(len(linechars)):

            try:
                int(linechars[j])
                intcount += 1

            except ValueError:
                pass

        print("Line: {} contains {} integers".format(str(i),str(intcount)))

        if intcount >= 1:
            # Find the first number in the list
            j = 0
            isint = False
            while not isint:
                try:
                    int(linechars[j])
                    isint = True

                except ValueError:
                    isint = False
                    j+=1

                if isint:
                    print("Found first integer in line: {}, which is: {}".format(str(i),int(linechars[j])))
                    firstnum = linechars[j]
        if intcount >= 2:    
            # Find the last number in the list
            j = 0
            linechars.reverse()
            isint = False
            while not isint:
                try:
                    int(linechars[j])
                    isint = True

                except ValueError:
                    isint = False
                    j+=1

                if isint:
                    print("Found last integer in line: {}, which is: {}".format(str(i),int(linechars[j])))
                    lastnum = linechars[j]

        if intcount == 0:
            i += 1
        if intcount == 1:
            linenum = firstnum+firstnum
            numbers.append(int(linenum))
        if intcount >= 2:
            linenum = firstnum+lastnum
            numbers.append(int(linenum))
            i += 1

    print(numbers)
    finalnumber = 0

    for i in range(len(numbers)):
        finalnumber += int(numbers[i])

        i += 1

    print("The final number is: {}".format(str(finalnumber)))