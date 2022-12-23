
name_list = ['Aung Aung', 'Mg Mg', 'Thiha', 'Thin Thin', 'Ko Ko', 'Hla Hla']
num = 7

class Queue:
    def _init_(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def enqueue(self,item):
        return self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
q = Queue()
q.enqueue(name_list)
print(q.enqueue())






