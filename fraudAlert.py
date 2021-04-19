def PairValidator(key, token):
    if len(key) != len(token):
        return False

    adjacentIndices = []

    for keyChar in key:
        foundAdjacent = False
        for idx, tokenChar in enumerate(token):
            if abs(ord(keyChar) - ord(tokenChar)) <= 1 and not idx in adjacentIndices:
                adjacentIndices.append(idx)
                foundAdjacent = True
                break
        if not foundAdjacent:
            return False
    return True

# Tests
print(PairValidator("CAT", "SAD") == True)
print(PairValidator("FAT", "SAD") == False)
print(PairValidator("CAAD", "CAAD") == True)
print(PairValidator("CAAD", "CABD") == True)
print(PairValidator("CABD", "CAAD") == True)
print(PairValidator("ZAT", "SBA") == False)
print(PairValidator("BCL", "KAD") == True)
