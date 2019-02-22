import re

def stripAllTeams(lines):
    newlines = lines[3269:3975]
    return newlines

def findURLs(lines):
    urls = []
    for i in range(len(lines)):
        if not i%2:
            urls.append(lines[i])
    return urls

def stripCodeAndName(line):
    parts = re.split("value",line)
    filedirs = re.split("/",parts[-1])
    code = filedirs[3]
    name = filedirs[4]
    return code, name
