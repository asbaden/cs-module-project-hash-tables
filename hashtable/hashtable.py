class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
       

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity 
        self.storage = [None] * capacity
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
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # laod factor is the number of elements, divided by the number of slots in the bucket array 
        load_factor = self.count / self.capacity
        return load_factor 


    def fnv1_64(self, string, seed = 0):
	    #Constants
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037

        #FNV-1a Hash Function
        hash = offset_basis + seed
        for char in string:
            hash = hash * FNV_prime
            hash = hash ^ ord(char)
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1_64(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #
        #something in the slot 
        #this is slot where the passed in value goes in storage 
        index_slot = self.hash_index(key)
        #this is pointing to the where the index of the passed in value will go 
        current_node = self.storage[index_slot]
        
        #creates a node that we will use in the bucket
        new_node = HashTableEntry(key, value)
        
        #if the index is already occupied
        if current_node:
            #establish a head node
            head_node = None
            #create a while loop to traverse the bucket array
            while current_node:
                #at each node, check to see if the occupied element's key matches the passed in key

                if current_node.key == key:
                    # if the key matches, update the value 
                    current_node.value = value
                    return
                # if the key does not match, we change the head node to the current node
                head_node = current_node
                #change the current node to traverse
                current_node = current_node.next
            # there is no key that matches the key being passed in 
            # so add the new node to the end of the bucket 
            head_node.next = new_node
            #increment the counter for load factor calculation
            self.count += 1 
        else:
            #if the current_node is point to none 
            # pass the new node into the bucket 
            self.storage[index_slot] = new_node
            self.count += 1 
    





    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        
        # find the slot where the hashed key is placed 
        index_slot = self.hash_index(key)
        # assign a variable to the node that is occupying that slot (current_node)
        current_node = self.storage[index_slot]
        # create a conditional checking if the node at that slot exists
        if current_node:
            #create a conditional, checking if the first node is equal to the searched key
            if current_node.key == key:
                #if it is, set that index_slot to current_node.next 
                self.storage[index_slot] = current_node.next
                return
            # create a variable for the prev_node 
            prev_node = None 
            # traverse that index with a while loop, looking for the node which has a key that matches the key we are searching for 
            while current_node:
                # if a node's key matches the one we are searching for 
                if current_node.key == key:
                    # set the prev_node.next to the curr.next 
                    prev_node.next = current_node.next
                #else, set prev_node to the current_node, set the current_node to current node.next 
                prev_node = current_node
                current_node = current_node.next 

        # else we have not found the key we are looking to delete, return ("key not found")
        else:
            print("Warning: Key not found")
                


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        # find the index_slot where the searched value is placed
        index_slot = self.hash_index(key)
        #create a variable to point to the contents of the slot
        current_node = self.storage[index_slot]

        
        #with a conditional, check to see if the index slot has a node in it
        if current_node: 
            # if so, traverse the bucket 
            while current_node:
                # check if the node in the bucket has a matching key to the one we are searching for 
                if current_node.key == key:
                    #if so, return that value
                    return current_node.value
                    #if not, move to the next node in the bucket 
                current_node = current_node.next
        #if the index slot has no node, return None
        return None 
        

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        # accounting for the load factor
        #create a copy of the bucket array 
        array_copy = self.storage
        
        # overwrite storage with the new capacity 
        self.capacity = new_capacity
        # update self.storage 
        self.storage = [None] * self.capacity
        
        #take whats in the copied array, and rehash all the elements into the new array 
        for element in range(0, len(array_copy)):
            # check if the element is not none
            if array_copy[element] is not None:
                # if it is not none, assign a variable to the node index
                current_node = array_copy[element]
                #create a while loop to traverse through the bucket
                while current_node.next is not None:
                    # call the put function, passing the node's key and value 
                    self.put(current_node.key, current_node.value)
                    # after each call, traverse the linked list 
                    current_node = current_node.next 
                # once we are outside the loop, call the put funciton, passing the element.key and element.value 
                self.put(current_node.key, current_node.value) 
        # return the array 
        return self.storage



        


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