class PriorityQueue:
    def ___init___(self):
           self.items = [] # List of (itme,priority)
    def insert(self,priority,item):
        for i in range(len(self.items)):
            if self.items[i][0] > priority:
                    self.items.insert(i,(priority,item))
                    break
        else:
            self.items.append((priority,item))

    def remove(self):
        try:
            return  self.items.pop(0)[1]
        except IndexError:
            raise RuntimeError('Queue is empty')

pq = PriorityQueue()
m = PriorityQueue.insert(pq,5,"Python")
print(pq.remove())