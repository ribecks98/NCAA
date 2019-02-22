import stringParse, re

def printLines(lines):
    count = 0
    for thing in lines:
        count = count + 1
        print count, thing

def printSplitLines(sets):
    count = 0
    for i in range(len(sets)):
        print "Set ", i+1
        for thing in sets[i]:
            count = count + 1
            print count, thing
        print ""

def printLists(lists):
    for aList in lists:
        print aList

def printDict(graph):
    for key in graph.keys():
        print key, ": ", graph[key]

def printTwoLists(list1,list2):
    if len(list1) <= len(list2):
        n = len(list1)
    else:
        n = len(list2)
    maxlen = max([len(thing) for thing in list1])
    for i in range(n):
        print stringParse.padChar(list1[i]," ",maxlen), ":", list2[i]

def printGameLine(attrs):
    string = stringParse.padChar(attrs[0]," ",15)
    string = stringParse.padChar(string+attrs[1]," ",21)
    string = stringParse.padChar(string+attrs[2]," ",26)
    string = stringParse.padChar(string+attrs[3]," ",31)
    string = stringParse.padChar(string+attrs[4]," ",35)
    string = stringParse.padChar(string+attrs[5]," ",37)
    print string

def printGames(games):
    for game in games:
        printGameLine(game)
    print ""

def printDiff(pd):
    print "Total Points For: ", str(pd[0])
    print "Total Points Against: ", str(pd[1])
    print "Average Points For: ", str(pd[2])
    print "Average Points Against: ", str(pd[3])
    print "Average Point Difference: ", str(pd[4])
