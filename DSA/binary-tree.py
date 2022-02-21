from dataclasses import dataclass


class node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None 
    
    def pre_order(self):
        print(self.data, end=" ")
        if self.prev:
            self.prev.pre_order()
        if self.next:
            self.next.pre_order()

    def in_order(self):
        
        if self.prev:
            self.prev.in_order()
        print(self.data, end=" ")
        if self.next:
            self.next.in_order()

    def post_order(self):
        
        if self.prev:
            self.prev.post_order()
        
        if self.next:
            self.next.post_order()
        print(self.data, end=" ")

if __name__ == '__main__':
    root = node(1)
    root.prev = node(2)
    root.next = node(3)
    root.prev.prev=node(4)
    root.prev.next=node(5)
    root.next.prev=node(6)
    root.next.next=node(7)

    print("Pre-Order Traversal: ")
    root.pre_order()

    print("\n\nIn-Order Traversal: ")
    root.in_order()
    
    print("\n\nPost-Order Traversal: ")
    root.post_order()
    