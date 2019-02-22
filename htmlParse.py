import stringParse, copy, re

def splitGames(lines,string):
    nextGame = [lines[0]]
    games = []
    i = 1
    count = len(lines)
    while i < count:
        if string in lines[i]:
            games.append(copy.deepcopy(nextGame))
            nextGame = []
        nextGame.append(lines[i])
        i = i + 1
    games.append(nextGame)
    return games

def getPlayedGames(games):
    count = 0
    n = len(games)
    flag = 0
    while count < n:
        if "Buy Tickets" in games[count][-3]:
            count = count+1
            flag = 1
        elif flag:
            games.pop(count)
            n = n-1
        else:
            count = count+1

def invalidGame(game):
    for line in game:
        if "Postponed" in line or "Cancelled" in line or "gametracker/live" in line:
            return 1
    return 0

def findScoreLine(game):
    for line in game:
        if "recap" in line:
            return line
    for line in game:
        if "scoreboard" in line:
            return line

def getGameAttrs(game):
    if invalidGame(game):
        return ""
    attrs = ["",game[1]]
    string = "recap"
    attrs[0] = findScoreLine(game)
    attrs[0] = stringParse.stripSpaces(attrs[0])
    attrs[1] = stringParse.stripSpaces(attrs[1])
    attrs[0] = re.split("</span>",attrs[0])
    attrs.append(re.split(">",attrs[0][0])[-1])
    attrs.append(stringParse.stripSpaces(re.split("<",attrs[0][1])[0]))
    string = attrs[0][0]
    attrs = attrs[1:]
    return attrs

def formatCode(line,code):
    parts = re.split("@",line)
    part1 = re.split("_",parts[0])[-1]
    part2 = re.split("/",parts[1])[0]
    if part1 == code:
        return part2
    else:
        return part1

def getName(line):
    parts = re.split(":",line)
    name = re.split('"',parts[1])[1]
    return name

def getOppName(game,current):
    name1 = getName(game[8])
    name2 = getName(game[12])
    if name1 == current:
        return name2
    else: 
        return name1

def pointSplit(result,score):
    stuff = re.split("/",score)
    scores = re.split("-",stuff[0])
    if len(stuff) > 1:
        ot = "OT"
    else:
        ot = ""
    if result == "W":
        pf = scores[0]
        pa = scores[1]
    else:
        pa = scores[0]
        pf = scores[1]
    return pf, pa, ot

def compileGames(gameAttrs,frontAttrs):
    fullGames = []
    for i in range(len(gameAttrs)):
        pf, pa, ot = pointSplit(gameAttrs[i][1],gameAttrs[i][2])
        allAttrs = [gameAttrs[i][0],gameAttrs[i][1],pf,pa,ot,frontAttrs[i]]
        fullGames.append(allAttrs)
    return fullGames
