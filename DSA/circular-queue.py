# First in First out
class circular_queue():
    def __init__(self, size) -> None:
        self.size = size
        self.queue = [None] * size
        self.start = self.rear = -1

    def insert_ele(self, data):
        if ((self.rear + 1) % self.size == self.start):
            print("Circular queue is full!")
        elif self.start == -1:
            self.start = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear += 1
            self.queue[self.rear] = data
    
    # First in First out    
    def delete_ele(self):
        if self.start == -1:
            print("Circular queue is empty")
        elif self.start==self.rear:
            temp = self.queue[self.start]
            self.start = self.rear = -1
            return temp
        else:
            temp = self.queue[self.start]
            self.start += 1
            return temp

    def print_cque(self):
        if self.start == -1:
            print("The Circular queue is empty! can't print")
        else:
            for i in range(self.start, self.rear + 1):
                print(self.queue[i]) 

if __name__ == "__main__":
    cque = circular_queue(8)
    cque.insert_ele(6)
    cque.insert_ele(4)
    cque.insert_ele(2)
    cque.insert_ele(9)
    cque.print_cque()
    cque.delete_ele()
    cque.print_cque()