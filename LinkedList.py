from typing import Any


class Node:
    def __init__(self, value: Any = None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value: Any) -> None:
        if self.head is not None:
            temp: Node = self.head
            self.head = Node(value)
            self.head.next = temp
        else:
            self.head = Node(value)
            self.tail = self.head

    def append(self, value: Any) -> None:
        if self.head is not None:
            loop: Node = self.head
            while loop.next:
                loop = loop.next
            loop.next = Node(value)
            self.tail = loop.next
        else:
            self.head = Node(value)
            self.tail = self.head

    def node(self, at: int) -> Node:
        if at < 0 or at > len(self) - 1:
            raise Exception("Wrong index")
        else:
            count = 0
            loop = self.head
            while loop:
                if count == at:
                    return loop
                count += 1
                loop = loop.next

    def get(self, at: int) -> Any:
        tmp: Node = self.head
        for counter in range(0, at):
            tmp = tmp.next
            counter += 1
        return tmp.value

    def insert(self, value: Any, after: Node) -> None:
        if after.next is None:
            after.next = Node(value)
            self.tail = after.next
            return
        else:
            if after == len(self) - 1:
                self.append(value)
            else:
                temp = after.next
                after.next = Node(value)
                after.next.next = temp

    def pop(self) -> Any:
        temp = self.head
        self.head = self.head.next
        return temp.value

    def remove_last(self) -> Any:
        loop: Node = self.head
        count = 0
        while loop:
            if count == len(self) - 2:
                removed_element: Node = loop.next
                loop.next = None
                self.tail = loop
                return removed_element.value
            loop = loop.next
            count += 1

    def remove(self, after: Node) -> Any:
        if after == self.tail:
            raise Exception("Next Node not exist")
        loop: Node = self.head
        while loop:
            if loop == after:
                if loop.next is self.tail:
                    loop.next = None
                    self.tail = loop
                else:
                    loop.next = loop.next.next
            loop = loop.next

    def __str__(self) -> str:
        loop: Node = self.head
        string: str = ''
        while loop:
            string += str(loop.value)
            if loop.next is not None:
                string += ' -> '
            loop = loop.next
        return string

    def __len__(self):
        count: int = 0
        loop: Node = self.head
        while loop:
            count += 1
            loop = loop.next
        return count
