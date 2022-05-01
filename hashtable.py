"""
Project 6
CSE 331 S21 (Onsay)
Austin Copeland
hashtable.py
"""

import random
from typing import TypeVar, List, Tuple

T = TypeVar("T")
HashNode = TypeVar("HashNode")
HashTable = TypeVar("HashTable")


class HashNode:
    """
    DO NOT EDIT
    """
    __slots__ = ["key", "value", "deleted"]

    def __init__(self, key: str, value: T, deleted: bool = False) -> None:
        self.key = key
        self.value = value
        self.deleted = deleted

    def __str__(self) -> str:
        return f"HashNode({self.key}, {self.value})"

    __repr__ = __str__

    def __eq__(self, other: HashNode) -> bool:
        return self.key == other.key and self.value == other.value

    def __iadd__(self, other: T) -> None:
        self.value += other


class HashTable:
    """
    Hash Table Class
    """
    __slots__ = ['capacity', 'size', 'table', 'prime_index']

    primes = (
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
        89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179,
        181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277,
        281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389,
        397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
        503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617,
        619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739,
        743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
        863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
        997)

    def __init__(self, capacity: int = 8) -> None:
        """
        DO NOT EDIT
        Initializes hash table
        :param capacity: capacity of the hash table
        """
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

        i = 0
        while HashTable.primes[i] <= self.capacity:
            i += 1
        self.prime_index = i - 1

    def __eq__(self, other: HashTable) -> bool:
        """
        DO NOT EDIT
        Equality operator
        :param other: other hash table we are comparing with this one
        :return: bool if equal or not
        """
        if self.capacity != other.capacity or self.size != other.size:
            return False
        for i in range(self.capacity):
            if self.table[i] != other.table[i]:
                return False
        return True

    def __str__(self) -> str:
        """
        DO NOT EDIT
        Represents the table as a string
        :return: string representation of the hash table
        """
        represent = ""
        bin_no = 0
        for item in self.table:
            represent += "[" + str(bin_no) + "]: " + str(item) + '\n'
            bin_no += 1
        return represent

    __repr__ = __str__

    def _hash_1(self, key: str) -> int:
        """
        ---DO NOT EDIT---
        Converts a string x into a bin number for our hash table
        :param key: key to be hashed
        :return: bin number to insert hash item at in our table, None if key is an empty string
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)
        return hashed_value % self.capacity

    def _hash_2(self, key: str) -> int:
        """
        ---DO NOT EDIT---
        Converts a string x into a hash
        :param key: key to be hashed
        :return: a hashed value
        """
        if not key:
            return None
        hashed_value = 0

        for char in key:
            hashed_value = 181 * hashed_value + ord(char)

        prime = HashTable.primes[self.prime_index]

        hashed_value = prime - (hashed_value % prime)
        if hashed_value % 2 == 0:
            hashed_value += 1
        return hashed_value

    ###############################################################################
    #                          Implement the following:                           #
    ###############################################################################

    def __len__(self) -> int:
        """
        Getter for the size (that, is, the number
        of elements) in the HashTable
        Returns: int that is size of hash table
        """
        return self.size

    def __setitem__(self, key: str, value: T) -> None:
        """
        Sets the value with an associated key in the HashTable
        Returns: None
        """
        self._insert(key, value)

    def __getitem__(self, key: str) -> T:
        """
        Looks up the value with an associated key in the HashTable
        Returns: The value with an associated Key
        """
        res = self._get(key)
        if res is None:
            raise KeyError
        return res.value

    def __delitem__(self, key: str) -> None:
        """
        Deletes the value with an associated key in the HashTable
        Returns: None
        """
        node = self._get(key)
        if node is None:
            raise KeyError
        self._delete(node.key)

    def __contains__(self, key: str) -> bool:
        """
        Determines if a node with the key denoted
        by the parameter exists in the table
        Returns: None
        """
        return self._get(key) is not None

    def _hash(self, key: str, inserting: bool = False) -> int:
        """
        Given a key string return an index in the hash table.
        Returns: int that is the bin we hashed into
        """
        # given key return an index to a hash table
        # insert into the next available bin
        idx = self._hash_1(key)
        new_idx = 0
        i = 0

        # insertion case
        if inserting:
            if (self.table[idx] is not None) and (self.table[idx].key == key):
                return idx
            while i < self.capacity:
                new_idx = (self._hash_1(key) + i * self._hash_2(key)) % self.capacity
                if self.table[new_idx] is None or self.table[new_idx].deleted:
                    return new_idx
                i += 1

        # lookup/deletion case
        else:
            if (self.table[idx] is not None) and (self.table[idx].key == key):
                return idx
            while i <= self.capacity:
                new_idx = (self._hash_1(key) + i * self._hash_2(key)) % self.capacity
                if self.table[new_idx] is None or self.table[new_idx].key == key:
                    return new_idx
                i += 1

    def _insert(self, key: str, value: T) -> None:
        """
        Use the key and value parameters to add
        a HashNode to the hash table.
        Returns: None
        """
        idx = self._hash(key, True)
        hashnode = self.table[idx]

        if hashnode is None or hashnode.key != key:
            self.table[idx] = HashNode(key=key, value=value)
            self.size += 1
            # lf = self.size / self.capacity
            if self.capacity <= 2 * self.size:
                self._grow()
        else:
            self.table[idx].value = value

    def _get(self, key: str) -> HashNode:
        """
        Find the HashNode with the given key in the hash table.
        Returns: HashNode with the key we looked up
        """
        idx = self._hash(key)

        if self.table[idx] is not None:
            if self.table[idx].deleted is not True:
                if self.table[idx].key == key:
                    return self.table[idx]

        return None

    def _delete(self, key: str) -> None:
        """
        Removes the HashNode with the given key from the hash table
        Returns: None
        """
        idx = self._hash(key)

        if self.table[idx] is not None:
            if self.table[idx].deleted is not True:
                if self.table[idx].key == key:
                    self.table[idx].key = None
                    self.table[idx].value = None
                    self.table[idx].deleted = True
                    self.size -= 1

    def _grow(self) -> None:
        """
        Double the capacity of the existing hash table.
        Returns: None
        """
        old = self.table
        self.capacity = self.capacity * 2
        self.table = [None] * self.capacity
        for obj in old:
            if obj is not None:
                if not obj.deleted:
                    idx = self._hash(obj.key, True)
                    self.table[idx] = obj

    def update(self, pairs: List[Tuple[str, T]] = []) -> None:
        """
        Updates the hash table using an iterable of key value pairs
        Returns: None
        """
        for i in range(len(pairs)):
            self[pairs[i][0]] = pairs[i][1]

    def keys(self) -> List[str]:
        """
        Makes a list that contains all of the keys in the table
        Returns: List of the keys
        """
        res = []

        for i in range(self.capacity):
            if self.table[i] is not None:
                res.append(self.table[i].key)

        return res

    def values(self) -> List[T]:
        """
        Makes a list that contains all of the values in the table
        Returns: List of the values
        """
        res = []

        for i in range(self.capacity):
            if self.table[i] is not None:
                res.append(self.table[i].value)

        return res

    def items(self) -> List[Tuple[str, T]]:
        """
        Makes a list that contains all of the key value pairs in the table
        Returns: List of Tuples of the form (key, value)
        """
        res = []

        for i in range(self.capacity):
            if self.table[i] is not None:
                res.append((self.table[i].key, self.table[i].value))

        return res

    def clear(self) -> None:
        """
        Should clear the table of HashNodes completely, in essence a reset of the table
        Returns: None
        """
        self.table = [None] * self.capacity
        self.size = 0


class ExecuteOnlyOnce:
    """
    Represents a request handler.
    """

    def __init__(self, max_time) -> None:
        """
        initializes a request handler
        param: max time threshold for a request handler
        """
        self.max_time = max_time
        self.master_ht = HashTable()
        self.time_ht = HashTable()

    def handle_request(self, time: int, request_id: str, client_id: str) -> int:
        """
        Returns the number of times this request
        has been seen already
        params:
        time: the timestamp of a request
        request_id: the request id sent
        client_id: the specific client_id sent
        """
        key = request_id + client_id
        if key not in self.time_ht:
            self.time_ht[key] = time
        time_diff = time - self.time_ht[key]
        if time_diff <= self.max_time:
            if key in self.master_ht:
                self.master_ht[key] += 1
            else:
                self.master_ht[key] = 0
            self.time_ht[key] = time

        return self.master_ht[key]
