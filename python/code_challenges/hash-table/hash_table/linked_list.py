class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        # if list is empty
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next

            current.next = node

    def includes(self,vlaue):
     current=self.head
     while current :
         if vlaue ==current.data[0]:
            return True
         current=current.next
     return False

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(current.data)
            current = current.next
        return f'{values}'


