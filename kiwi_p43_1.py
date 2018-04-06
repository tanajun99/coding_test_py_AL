

def thePouring(capasities, bottles, fromId, toId):
    result_bottle=[0 for i in range(len(bottles))]
    for i in range(len(fromId)):
        if capasities[toId[i]] >= bottles[toId[i]]+bottles[fromId[i]]:
            bottles[toId[i]]=bottles[toId[i]]+bottles[fromId[i]]
            bottles[fromId[i]]=0
        else:
            bottles[toId[i]]=capasities[toId[i]]
            bottles[fromId[i]]=bottles[fromId[i]]-(capasities[toId[i]]-bottles[toId[i]])
    return bottles


if __name__=="__main__":
    capasities = list(map(int, input().strip().split(' ')))
    bottles = list(map(int, input().strip().split(' ')))
    fromId = list(map(int, input().strip().split(' ')))
    toId = list(map(int, input().strip().split(' ')))
    result = thePouring(capasities, bottles, fromId, toId)
    print (" ".join(map(str, result)))
