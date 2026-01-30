# Ver 1.1.2
# Make sure CSV file only contains the digits and that there are no empyt lines in file. 

import csv
userFile = input("Enter file name(example.csv):\n")

userList = []
with open(userFile,newline='') as userFile:
   for row in csv.reader(userFile):
       userList.append(row[0])

print("\n[Frequency Calculator]\n")

listTotal = len(userList)
print(f'Data set: \n{userList}')


repeat = 'y'
while repeat != 'n':

    lowerLimit = input('\nLower limit: ')
    while lowerLimit.isdigit() == False:
        lowerLimit = input('Lower limit (numerical values only!): ')

    upperLimit = input('Upper Limit: ')
    while upperLimit.isdigit() == False:
        upperLimit = input('Upper limit (numerical values only!): ')

    frequency = 0
    numCheck = 'n'
    numCheck = input("Would you like to see the values?(y/n): ").lower()

    for item in userList:
        if float(item) >= float(lowerLimit) and float(item) <= float(upperLimit):
            frequency += 1
            if numCheck == 'y':
                print(item)

    relativeFre = frequency/listTotal
    roundFre = round(relativeFre, 4)

    print(f'Frequency of items betwen {lowerLimit}-{upperLimit}: {frequency}')
    print(f'Relative frequency (rounded to 4) of items betwen {lowerLimit}-{upperLimit}: {roundFre}')
    repeat = input("\nAgain?(y/n): ").lower()

print("\nProgram stoped")