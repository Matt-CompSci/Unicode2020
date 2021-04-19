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

# Visa’s new in-app payment system uses a secure key for authentication and generates a related token for transmission to merchants. To speed up processing, a quick validation can be performed on this (key, token) pair to reject fraudulent submissions before backend verification, by using an adjacency check.
# 
# A key and token can be considered adjacent if:
# 
#     they are the same length
#     each letter in the key is adjacent to a unique letter in the token
# 
# Two letters are adjacent if:
# 
#     They are the same letter, or
#     They are lexigraphically adjacent, i.e.
# 
#     J -> I, J -> K
# 
#     (Z -> A is NOT adjacent)
# 
# For example, the strings CAT and SAD are adjacent as C -> D, A -> A and T -> S.
# 
# You can assume both the key and token contain only uppercase letters.
