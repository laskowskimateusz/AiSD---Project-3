from LinkedList import *


class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def peek(self) -> Any:
        return self._storage.head

    def enqueue(self, element: Any) -> Any:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def __len__(self) -> int:
        return len(self._storage)

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1
        if self.current < len(self._storage):
            return self._storage.get(self.current)
        raise StopIteration

    def __str__(self) -> str:
        loop: Node = self._storage.head
        string: str = ''
        while loop:
            string += str(loop.value)
            if loop.next is not None:
                string += ', '
            loop = loop.next
        return string
