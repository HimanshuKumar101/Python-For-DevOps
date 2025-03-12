class Node:
    def __init__(self, data):
        self.data = data
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.head = None


    def traverse(self):
        current = self.head

        while current is not Node:
            print(current.data)
            current = current.nextval



if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    Linked_List = LinkedList()
    Linked_List.head = n1
    Linked_List.head.nextval = n2
    n2.nextval = n3

    n3.nextval = None


Linked_List.traverse()