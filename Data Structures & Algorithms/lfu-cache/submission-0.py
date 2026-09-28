class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_node(self, node):
        prev_node = self.head
        next_node = self.head.next
        prev_node.next = node
        node.prev = prev_node
        node.next = next_node
        next_node.prev = node
        self.size += 1

    def remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1

    def pop_tail(self):
        if self.size > 0:
            node = self.tail.prev
            self.remove_node(node)
            return node
        return None

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.keyTable = {}
        self.freqTable = {}

    def _update_freq(self, node):
        freq = node.freq
        self.freqTable[freq].remove_node(node)
        
        if freq == self.minFreq and self.freqTable[freq].size == 0:
            self.minFreq += 1
            
        node.freq += 1
        if node.freq not in self.freqTable:
            self.freqTable[node.freq] = DoublyLinkedList()
        self.freqTable[node.freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.keyTable:
            return -1
        node = self.keyTable[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        
        if key in self.keyTable:
            node = self.keyTable[key]
            node.val = value
            self._update_freq(node)
            return
        
        if len(self.keyTable) >= self.capacity:
            lfu_list = self.freqTable[self.minFreq]
            to_remove = lfu_list.pop_tail()
            del self.keyTable[to_remove.key]
            
        new_node = Node(key, value)
        self.keyTable[key] = new_node
        self.minFreq = 1
        if 1 not in self.freqTable:
            self.freqTable[1] = DoublyLinkedList()
        self.freqTable[1].add_node(new_node)
