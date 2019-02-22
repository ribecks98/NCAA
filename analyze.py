import printing

def splitCols(stats):
    cols = []
    for i in range(len(stats[0])):
        cols.append([x[i] for x in stats])
    return cols

def splitTables(stats):
    sched = []
    conc = []
    i = 1
    n = len(stats)
    while i < n and len(stats[i]) and stats[i][0]:
        sched.append(stats[i])
        i = i+1
    i = i+1
    while i < len(stats):
        conc.append(stats[i])
        i = i+1
    return sched, conc

def step1(sched):
    cols = splitCols(sched)
    pf = convertToInt(cols[2])
    pa = convertToInt(cols[3])
    pd = findDiff(pf,pa)
    return formatDiff(pd) 

def convertToInt(aList):
    new = []
    for thing in aList:
        new.append(int(thing))
    return new

def findDiff(pf,pa):
    tpf = sum(pf)
    tpa = sum(pa)
    numGames = float(len(pf))
    return [tpf,tpa,tpf/numGames,tpa/numGames,(tpf-tpa)/numGames]

def formatDiff(pd):
    end = [[],["Total Points For:",str(pd[0])],["Total Points Against:",str(pd[1])],\
    ["Average Points For:",str(pd[2])],["Average Points Against:",str(pd[3])],["Average Point Difference:",str(pd[4])]]
    return end

def step2(sched):
    return formatWinPct(findWinPct(sched))

def findWinPct(sched):
    count = 0
    n = float(len(sched))
    for game in sched:
        if game[1] == "W":
            count = count+1
    return 100*count/n

def formatWinPct(pct):
    end = [[],["Win Percentage:",str(pct)]]
    return end

def doAll(stats):
#   print stats
    sched, conc = splitTables(stats)
#   print sched
    cols = splitCols(sched)
#   print cols[2]
    pf = convertToInt(cols[2])
    pa = convertToInt(cols[3])
    pd = findDiff(pf,pa)
#   printing.printDiff(pd)
    n = len(conc)
    if n < 5:
        stats.extend(step1(sched))
    if 1:#n < 7:
        stats.pop()
        stats.pop()
        stats.extend(step2(sched))
