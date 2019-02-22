codes = {}
names = {}

import allio, printing

def initCodes():
    global codes
    codes = allio.readData()
    initNames()

def initNames():
    global names
    keys = codes.keys()
    schools = [codes[x][1] for x in keys]
    for i in range(len(schools)):
        names[schools[i]] = keys[i]
    sortedSchools = sorted(schools)
    printing.printTwoLists(sortedSchools,[names[x] for x in sortedSchools])

def getCodes():
    return codes.keys()
    
def getNames():
    return names.keys()

def getWebName(code):
    return codes[code][0]

def getTeamName(code):
    return codes[code][1]

def updateCodes(code,name):
    if not code in codes.keys():
        return
    if not codes[code][1]:
        codes[code][1] = name

def destroyCodes():
    allio.exportData(codes)

initCodes()
