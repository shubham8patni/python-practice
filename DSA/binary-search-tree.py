class bst:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def traverse_pre(self):
        print(self.data, end=" ")
        if self.left and self.left.data is not None:
            self.left.traverse_pre()
        if self.right and self.right.data is not None:
            self.right.traverse_pre()
    
    def traverse_in(self):
        if self.left and self.left.data is not None:
            self.left.traverse_in()
        print(self.data, end=" ")
        if self.right and self.right.data is not None:
            self.right.traverse_in()

    def traverse_post(self):
        if self.left and self.left.data is not None:
            self.left.traverse_post()
        if self.right and self.right.data is not None:
            self.right.traverse_post()
        print(self.data, end=" ")

    def search_pre(self, data):
        temp = data
        if temp==self.data:
            print("data found")
        elif temp < self.data:
            if self.left:
                self.left.search_pre(temp)
            else:
                print("data not found")
        elif temp > self.data:
            if self.right:
                self.right.search_pre(temp)
            else:
                print("data not found")

    def insert_pre(self, data):
        temp = data
        if temp < self.data:
            if self.left:
                self.left.insert_pre(temp)
            else:
                self.left = bst(temp)
                print(f"{temp} added to the tree")
                return
        elif temp > self.data:
            if self.right:
                self.right.insert_pre(temp)
            else:
                self.right = bst(temp)
                print(f"{temp} added to the tree")
                return

    def delete(self, data):
        temp = data
        other = 0
        if temp < self.data:
            if self.left:
                self.left.delete(temp)
        elif temp > self.data:
            if self.right:
                self.right.delete(temp)
        elif temp == self.data:
            if self.left is None and self.right is None:
                self.data = None
                return
            if self.left is None:
                temp1 = self.right
                self.data = temp1.data
                self.right = None
                return 
            if self.right is None:
                temp1 = self.left
                self.data = temp1.data
                self.left = None 
                return

if __name__ == "__main__":
    bstt = bst(8)
    bstt.left = bst(5)
    bstt.right = bst(10)
    bstt.left.left = bst(3)
    bstt.left.right = bst(7)
    bstt.left.right.left = bst(6)
    bstt.right.left = bst(9)
    bstt.right.right = bst(11)
    
    print("pre order traversal ", bstt.traverse_pre())
    print("in order traversal ", bstt.traverse_in())
    print("post order traversal ", bstt.traverse_post())
    
    bstt.search_pre(1)
    bstt.insert_pre(1)
    bstt.search_pre(1)
    bstt.delete(6)
    bstt.traverse_pre()


    
