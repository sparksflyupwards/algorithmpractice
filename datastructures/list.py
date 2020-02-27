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

l = NodeList(2)
l.addNode(Node(3))
l.addNode(Node(5))
l.addNode(Node(0))
l.addNode(Node(3))
l.printNodes()