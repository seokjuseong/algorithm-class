#define Stack class with push, pop, is_impty, and size methods
class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*capacity
        self.top = -1
    def is_empty(self):
        return self.top == -1
    def is_full(self):
        return self.top == self.capacity - 1
    def push(self, item):
        if not self.is_full():
            self.top  += 1
            self.array[self.top] = item
            print(f"PUSH: {item!r} -> stack is now {self.array[:self.top + 1]}")
        else:
            raise OverflowError("Stack Overflow") #pass 
    def pop(self):
        if not self.is_empty():
            item = self.array[self.top]
            self.array[self.top] = None
            self.top -= 1
            print(f"POP: {item!r} -> stack is now {self.array[:self.top + 1]}")
            return item
        else:
            raise IndexError("Stack Underflow!")
    def peek(self):
        if not self.is_empty():
            return self.array[self.top]
        return None
    def size(self):
        return self.top + 1
    
#Test the Stack class 
def reverse_string(statement):
    print("\n[1] PUSH 단계----------------------------------\n")
    st = ArrayStack(statement)
    for index in range(0,statement):
        print(f"{index + 1}번째의 인덱스에 삽입할 아이템을 입력하세요")
        item = input()
        st.push(item)
    print("POP단계-----------------------------------\n")
    out = []
    while not st.is_empty():
        out.append(st.pop())
    result = ''.join(out)
    print(f"최종결과: {result}")
    return result

if __name__ == "__main__":
    print("Stack 의 크기를 입력하세요:   ")
    capacity = int(input())
    reverse_string(capacity)
    