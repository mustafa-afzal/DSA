class HashMap:
    def __init__(self, size=16):
        self.size = size
        self.buckets = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, val):
        # your job: handle collision, update if key exists
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for i, pair in enumerate(bucket): 
            if key == pair[0]:
                bucket[i] = (key, val)
                return
        bucket.append((key, val))

    def get(self, key):
        # your job: return val or -1 if not found
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        bucket_index = self._hash(key)
        bucket = self.buckets[bucket_index]
        newBucket = []
        for i, pair in enumerate(bucket):
            if key != pair[0]:
                newBucket.append((pair[0], pair[1]))
        self.buckets[bucket_index] = newBucket


hm = HashMap(9)
hm.put("name", "mustafa")
print(hm.get("name"))
print(hm.remove("name"))