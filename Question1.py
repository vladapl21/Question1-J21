class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode



linkedList = [node(1, 1), node(5, 4), node(6, 7), node(7, -1), node(2, 2), 
node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]


def outputNodes(arr, startPointer):
    print(arr[startPointer].data)
    next = arr[startPointer].nextNode
    while next != -1:
        print(arr[next].data)
        next = arr[next].nextNode

outputNodes(linkedList, 0)


def addNode(linkedList, startPointer, emptyList, input):
    if emptyList == -1:
        return False
    
    linkedList[emptyList].data = input
    for pointers in linkedList:
        if pointers.nextNode == -1:
            pointers.nextNode = emptyList
    linkedList[emptyList].nextNode = -1
    return True


outputNodes(linkedList, 0)
addNode(linkedList, 0, 5, 5)
outputNodes(linkedList, 0)