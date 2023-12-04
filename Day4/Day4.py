import datetime

start = datetime.datetime.now()
collection = []
print("Started at: {}".format(start))
with open('Day4/input.txt','r') as f:
    data = f.readlines()
    for i in data:
        collection.append(1)


base = 1
total = 0
winningnums = 0
timeswon = 0
for line in data:
    winningnums = 0
    # Separate the card number from the data from each pull
    card = line.strip().split(': ')
    cardnum = int(card[0].strip().split()[1])
    if cardnum == 192:
        break
    batch = card[1].split(' | ')
    winners = batch[0].strip().split()
    ournumbers = batch[1].strip().split()
    print("Total number of card {} left: {}".format(cardnum,collection[cardnum - 1]))
    for i in range(len(ournumbers)):
        if ournumbers[i] in winners:
                #print("card: {} | number: {} is in the list of winners!".format(cardnum,ournumbers[i]))               
            timeswon += 1
            if winningnums == 0:
                winningnums += 1
            else:
                winningnums = winningnums*2
    collection[cardnum - 1] -= 1
    total += winningnums
    winningnums = 0
    looper = timeswon

    while collection[cardnum - 1] > 0:
        timeswon = looper
        while timeswon > 0:
            shifter = 0
            collection[cardnum] += 1
            timeswon -= 1
        collection[cardnum - 1] -= 1

print (total)

print(collection)

print("Started at: {}".format(start))
print("Ended at: {}".format(datetime.datetime.now()))