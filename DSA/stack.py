class operations():
    def push(self,value, top, size, stack):
        if top == size:
            print("Stack Overflow")
            return 0
        else:
            top += 1
            stack.append(value)
            return (top, stack)
    
    def popp(slef, top, stack):
        if top == -1:
            return ("Stack Underflow")
        else:
            stack.pop()
            top -= 1
        return (top, stack)
    
    def traverse(self, top, stack):
        temp = -1
        if top == -1:
            return ("Stack is empty cannot be traversed!")
        else:
            while temp != top:
                temp += 1
                print(stack[temp])
        return 0


if __name__ == "__main__":
    size = int(input("input size of the stack : "))
    top = -1
    stack = []
    stk = operations()

    result= stk.push(5, top, size, stack)
    top, stack  = result
    result= stk.push(8, top, size, stack)
    top, stack  = result
    result= stk.push(18, top, size, stack)
    top, stack  = result
    result= stk.push(6, top, size, stack)
    top, stack  = result
    result= stk.traverse(top, stack)
    result= stk.popp(top, stack)
    top, stack  = result
    result= stk.traverse(top, stack)
    
    