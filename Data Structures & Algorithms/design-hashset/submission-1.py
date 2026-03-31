class MyHashSet:

    def __init__(self):
        self.m_set = []

    def add(self, key: int) -> None:
        if key not in self.m_set:
            self.m_set.append(key)

    def remove(self, key: int) -> None:
        if key in self.m_set:
            self.m_set.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.m_set


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)