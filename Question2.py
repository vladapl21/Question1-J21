arrayData = [10,5,6,7,1,12,13,15,21,8]

def linearSearch(n):
    global arrayData
    for x in arrayData:
        if n == x:
            return True
    return False

'''n = int(input("Enter an integer:  "))
if linearSearch(n):
    print("Value found")
else:
    print("Value not found")'''


def bubbleSort():
    temp = 0
    for i in range(len(arrayData)-1):
        for j in range(len(arrayData)-1):
            if arrayData[j] < arrayData[j+1]:
                temp = arrayData[j]
                arrayData[j] = arrayData[j+1]
                arrayData[j+1] = temp

bubbleSort()
print(arrayData)