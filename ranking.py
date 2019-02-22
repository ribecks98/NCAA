import allio

def compilePcts(pcts):
    new = {}
    for key in pcts.keys():
        if pcts[key] in new.keys():
            new[pcts[key]].append(key)
        else:
            new[pcts[key]] = [key]
    return new

def alg1(winpcts):
    onlyPcts = compilePcts(winpcts)
    ranks = ["Rank"]
    codes = ["School"]
    winpct = ["Win Percentage"]
    count = 1
    for key in sorted(onlyPcts.keys(),reverse=True):
        flag = 0
        for team in onlyPcts[key]:
            if not flag:
                flag = 1
                ranks.append(str(count))
            else:
                ranks.append("")
            codes.append(team)
            winpct.append(str(key))
            count = count+1
    allio.writeCols([ranks,codes,winpct],"rank1")
