class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        array = self.hashmap[key]
        if (timestamp < array[0][0]):
            return ""
        l, r = 0, len(array) - 1
        mid = 0
        result = ""
        while l <= r:
            mid = (l + r) // 2
            if (array[mid][0] == timestamp):
                result = array[mid][1]
                break
            elif (array[mid][0] < timestamp):
                l = mid + 1
                result = array[mid][1]
            else:
                r = mid - 1
        return result
