
class MinHeap:

    def __init__(self) -> None:
        self.items = []
    
    @property
    def size(self) -> int:
        return len(self.items)

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

    def swap(self, a, b):
        temp = self.items[a]
        self.items[a] = self.items[b]
        self.items[b] = temp
    
    def _siftup(self, i):
        parent = MinHeap.parentIndex(i)
        while i != 0 and self.items[i] < self.items[parent]:
            self.items[i], self.items[parent] = self.items[parent], self.items[i]
            i = parent
            parent = MinHeap.parentIndex(i)

    