#fuck day 3. I'm not doing this shit

import re

with open('Day3/input.txt','r') as f:
    data = f.readlines()

regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

total = 0

def contains_digit(s):
    # get a list of all the numbers in our line
    numbers = re.findall('[0-9]+',s)
    linenumber = data.index(s)
    # for every number in our line
    for i in range(len(numbers)):
        # get the location in our string where our number is located
        location = s.find(numbers[i])

        checks = []
        checks.append(location-1)
        for l in range(len(str(location))):
            checks.append(location + l)
        checks.append(location+len(str(location))+1)
        print(location)
        print(checks)

        checking = True
        while checking:
            if linenumber != 0:
                lineabove = [*data[linenumber-1]]
                for c in range(len(checks)):
                    if regex.search(lineabove[c]) == True:
                        total += numbers[i]
                        checking = False
                        break
            
            sameline = [*data[linenumber]]
            for c in range(len(checks)):
                    if regex.search(sameline[c]) == True:
                        total += numbers[i]
                        checking = False
                        break

            if linenumber != len(data):
                linebelow = [*data[linenumber+1]]
                for c in range(len(checks)):
                    if regex.search(linebelow[c]) == True:
                        total += numbers[i]
                        checking = False
                        break
        
            

        # 
    print(total)



contains_digit(data[0])