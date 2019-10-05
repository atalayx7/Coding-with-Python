import re

with open('istiklal.txt', encoding='utf-8') as x:
    firstList = []
    # x=x.readlines()
    for i in x.readlines():
        firstList.append(i.strip().split())
dictList = {}
dictList2 = {'toprak': 0, 'vatan': 0, 'yurt': 0, 'kan': 0}
for i in range(len(firstList)):
    for j in firstList[i]:
        j = re.sub(r'\W+', '', j).lower()
        if 'toprak' in j or 'toprağ' in j:
            dictList2['toprak'] += 1
        elif 'vatan' in j:
            dictList2['vatan'] += 1
        elif 'yurt' in j or 'yurd' in j:
            dictList2['yurt'] += 1
        elif 'kan' in j:
            dictList2['kan'] += 1

        #if not j in dictList:
        #    dictList[j] = 1
        #else:
        #    dictList[j] += 1
# print(dictList)
print(dictList2)
