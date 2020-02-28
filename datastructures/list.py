class Node:
    def __init__(self, _val):
        self.value = _val
        self.next = None


class NodeList:
    def __init__(self,val):
        self.head = Node(val)
        self.tailNode = None

        self.head.next=self.tailNode
    def getHeadNode(self):
        return self.head
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
    def reverseList(self):
        prevNode = None
        nextNode = None
        currentNode = self.head

        while not currentNode == None:
            nextNode = currentNode.next
            currentNode.next = prevNode
            prevNode = currentNode
            currentNode = nextNode
        self.head = prevNode
        self.printNodes()
def reverseListOld(list):
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

def mergeLists(l1,l2):
    l1_head= l1.getHeadNode()
    l2_head= l2.getHeadNode()

    while not l1_head == None or not l2_head == None:
        
        if not l1_head == None and not l2_head == None:
            if l1_head.value < l2_head.value:
                print(l1.head.value)
                l1_head = l1_head.next
                continue
            else:
                print(l2.head.value)
                l2_head = l2_head.next
                continue

            if not l1_head == None:
                print(l1_head.value)
                l1_head = l1_head.next
                continue
            if not l2_head == None:
                print(l2_head.value)
                l2_head = l2_head.next
                continue
        
l = NodeList(1)
l.addNode(Node(2))
l.addNode(Node(3))
l.addNode(Node(4))
l.addNode(Node(5))
#l.printNodes()
l2 = NodeList(1)
l2.addNode(Node(3))
l2.addNode(Node(44))

mergeLists(l,l2)