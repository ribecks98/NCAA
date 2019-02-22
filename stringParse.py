def isSpaceLine(line):
    realline = line[:-1]
    for thing in realline:
        if thing != " ":
            return 0
    return 1

def stripSpaces(line):
    new = line
    while new[0] == " ":
        new = new[1:]
    return new

def padChar(string,char,num):
    newstr = string
    while len(newstr) < num:
        newstr = newstr + char
    return newstr
