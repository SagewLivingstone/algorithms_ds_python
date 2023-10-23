
class MinHeap:

    def __init__(self) -> None:
        self.items = []
    
    @property
    def size(self) -> int:
        return len(self.items)

    @classmethod
    def from_array(cls, array):
        heap = cls()
        heap.items = array.copy()
        for i in range(len(heap.items))[::-1]:
            heap._siftdown(i)
        return heap

    @staticmethod
    def leftChildIndex(parentIndex) -> int:
        return (parentIndex * 2) + 1
    @staticmethod
    def rightChildIndex(parentIndex) -> int:
        return (parentIndex * 2) + 2
    @staticmethod
    def parentIndex(childIndex) -> int:
        return (childIndex - 1) // 2

    def hasLeftChild(self, i) -> bool:
        return MinHeap.leftChildIndex(i) < self.size
    def hasRightChild(self, i) -> bool:
        return MinHeap.rightChildIndex(i) < self.size
    def hasParent(self, i) -> bool:
        return MinHeap.parentIndex(i) >= 0

    def leftChild(self, i):
        return self.items[MinHeap.leftChildIndex(i)]
    def rightChild(self, i):
        return self.items[MinHeap.rightChildIndex(i)]
    def parent(self, i):
        return self.items(MinHeap.parentIndex(i))

    def _siftup(self, i):
        parent = MinHeap.parentIndex(i)
        while i > 0 and self.items[i] < self.items[parent]:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent
            parent = MinHeap.parentIndex(i)

    def _siftdown(self, i):
        left = MinHeap.leftChildIndex(i)
        right = MinHeap.rightChildIndex(i)
        while (self.hasLeftChild(i) and self.items[i] > self.leftChild(i)) \
            or (self.hasRightChild(i) and self.items[i] > self.rightChild(i)):
            smallest = left if (not self.hasRightChild(i) or self.leftChild(i) < self.rightChild(i)) else right
            self.items[i], self.items[smallest] = self.items[smallest], self.items[i]
            i = smallest
            left = MinHeap.leftChildIndex(i)
            right = MinHeap.rightChildIndex(i)
    

    def insert(self, element):
        self.items.append(element)
        self._siftup(len(self.items)-1)

    def peek(self):
        return self.items[0] if len(self.items) else None
    
    def pop(self):
        if not len(self.items):
            return None
        
        self.items[0], self.items[-1] = self.items[-1], self.items[0]
        removed = self.items.pop()
        self._siftdown(0)
        return removed
    
    def setByIndex(self, index, value):
        old = self.items[index]
        self.items[index] = value
        if old > value:
            self._siftdown(index)
        else:
            self._siftup(index)
    
    def set(self, old, new):
        if old in self.items:
            self.setByIndex(self.items.index(old), new)
