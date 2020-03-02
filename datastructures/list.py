class Node:
    def __init__(self, _val):
        self.value = _val
        self.next = None


class NodeList:
    ##initializer takes args object. if List initialized with int it generates a new node for the List
    # with the passed value else if a Node was passed the Node list object mirrors the list the passed Node belongs to.
    def __init__(self,*args):
        if len(args)>0:
            if isinstance(args[0], int):
                self.head = Node(args[0])
                if self.head.next == None:
                    self.tailNode = None
                    self.head.next=self.tailNode
            elif isinstance(args[0], Node):
                self.head = args[0]
                temp_node = self.head
                while not temp_node == None:
                    temp_node = temp_node.next
                self.tailNode = temp_node
        else:
            self.head = None
            self.tailNode = None
           
    def getHeadNode(self):
        return self.head

    def addNode(self,_node):
        if self.head == None:
            self.head = _node
            self.head.next=self.tailNode
            return
        if not self.tailNode == None:
            temp_node = self.tailNode
            self.tailNode = _node
            temp_node.next = self.tailNode

        else:
            self.tailNode = _node
            self.head.next = self.tailNode
    #prints the current list as an array
    def printNodes(self):
        currentNode = self.head
        node_arry = []
        while not currentNode == None:
            node_arry.append(currentNode.value)
            currentNode = currentNode.next
        print(node_arry)

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

    def sum(self):
        currentNode = self.head
        sum = 0
        while not currentNode == None:
            sum = sum + currentNode.value
            currentNode = currentNode.next
        return sum
    # deletes all duplicate entries in the array if the array is sorted    
    def deleteDuplicates(self):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if self.head == None:
            return None
        prevNode = self.head
        currentNode = self.head.next
        
        while not currentNode == None:
            nextNode = currentNode.next
            print(str(prevNode.value)+ " "+str(currentNode.value))
            
            if prevNode.value == currentNode.value:
                prevNode.next = nextNode
                currentNode = currentNode.next
                
            else:
                prevNode = prevNode.next
                currentNode = currentNode.next
                
                
            
        return NodeList(self.head)
    


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
    third_list = NodeList()
    while not l1_head == None or not l2_head == None:
        
        if not l1_head == None and not l2_head == None:
            if l1_head.value < l2_head.value:
                #print(l1_head.value)
                third_list.addNode(Node(l1_head.value))
                l1_head = l1_head.next
                continue
                
            else:
                #print(str(l2_head.value))
                third_list.addNode(Node(l2_head.value))
                l2_head = l2_head.next
                continue
                

        if not l1_head == None:
                #print(l1_head.value)
                third_list.addNode(Node(l1_head.value))
                l1_head = l1_head.next
                
        if not l2_head == None:
                #print(l2_head.value)
                third_list.addNode(Node(l2_head.value))
                l2_head = l2_head.next
    return third_list

l1 = NodeList(0)  
l2 = NodeList(1)
#mergeLists(l1,l2).printNodes()     

l1.addNode(Node(0))
l1.addNode(Node(1))
l1.addNode(Node(1))
l1.deleteDuplicates().printNodes()



