import urllib
import listParse as l, htmlParse as html, allio, stringParse, teamCodes as codes, findWebExts as exts, printing


def main(startflag=0,code=""):
    if not startflag:
        code = allio.sanitizeInput("Input the CBS team code:")
    team = codes.getWebName(code) 
    link = "https://www.cbssports.com/college-basketball/teams/"+code+"/"+team+"/schedule/"
    f = urllib.urlopen(link)
    myfile = f.read()
    lines = myfile.split("\n")

    l.deleteSpaceLines(lines)
#   printing.printLines(lines)

    if not startflag:
        flag = allio.sanitizeInput("search or strip?")
    else:
        flag = ""
    if flag == "search":
        search = allio.sanitizeInput("Search for what?")
        l.searchLines(lines,search)
        return
    elif flag == "strip":
        lines = exts.stripAllTeams(lines)
        urls = exts.findURLs(lines)
#       printing.printLines(lines)
        strippedLines = []
        for url in urls:
            name, code = exts.stripCodeAndName(url)
            strippedLines.append([name,code])
#       printing.printLists(strippedLines)
        allio.exportData(strippedLines)
        return

    back = l.chopBackwards(lines,"Page-colSecondary")
#   printing.printLines(lines)

    recordLine = lines[l.searchLines(lines,"PageTitle-header")[0] + 4]

    front = l.chopFront(lines,"CellGameDate")
#   printing.printLines(lines)
#   printing.printLines(front[:1300])

    l.chopForwards(front,"cbs-site-data")
#   printing.printLines(front)

    realFront = l.chopFront(front,"application/ld+json")
#   printing.printLines(realFront)
#   printing.printLines(front)

    gamesFront = html.splitGames(front,"application/ld+json")
    gamesFront = gamesFront[:-1]
#   printing.printSplitLines(gamesFront)

    games = html.splitGames(lines,"CellGameDate")
#   printing.printSplitLines(games)

    html.getPlayedGames(games)
#   printing.printSplitLines(games)

    gameAttrs = []
    for game in games:
#       printing.printLines(game)
        attrs = html.getGameAttrs(game)
        if attrs:
            gameAttrs.append(attrs)
#       printing.printLists(game)

    teamname = codes.getTeamName(code)

    frontAttrs = []
    for i in range(len(games)):
        frontAttrs.append(html.getOppName(gamesFront[i],teamname))

    print stringParse.stripSpaces(recordLine), "\n" 
    printing.printGameLine(["Date", "Win?", "PF", "PA", "OT", "Opponent"])

    fullGames = html.compileGames(gameAttrs,frontAttrs)
    printing.printGames(fullGames)

    fullGames.insert(0,["Date","Win?","Points For","Points Against","OT?","Opponent"])

    allio.exportTeam(fullGames,code)

    return fullGames

if __name__ == "__main__":
    import listParse as l, htmlParse as html, allio, stringParse, teamCodes as codes, findWebExts as exts, printing
    main()
