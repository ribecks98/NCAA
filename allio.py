import sys, csv, stringParse

def sanitizeInput(header):
    print header
    line = sys.stdin.readline()
    return line[:-1]

def toList(key,value):
    new = [key]
    new.extend(value)
    return new

def exportData(pairs):
    with open("allPairs.csv","w") as writer:
        csvwriter = csv.writer(writer,delimiter=',')
        for pair in pairs.keys():
            csvwriter.writerow(toList(pair,pairs[pair]))

def readData():
    teamCodes = {}
    with open("allPairs.csv","r") as reader:
        csvreader = csv.reader(reader,delimiter=',')
        for line in csvreader:
            teamCodes[line[0]] = line[1:]
    return teamCodes

def exportTeam(games,code):
    with open("stats/"+code+".csv","w") as writer:
        csvwriter = csv.writer(writer,delimiter='|')
        for game in games:
            csvwriter.writerow(game)

def readTeam(code):
    games = []
    with open("stats/"+code+".csv",'r') as reader:
        csvreader = csv.reader(reader,delimiter="|")
        for line in csvreader:
            games.append(line)
    return games

def writeCols(cols,ext):
    with open("rankings/"+ext+".csv",'w') as writer:
        csvwriter = csv.writer(writer,delimiter="|")
        minlen = min([len(col) for col in cols])
        for i in range(minlen):
            row = []
            for thing in cols:
                row.append(thing[i])
            csvwriter.writerow(row)
