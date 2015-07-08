"""
LOOPS REVIEW
"""
soldiers = ['infantry', 'archers', 'cavalry', 'siege', 'medic']

for soldier in soldiers:
    if soldier == 'siege':
        print('Siege engineers aren not real frontline soldiers, pfft')
    print(soldier, 'corps')
else:
    print('A fine army you got there!')
    print('Still, all your base are belong to us!')
