from asyncio.windows_events import NULL


class node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAEnd(self,data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node
    
    def deleteIndex(self, position):
        if self.head is None:
            return
        
        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return
        
        counter = 0
        while counter < position:
            if counter == position-1:
                temp.next= temp.next.next
            counter += 1
            temp = temp.next
            if temp.next == None:
                print(f"The index {position} does not exist in the linked list, index out of range!")
                return
          

    def search(self, key):
        temp = self.head
        counter = 0
        while (temp):
            if temp.data == key:
                print("Starting from 0 the index value of the data : ", counter)
                return
            counter += 1
            temp = temp.next
        print("The value does not exixst in the linked list")
    
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data , "\n")
            temp = temp.next

if __name__ == "__main__":
    ll = linked_list()
    ll.insertAEnd(5)
    ll.insertAEnd(8)
    ll.insertAtBegin(2)
    ll.printList()
    ll.search(5)
    ll.search(8)
    ll.search(11)
    ll.deleteIndex(3)
    #ll.deleteIndex(1)
    ll.printList()