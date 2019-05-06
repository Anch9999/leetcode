from utils.node_helper import DoubleLinkNode


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = DoubleLinkNode(0, 0)
        self.tail = DoubleLinkNode(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def _add(self, node):
        p = self.tail.pre
        self.tail.pre = node
        p.next = node
        node.next = self.tail
        node.pre = p

    def _remove(self, node):
        p = node.pre
        n = node.next
        p.next = n
        n.pre = p

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self._remove(self.dic[key])
        node = DoubleLinkNode(key, value)
        self.dic[key] = node
        self._add(node)
        if len(self.dic) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.dic[node.key]


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))       # return 1
    cache.put(3, 3)           # evicts key 2
    print(cache.get(2))       # returns -1 (not found)
    cache.put(4, 4)           # evicts key 1
    print(cache.get(1))       # returns -1 (not found)
    print(cache.get(3))       # returns 3
    print(cache.get(4))       # returns 4
