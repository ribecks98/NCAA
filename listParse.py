import stringParse

def deleteSpaceLines(lines):
    count = len(lines)
    i = 0
    while i < count:
        if stringParse.isSpaceLine(lines[i]):
            lines.pop(i)
            count = count - 1
        else:
            i = i + 1

def searchLines(lines,string):
    inLines = []
    for i in range(len(lines)):
        if string in lines[i]:
            inLines.append(i)
    return inLines

def chopBackwards(lines,string):
    i = -1
    count = len(lines)
    flag = 0
    cut = []
    while i + count >= 0:
        if string in lines[i]:
            i = i + count
            while i < count:
                cut.append(lines.pop(i))
                count = count - 1
            return cut
        else:
            i = i - 1
    return cut

def chopForwards(lines,string):
    i = 0
    count = len(lines)
    flag = 0
    cut = []
    while i < count:
        if flag:
            cut.append(lines.pop(i))
            count = count - 1
        elif string in lines[i]:
            flag = 1
            i = i + 1
        else:
            i = i + 1
    return cut

def chopFrontFromBack(lines,string):
    i = len(lines) - 1
    flag = 0
    cut = []
    while i >= 0:
        if flag:
            cut.append(lines.pop(i))
        elif string in lines[i]:
            flag = 1
        i = i - 1
    cut.reverse()
    return cut

def chopFront(lines,string):
    i = 0
    count = len(lines)
    cut = []
    while i < count:
        if string in lines[i]:
            for j in range(i-1,-1,-1):
                cut.append(lines.pop(j))
            cut.reverse()
            return cut
        i = i + 1


