def main(code=""):
    stats = allio.readTeam(code)
    flag = analyze.doAll(stats)
    if flag:
        allio.exportTeam(stats,code)
    return getWinPct(stats)

def getWinPct(stats):
    for line in stats:
        if "Win Percentage:" in line:
            return float(line[1])

def iterate():
    winpcts = {}
    for code in teamCodes.getCodes():
        print code
        print teamCodes.getTeamName(code)
        print ""
        winpcts[teamCodes.getTeamName(code)] = main(code)
    ranking.alg1(winpcts)

if __name__ == "__main__":
    import analyze, getTeamStats as get, teamCodes, allio, ranking
#   main()
    iterate()
