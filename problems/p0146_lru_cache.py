"""LeetCode 146: LRU Cache."""

from __future__ import annotations


class LRUCache:
    """A fixed-capacity least-recently-used cache."""

    def __init__(self, capacity: int) -> None:
        """Initialize a cache that stores at most ``capacity`` key-value pairs."""
        assert capacity > 0, f"capacity should > 0, {capacity}"
        self._capacity = capacity
        self._cache: dict[int, Node] = {}
        self._doubly_linked_list = DoublyLinkedList()

    def get(self, key: int) -> int:
        """Return ``key``'s value, or ``-1`` when the key is absent."""
        if key not in self._cache:
            return -1

        node = self._cache[key]
        self._doubly_linked_list.remove(node)
        self._doubly_linked_list.append(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """Store ``value`` for ``key``, evicting the least-recently-used key if needed."""
        # if not exist, simply add to cache and append to list tail
        if key not in self._cache:
            node = Node(key, value)
            self._cache[key] = node
            self._doubly_linked_list.append(node)
        else:
            # if exist, update value and remove -> re-add to list tail
            node = self._cache[key]
            node.value = value
            self._doubly_linked_list.remove(node)
            self._doubly_linked_list.append(node)

        # check capacity
        if self._doubly_linked_list.size() > self._capacity:
            first = self._doubly_linked_list.first()
            assert first is not None, f"first node should not be None"

            self._doubly_linked_list.remove(first)
            del self._cache[first.key]


class Node:
    def __init__(
        self, key: int, value: int, left: Node | None = None, right: Node | None = None
    ) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node(key={self.key!r}, value={self.value!r})"


class DoublyLinkedList:
    def __init__(self) -> None:
        self._head = Node(0, 0)
        self._tail = Node(-1, -1)
        self._head.right = self._tail
        self._tail.left = self._head
        self._size = 0

    def remove(self, node: Node) -> None:
        left = node.left
        assert left is not None, f"node left should never be None {node}"
        right = node.right
        assert right is not None, f"node left should never be None {node}"
        left.right = right
        right.left = left
        self._size -= 1

    def append(self, node: Node) -> None:
        left = self._tail.left
        assert left is not None, f"node left should never be None {node}"
        left.right = node
        node.left = left
        node.right = self._tail
        self._tail.left = node
        self._size += 1

    def first(self) -> Node | None:
        right = self._head.right
        if right == self._tail:
            return None
        return right

    def size(self) -> int:
        return self._size

    def __repr__(self) -> str:
        nodes = []
        node = self._head.right
        while node is not self._tail:
            nodes.append(node)
            assert node is not None
            node = node.right
        return str(nodes)


if __name__ == "__main__":
    dlist = DoublyLinkedList()
    assert dlist.first() is None, f"Expect first node is None"
    assert dlist.size() == 0, f"Expect empty list"

    node1 = Node(1, 1)
    dlist.append(node1)
    assert dlist.first() == node1, f"Excpet first node to be {node1}"
    assert dlist.size() == 1, f"Expect list size = 1"

    node2 = Node(2, 2)
    dlist.append(node2)
    assert dlist.first() == node1, f"Excpet first node to be {node1}"
    assert dlist.size() == 2, f"Expect list size = 2"

    dlist.remove(node1)
    dlist.append(node1)
    assert dlist.first() == node2, f"Excpet first node to be {node2}"
    assert dlist.size() == 2, f"Expect list size = 2"

    print("DoublyLinkedList tests passed")

    cache = LRUCache(2)

    # test 1
    assert cache.get(1) == -1, f"Expect get(1) returns -1"

    # test 2
    cache.put(1, 1)
    assert cache.get(1) == 1, f"Expect get(1) returns 1"

    cache.put(2, 2)
    assert cache.get(2) == 2, f"Expect get(2) returns 2"

    cache.put(3, 3)
    assert cache.get(3) == 3, f"Expect get(3) returns 3"
    assert cache.get(1) == -1, f"Expect get(1)  == -1, but get {cache.get(1)}"

    cache.put(1, 1)
    assert cache.get(2) == -1, f"Expect get(2)  == -1, but get {cache.get(1)}"

    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    assert cache.get(1) == 10
    cache.put(3, 30)
    assert cache.get(2) == -1
    assert cache.get(1) == 10
    assert cache.get(3) == 30

    cache = LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    cache.put(1, 11)
    cache.put(3, 30)
    assert cache.get(2) == -1
    assert cache.get(1) == 11

    cache = LRUCache(1)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2

    print("LRUCache get tests passed")
