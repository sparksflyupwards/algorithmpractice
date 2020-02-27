class Node:
    def __init__(self, _val):
        self.value = _val
        self.next = None


class NodeList:
    def __init__(self,val):
        self.head = Node(val)
        self.tailNode = None

        self.head.next=self.tailNode
    def addNode(self,_node):
        if not self.tailNode == None:
            temp_node = self.tailNode
            self.tailNode = _node
            temp_node.next = self.tailNode

        else:
            self.tailNode = _node
            self.head.next = self.tailNode

    def printNodes(self):
        currentNode = self.head

        while not currentNode == None:
            print(currentNode.value)
            currentNode = currentNode.next

def reverseList(list):
        tempHead = list.head
        tempList = []
        reversedList = []
        while(not tempHead == None):
            tempList.append(tempHead.value)
            tempHead = tempHead.next
        
        for i in range(len(tempList)):
            reversedList.append(tempList[len(tempList)-1-i])
        reversedLinkedList = NodeList( reversedList.pop(0))
        reversedLinkedList.addNode(Node(reversedList.pop(0)))
        for j in range(len(reversedList)):
            reversedLinkedList.addNode(Node(reversedList[j]))
        reversedLinkedList.printNodes()

l = NodeList(1)
l.addNode(Node(2))
l.addNode(Node(3))
l.addNode(Node(4))
l.addNode(Node(5))
#l.printNodes()

reverseList(l)