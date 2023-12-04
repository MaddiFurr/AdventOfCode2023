# Check for 12 red, 13 green, 14 blue

with open('Day2/input.txt','r') as f:
    data = f.readlines()

redmax = 12
greenmax = 13
bluemax = 14

possgametotal = 0
smallestpossible = 0

def pause():
    input(">>")

for line in data:
    pullred = 0
    pullgreen = 0
    pullblue = 0

    highestred = 0
    highestgreen = 0
    highestblue = 0
    # Separate the game number from the data from each pull
    game = line.strip().split(': ')
    # The item 1 in the Game list contains all the game pulls
    # by splitting it at the semi-colon, we are breaking each pull into a new list
    pulls = game[1].split('; ')
    # take the first item in the game list, remove everything up to the space which removes 'Game: '
    # then we are left with just the number which we can then turn into an integer for use later
    gamenum = int(game[0].strip().split(' ')[1])
    print("Game Number: {}".format(gamenum))
    # this happens for every pull in each game
    possible = True
    for pull in pulls:
        pullred = 0
        pullgreen = 0
        pullblue = 0      

        cubes = pull.strip().split(', ')
        #print("processing: {}".format(cubes))
        for cube in cubes:
            number = int(cube.strip().split(' ')[0])
            color = cube.strip().split(' ')[1]
            #print("Color: {} | Number: {}".format(color,number))
            match color:
                case "blue":
                    pullblue += number
                    #print("Case BLUE")
                    if number > highestblue:
                        print("New Highest Blue: {}, WAS: {}".format(number,highestblue))
                        highestblue = number
                case "green":
                    pullgreen += number
                    #print("Case GREEN")
                    if number > highestgreen:
                        print("New Highest Green: {}, WAS: {}".format(number,highestgreen))
                        highestgreen = number
                case "red":
                    pullred += number
                    #print("Case RED")
                    if number > highestred:
                        print("New Highest Red: {}, WAS: {}".format(number,highestred))
                        highestred = number
            
            if pullblue > bluemax or pullgreen > greenmax or pullred > redmax:
                possible = False
        
    if possible:
        possgametotal += gamenum
    smallestpossible += highestblue * highestgreen * highestred
    #input(":::::")
        
    
print(possgametotal)

print(smallestpossible)
