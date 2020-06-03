class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    def __repr__(self):
        return f'HashTableEntry({repr(self.key)},{repr(self.value)})'


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8





class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.bucket_array = [None for i in range(capacity)]
        self.capacity = capacity
        self.count = 0
       
        



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        print("this is the len of the array", len(self.bucket_array))
        return len(self.bucket_array)
        
        


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        count = 0

       

        print("this is count", self.count)
        print("this is capacity", self.capacity)
            
        return self.count / self.get_num_slots()
        
        

                


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        byte_array = str(key).encode("utf-8")

        for byte in byte_array:
            hash = ((hash * 33) ^ byte) % 0x100000000
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
      
        key_hash = self.djb2(key)
        bucket_index = key_hash % self.capacity

        new_node = HashTableEntry(key, value)
        current_node = self.bucket_array[bucket_index]

        if current_node:
            head_node = None
            while current_node:
                if current_node.key == key:
                    # found existing key, replace value
                    current_node.value = value
                    return
                head_node = current_node
                current_node = current_node.next
            # if we get this far, we didn't find an existing key
            # so just append the new node to the end of the bucket
            head_node.next = new_node
            self.count += 1 
        else:
            self.bucket_array[bucket_index] = new_node
            self.count += 1 
            print("this is the new count:", self.count)
         



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        key_hash = self.djb2(key)
        bucket_index = key_hash % self.capacity

        current_node = self.bucket_array[bucket_index]
        if current_node:
            head_node = None
            while current_node:
                if current_node.key == key:
                    if head_node:
                        head_node.next = current_node.next
                    else:
                        self.bucket_array[bucket_index] = current_node.next
                else:
                    print("key not found")
                head_node = current_node
                current_node = current_node.next
        
      


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        key_hash = self.djb2(key)
        bucket_index = key_hash % self.capacity

        current_node = self.bucket_array[bucket_index]
        if current_node:
            while current_node:
                if current_node.key == key:
                    return current_node.value
                current_node = current_node.next

        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # # Your code here
        #  # create a copy of the old storage
        array_copy = self.bucket_array
            
        self.count = 0
            
        self.capacity = new_capacity

        self.bucket_array = [None] * self.capacity
            
            
        for node_index in range(len(array_copy)):
            if array_copy[node_index] is not None:
                cur = array_copy[node_index]
                while cur.next is not None:
                    self.put(cur.key, cur.value)
                    cur = cur.next 
                self.put(cur.key, cur.value)
                
        print("this is load", self.get_load_factor())      

        return array_copy
    



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")
    ht.get_num_slots()
    ht.get_load_factor()
    

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
