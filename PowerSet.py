def getSubsets(set, index=0):
    allSets = []
    if len(set) == index:
        allSets.append([])
    else:
        allSets = getSubsets(set, index+1)
        item = set[index]
        moreSubsets = []
        for subset in allSets:
            newSubset = []
            newSubset += subset
            newSubset.append(item)
            moreSubsets.append(newSubset)
        allSets += moreSubsets
    return allSets

print(getSubsets([1,2,3]))