import random

numberArray = ["" for x in range(10)]
for x in range(10):
    numberArray[x] = random.randint(1, 100)

def InsertionSort(myList):
    lowerBound = 0
    UpperBound = 10

    for index in range(lowerBound+1, UpperBound):
        key = myList[index]
        place = index - 1
        if myList[place] > key:
            while place >= lowerBound and myList[place] > key:
                temp = myList[place + 1]
                myList[place+1] = myList[place]
                myList[place] = temp
                place = place - 1
        myList[place+1] = key
    return (myList)

print("Before")
print(numberArray)
print("After")
print(InsertionSort(numberArray))