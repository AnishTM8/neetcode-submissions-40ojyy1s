class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.next = None
        self.value = value
class MyHashMap:

    def __init__(self):
        self.map = [ListNode(-1,-1) for i in range(10**4)]

    def put(self, key: int, value: int) -> None:
        index = key%len(self.map)
        curr = self.map[index]

        while curr.next:
            if curr.next.key == key:
                curr.next.value = value
            curr = curr.next
        curr.next = ListNode(key,value)

    def get(self, key: int) -> int:
        index = key%len(self.map)
        curr = self.map[index]

        while curr.next:
            if curr.next.key == key:
                return curr.next.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = key%len(self.map)
        curr = self.map[index]

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)