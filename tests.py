import unittest
import random
from xml.dom import minidom
from hashtable import HashTable, HashNode, ExecuteOnlyOnce

random.seed(331)


class TestProject1(unittest.TestCase):

    def test_hash(self):
        # (1) Basic with no double hashing
        table1 = HashTable(capacity=16)

        self.assertEqual(4, table1._hash("Ian"))
        self.assertEqual(2, table1._hash("Max"))
        self.assertEqual(5, table1._hash("Yash"))
        self.assertEqual(0, table1._hash("Brandon"))

        # (2) Basic with double hashing - Inserting Mode Only
        table2 = HashTable(capacity=16)

        table2.table = [None, None, None, None, HashNode("Ian", 150, True),
                        None, None, None, HashNode("H", 100),
                        None, None, None, None, None, None, None]

        self.assertEqual(9, table2._hash("Andrew", inserting=True))
        self.assertEqual(5, table2._hash("Andy", inserting=True))
        self.assertEqual(15, table2._hash("Lukas", inserting=True))

        # (3) Larger with Inserting and not Inserting
        table3 = HashTable(capacity=16)

        table3.table = [None, None, None,
                        HashNode('class_ever', 1), HashNode(None, None, True),
                        HashNode(None, None, True), None, None, None,
                        None, HashNode(None, None, True), None,
                        None, None, HashNode('cse331', 100), None]

        # Should insert in the first available bin
        self.assertEqual(4, table3._hash("is_the", inserting=True))

        # Should search until the first None/unused bin
        self.assertEqual(15, table3._hash("is_the"))

        # Should insert in the first available bin
        self.assertEqual(5, table3._hash("yash", inserting=True))

        # Should search until the first None/unused bin
        self.assertEqual(7, table3._hash("yash"))

        self.assertEqual(3, table3._hash("class_ever"))

        # (4) Large Comprehensive
        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i * 10 for i in range(19)]

        table4 = HashTable(capacity=16)

        table4.table = [None, None, HashNode('Max', 0),
                        None, HashNode('Ian', 10),
                        HashNode(None, None, True), None, None, None,
                        None, HashNode(None, None, True), None,
                        None, None, HashNode(None, None, True), None]

        expected = [2, 2, 4, 4, 9, 9, 8, 8, 8, 8, 0, 0, 8, 8, 7, 7, 6, 6, 15, 15, 3, 3, 15, 15, 14, 7, 9, 9, 1, 1, 9,
                    9, 0, 0, 5, 8, 15, 15]

        for i, key in enumerate(keys):
            # inserts every key in inserting mode and normal mode
            self.assertEqual(expected[2 * i], table4._hash(key, inserting=True))
            self.assertEqual(expected[2 * i + 1], table4._hash(key))

    def test_insert(self):
        # This test is just to make sure that the hidden method does the proper amount of work!
        # Insert Sanity Check
        table = HashTable()

        solution = [None, None, None, None, HashNode('is_the', 3005), None, HashNode('cse331', 100), None]

        table._insert('cse331', 100)
        table._insert('is_the', 3005)

        self.assertEqual(solution, table.table)

        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table._insert('best', 42)
        table._insert('class_ever', 1)

        self.assertEqual(4, table.size)
        self.assertEqual(16, table.capacity)
        self.assertEqual(solution, table.table)

    def test_get(self):
        # This test is just to make sure that the hidden method does the proper amount of work!
        # Get Sanity Check
        table = HashTable(capacity=8)

        solution = [None, None, None, None, HashNode('is_the', 3005), None, HashNode('cse331', 100), None]
        table.table = solution  # set the table so insert does not need to work
        table.size = 2

        self.assertEqual(HashNode("is_the", 3005), table._get('is_the'))
        self.assertEqual(HashNode("cse331", 100), table._get('cse331'))
        self.assertIsNone(table._get('cse320'))

    def test_delete(self):
        # This test is just to make sure that the hidden method does the proper amount of work!
        # Delete Sanity Check
        table = HashTable(capacity=16)

        pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                        None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        post_solution = [None, None, None, HashNode('class_ever', 1), HashNode(None, None, True), None, None, None,
                         None, None, HashNode(None, None, True), None, None, None, HashNode('cse331', 100), None]

        table.table = pre_solution  # set the table so insert does not need to work
        table.size = 4

        delete = ['best', 'is_the']
        for k in delete:
            table._delete(k)

        self.assertEqual(post_solution, table.table)
        self.assertEqual(2, table.size)

    def test_len(self):
        # (1) Empty
        table = HashTable()
        self.assertEqual(0, len(table))

        # (2) Size = 1
        table.size = 1
        self.assertEqual(1, len(table))

        # (3) Size = 5
        table.size = 5
        self.assertEqual(5, len(table))

    def test_setitem(self):
        # (1) Simple (No Grow)
        table = HashTable()

        solution = [None, None, None, None, HashNode('is_the', 3005), None, HashNode('cse331', 100), None]

        table["cse331"] = 100
        table["is_the"] = 3005

        self.assertEqual(2, table.size)
        self.assertEqual(8, table.capacity)
        self.assertEqual(solution, table.table)

        # (2) Simple (Grow, builds on 1)
        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table['best'] = 42
        table['class_ever'] = 1

        self.assertEqual(4, table.size)
        self.assertEqual(16, table.capacity)
        self.assertEqual(solution, table.table)

        # (3) Large Comprehensive
        table2 = HashTable()

        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i * 10 for i in range(19)]

        solution = [None, None, None, None, HashNode("Ian", 10), None, None, None, HashNode("H", 30), #8
                    HashNode("Andrew", 20), None, None, None, None, None, None, HashNode("Olivia", 50), None, #17
                    HashNode("Zach", 100), None, None, HashNode("Yash", 170), None, None, HashNode("Lukas", 60), #24
                    HashNode("Scott", 150), None, None, None, None, HashNode("Onsay", 120), None, #31
                    HashNode("Brandon", 160), HashNode("Zosha", 140), None, None, HashNode("Bank", 110), None, None, #38
                    None, None, None, None, None, None, None, None, HashNode("Sarah", 180), None, None, #59
                    HashNode("Anna", 130), None, None, None, HashNode("Angelo", 80), HashNode("Sean", 70), #55
                    HashNode("Andy", 40), None, None, None, None, HashNode("Max", 0), None, HashNode("Jacob", 90)] #63

        for i, key in enumerate(keys):
            table2[key] = vals[i]

        self.assertEqual(19, table2.size)
        self.assertEqual(64, table2.capacity)
        self.assertEqual(solution, table2.table)

    def test_getitem(self):
        # (1) Basic
        table = HashTable(capacity=8)

        solution = [None, None, None, None, HashNode('is_the', 3005), None, HashNode('cse331', 100), None]
        table.table = solution  # set the table so insert does not need to work
        table.size = 2

        self.assertEqual(3005, table["is_the"])
        self.assertEqual(100, table["cse331"])

        # (2) Slightly Larger
        solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                    None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        table.table = solution  # set the table so insert does not need to work
        table.capacity = 16
        table.size = 4

        self.assertEqual(3005, table["is_the"])
        self.assertEqual(100, table["cse331"])
        self.assertEqual(42, table["best"])
        self.assertEqual(1, table["class_ever"])

        # (3) Large Comprehensive
        table2 = HashTable(capacity=64)

        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i * 10 for i in range(19)]

        solution = [None, None, None, None, HashNode("Ian", 10), None, None, None, HashNode("H", 30),
                    HashNode("Andrew", 20), None, None, None, None, None, None, HashNode("Olivia", 50), None,
                    HashNode("Zach", 100), None, None, HashNode("Yash", 170), None, None, HashNode("Lukas", 60),
                    HashNode("Scott", 150), None, None, None, None, HashNode("Onsay", 120), None,
                    HashNode("Brandon", 160), HashNode("Zosha", 140), None, None, HashNode("Bank", 110), None, None,
                    None, None, None, None, None, None, None, None, HashNode("Sarah", 180), None, None,
                    HashNode("Anna", 130), None, None, None, HashNode("Angelo", 80), HashNode("Sean", 70),
                    HashNode("Andy", 40), None, None, None, None, HashNode("Max", 0), None, HashNode("Jacob", 90)]
        table2.table = solution  # set the table so insert does not need to work
        table2.size = 19

        for i, key in enumerate(keys):
            self.assertEqual(vals[i], table2[key])

        # (4) KeyError Check
        with self.assertRaises(KeyError):
            abc = table2["Enbody"]

    def test_delitem(self):
        # (1) Basic
        table = HashTable(capacity=16)

        pre_solution = [None, None, None, HashNode('class_ever', 1), HashNode('is_the', 3005), None, None, None, None,
                        None, HashNode('best', 42), None, None, None, HashNode('cse331', 100), None]

        post_solution = [None, None, None, HashNode('class_ever', 1), HashNode(None, None, True), None, None, None,
                         None, None, HashNode(None, None, True), None, None, None, HashNode('cse331', 100), None]

        table.table = pre_solution  # set the table so insert does not need to work
        table.size = 4

        delete = ['best', 'is_the']
        for k in delete:
            del table[k]

        self.assertEqual(post_solution, table.table)
        self.assertEqual(2, table.size)

        # (2) Large Comprehensive
        table2 = HashTable(capacity=64)

        keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        vals = [i * 10 for i in range(19)]

        pre_solution = [None, None, None, None, HashNode("Ian", 10), None, None, None, HashNode("H", 30),
                        HashNode("Andrew", 20), None, None, None, None, None, None, HashNode("Olivia", 50), None,
                        HashNode("Zach", 100), None, None, HashNode("Yash", 170), None, None, HashNode("Lukas", 60),
                        HashNode("Scott", 150), None, None, None, None, HashNode("Onsay", 120), None,
                        HashNode("Brandon", 160), HashNode("Zosha", 140), None, None, HashNode("Bank", 110), None, None,
                        None, None, None, None, None, None, None, None, HashNode("Sarah", 180), None, None,
                        HashNode("Anna", 130), None, None, None, HashNode("Angelo", 80), HashNode("Sean", 70),
                        HashNode("Andy", 40), None, None, None, None, HashNode("Max", 0), None, HashNode("Jacob", 90)]

        solution = [None, None, None, None, HashNode(None, None), None, None, None, HashNode(None, None),
                    HashNode(None, None), None, None, None, None, None, None, HashNode(None, None), None,
                    HashNode("Zach", 100), None, None, HashNode("Yash", 170), None, None, HashNode(None, None),
                    HashNode("Scott", 150), None, None, None, None, HashNode("Onsay", 120), None,
                    HashNode("Brandon", 160), HashNode("Zosha", 140), None, None, HashNode("Bank", 110), None, None,
                    None, None, None, None, None, None, None, None, HashNode("Sarah", 180), None, None,
                    HashNode("Anna", 130), None, None, None, HashNode(None, None), HashNode(None, None),
                    HashNode(None, None), None, None, None, None, HashNode(None, None), None, HashNode(None, None)]

        table2.table = pre_solution  # set the table so insert does not need to work
        table2.size = 19

        for i, key in enumerate(keys):
            if i < 10:
                del table2[key]

        self.assertEqual(solution, table2.table)
        self.assertEqual(9, table2.size)

        # (3) KeyError Check
        with self.assertRaises(KeyError):
            del table2["Enbody"]
        self.assertEqual(9, table2.size)

    def test_contains(self):
        # (1) Not in Table
        table = HashTable()
        self.assertEqual(False, 'key' in table)

        # (2) In Table
        table.table[5] = HashNode('key', 331)

        self.assertEqual(True, 'key' in table)
        self.assertEqual(False, 'new_key' in table)

    def test_update(self):
        # (1) Not in Table Already
        table = HashTable()

        table.update([("minecraft", 10), ("ghast", 15)])
        self.assertEqual(10, table["minecraft"])
        self.assertEqual(15, table["ghast"])
        self.assertEqual(2, table.size)

        # (2) Update Values in Table
        table.update([("minecraft", 31), ("ghast", 42)])
        self.assertEqual(31, table["minecraft"])
        self.assertEqual(42, table["ghast"])
        self.assertEqual(2, table.size)

        # (3) Update Values in Table and Add New Values
        table.update([("minecraft", 50), ("enderman", 12)])
        self.assertEqual(50, table["minecraft"])
        self.assertEqual(12, table["enderman"])
        self.assertEqual(42, table["ghast"])
        self.assertEqual(3, table.size)

        # (4) Do Nothing
        table.update()
        self.assertEqual(50, table["minecraft"])
        self.assertEqual(12, table["enderman"])
        self.assertEqual(42, table["ghast"])
        self.assertEqual(3, table.size)

    def test_keys_values_items(self):
        # (1) Basic
        table = HashTable()

        initial_keys = ['one', 'two', 'three']
        initial_values = [1, 2, 31]
        initial_items = [('one', 1), ('two', 2), ('three', 31)]

        for i in range(3):
            table[initial_keys[i]] = initial_values[i]

        keys = table.keys()
        values = table.values()
        items = table.items()

        self.assertEqual(set(initial_keys), set(keys))
        self.assertEqual(set(initial_values), set(values))
        self.assertEqual(set(initial_items), set(items))

        # (2) Large
        table2 = HashTable()
        initial_keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach",
                        "Bank", "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        initial_values = [i * 10 for i in range(19)]
        initial_items = []

        for i, key in enumerate(initial_keys):
            table2[key] = initial_values[i]
            initial_items.append((key, initial_values[i]))

        keys = table2.keys()
        values = table2.values()
        items = table2.items()

        self.assertEqual(set(initial_keys), set(keys))
        self.assertEqual(set(initial_values), set(values))
        self.assertEqual(set(initial_items), set(items))

    def test_clear(self):
        # (1) Table with contents
        table = HashTable()

        table['table'] = 1
        table['will'] = 2
        table['be'] = 3
        table['cleared'] = 4

        self.assertEqual(4, table.size)

        table.clear()

        self.assertEqual(0, table.size)
        for node in table.table:
            self.assertIsNone(node)

        # (2) Empty Table
        table.clear()

        self.assertEqual(0, table.size)
        for node in table.table:
            self.assertIsNone(node)

        # (3) Reused Table
        table['one'] = 1

        table.clear()

        self.assertEqual(0, table.size)
        for node in table.table:
            self.assertIsNone(node)

    def test_all(self):
        table = HashTable()

        sol_keys = ["Max", "Ian", "Andrew", "H", "Andy", "Olivia", "Lukas", "Sean", "Angelo", "Jacob", "Zach", "Bank",
                    "Onsay", "Anna", "Zosha", "Scott", "Brandon", "Yash", "Sarah"]
        sol_vals = [i * 100 for i in range(19)]

        solution_a = [None, None, None, None, HashNode("Ian", 100), None, None, None, HashNode("H", 300),
                      HashNode("Andrew", 200), None, None, None, None, None, None, HashNode("Olivia", 500), None,
                      HashNode("Zach", 1000), None, None, HashNode("Yash", 1700), None, None, HashNode("Lukas", 600),
                      HashNode("Scott", 1500), None, None, None, None, HashNode("Onsay", 1200), None,
                      HashNode("Brandon", 1600), HashNode("Zosha", 1400), None, None, HashNode("Bank", 1100), None,
                      None, None, None, None, None, None, None, None, None, HashNode("Sarah", 1800), None, None,
                      HashNode("Anna", 1300), None, None, None, HashNode("Angelo", 800), HashNode("Sean", 700),
                      HashNode("Andy", 400), None, None, None, None, HashNode("Max", 0), None, HashNode("Jacob", 900)]

        solution_b = [None, None, None, None, HashNode(None, None), None, None, None, HashNode(None, None),
                      HashNode(None, None), None, None, None, None, None, None, HashNode(None, None), None,
                      HashNode("Zach", 1000), None, None, HashNode("Yash", 1700), None, None, HashNode(None, None),
                      HashNode("Scott", 1500), None, None, None, None, HashNode("Onsay", 1200), None,
                      HashNode("Brandon", 1600), HashNode("Zosha", 1400), None, None, HashNode("Bank", 1100), None,
                      None, None, None, None, None, None, None, None, None, HashNode("Sarah", 1800), None, None,
                      HashNode("Anna", 1300), None, None, None, HashNode(None, None), HashNode(None, None),
                      HashNode(None, None), None, None, None, None, HashNode(None, None), None, HashNode(None, None)]

        solution_c = [None, None, None, None, HashNode("Ian", 45), None, None, None, HashNode("H", 300),
                      HashNode("Andrew", 200), None, None, None, None, None, None, HashNode("Olivia", 500), None,
                      HashNode("Zach", 1000), None, None, HashNode("Yash", 1700), None, None, HashNode("Lukas", 600),
                      HashNode("Scott", 1500), None, None, None, None, HashNode("Onsay", 1200), None,
                      HashNode("Brandon", 1600), HashNode("Zosha", 1400), None, None, HashNode("Bank", 1100), None,
                      None, None, None, None, None, None, None, None, None, HashNode("Sarah", 1800), None, None,
                      HashNode("Anna", 1300), None, None, None, HashNode("Angelo", 800), HashNode("Sean", 700),
                      HashNode("Andy", 400), None, None, None, None, HashNode("Max", 40), None, HashNode("Jacob", 900)]

        # (1) Insertions/Grow
        sizes = [i + 1 for i in range(19)]
        capacities = [8] * 3 + [16] * 4 + [32] * 8 + [64] * 4
        for i, key in enumerate(sol_keys):
            table[key] = sol_vals[i]
            self.assertEqual(sizes[i], table.size)
            self.assertEqual(capacities[i], table.capacity)

        self.assertEqual(solution_a, table.table)

        # (2) Get
        for i, key in enumerate(sol_keys):
            self.assertEqual(sol_vals[i], table[key])

        with self.assertRaises(KeyError):
            abc = table["Owen"]

        # (3) Delete
        for i, key in enumerate(sol_keys):
            if i < 10:
                del table[key]

        self.assertEqual(solution_b, table.table)
        self.assertEqual(9, table.size)

        with self.assertRaises(KeyError):
            del table["Owen"]
        self.assertEqual(9, table.size)

        # (4) Clear
        table.clear()

        self.assertEqual(0, table.size)
        for node in table.table:
            self.assertIsNone(node)

        table = HashTable()
        for i, key in enumerate(sol_keys):
            table[key] = sol_vals[i]

        # (5) Keys/Vals/Items
        keys = table.keys()
        values = table.values()
        items = table.items()

        self.assertEqual(set(sol_keys), set(keys))
        self.assertEqual(set(sol_vals), set(values))
        self.assertEqual({(sol_keys[i], sol_vals[i]) for i in range(19)}, set(items))

        # (6) Contains
        for i, key in enumerate(sol_keys):
            self.assertEqual(True, key in table)
        self.assertEqual(False, "Ofria" in table)

        # (7) Update
        table.update([("Ian", 45), ("Max", 40)])
        self.assertEqual(solution_c, table.table)

    def test_application(self):
        # (1) Simple
        handler = ExecuteOnlyOnce(max_time=5)
        result1 = handler.handle_request(0, "A", "A")
        self.assertEqual(result1, 0)

        result2 = handler.handle_request(1, "A", "A")
        self.assertEqual(result2, 1)

        result3 = handler.handle_request(2, "A", "A")
        self.assertEqual(result3, 2)

        # (2) Simple, multiple keys
        handler = ExecuteOnlyOnce(max_time=4)
        result1 = handler.handle_request(0, "A", "A")
        self.assertEqual(result1, 0)

        result2 = handler.handle_request(1, "B", "B")
        self.assertEqual(result2, 0)

        result3 = handler.handle_request(2, "A", "A")
        self.assertEqual(result3, 1)

        result4 = handler.handle_request(3, "B", "B")
        self.assertEqual(result4, 1)

        # (3) Check occurred more than max_time ago but still counted
        handler = ExecuteOnlyOnce(max_time=3)
        result1 = handler.handle_request(0, "A", "A")
        self.assertEqual(result1, 0)

        result2 = handler.handle_request(3, "A", "A")
        self.assertEqual(result2, 1)

        result3 = handler.handle_request(6, "A", "A")
        self.assertEqual(result3, 2)

        # (4) Check reset count behavior
        handler = ExecuteOnlyOnce(max_time=6)
        result1 = handler.handle_request(0, "A", "A")
        self.assertEqual(result1, 0)

        result2 = handler.handle_request(1, "B", "B")
        self.assertEqual(result2, 0)

        result3 = handler.handle_request(7, "A", "A")
        self.assertEqual(result3, 0)

        result4 = handler.handle_request(8, "B", "B")
        self.assertEqual(result4, 0)

    def test_application_comprehensive(self):
        # (1) Comprehensive
        handler = ExecuteOnlyOnce(6)
        times = [0, 2, 3, 5, 7, 9, 11, 13, 15, 16, 18, 19, 21, 22, 24, 25, 26, 28, 29, 30, 32, 33, 34, 35, 36]
        request_ids = ['A', 'A', 'C', 'C', 'C', 'C', 'A', 'C', 'B', 'C', 'C', 'A', 'C', 'A', 'A', 'B', 'A', 'A', 'C', 'A', 'B', 'A', 'A', 'A', 'A']
        client_ids = ['A', 'A', 'B', 'C', 'C', 'B', 'B', 'C', 'C', 'A', 'C', 'C', 'B', 'C', 'C', 'C', 'B', 'B', 'C', 'C', 'B', 'A', 'B', 'A', 'A']
        expected = [0, 1, 0, 0, 1, 1, 0, 2, 0, 0, 3, 0, 0, 1, 2, 0, 0, 1, 0, 3, 0, 0, 2, 1, 2]

        for time, request_id, client_id, ans in zip(times, request_ids, client_ids, expected):
            self.assertEqual(handler.handle_request(time, request_id, client_id), ans)

        handler = ExecuteOnlyOnce(10)
        times = [0, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 15, 16, 18, 20, 22, 24, 26, 28, 30, 31, 33, 35, 36, 37, 39, 40, 42, 43, 45, 47, 49, 51, 53, 55, 56, 58, 60, 61, 63, 64, 66, 67, 69, 71, 73, 74, 75, 77, 78]
        request_ids = ['A', 'B', 'C', 'A', 'C', 'C', 'B', 'B', 'C', 'C', 'C', 'B', 'C', 'B', 'B', 'B', 'C', 'B', 'C', 'A', 'B', 'A', 'B', 'B', 'C', 'A', 'B', 'B', 'B', 'A', 'C', 'B', 'A', 'B', 'A', 'B', 'C', 'B', 'B', 'A', 'A', 'A', 'A', 'B', 'B', 'C', 'C', 'B', 'B', 'A']
        client_ids =  ['A', 'A', 'C', 'A', 'C', 'C', 'C', 'A', 'C', 'A', 'A', 'C', 'B', 'C', 'B', 'A', 'C', 'C', 'B', 'A', 'B', 'B', 'A', 'B', 'A', 'A', 'C', 'C', 'B', 'A', 'C', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'C', 'C', 'A', 'B', 'B', 'C', 'A', 'B', 'C', 'A', 'C', 'C']
        expected = [0, 0, 0, 1, 1, 2, 0, 1, 3, 0, 1, 1, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 2, 2, 0, 0, 3, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 2, 0]

        for time, request_id, client_id, ans in zip(times, request_ids, client_ids, expected):
            self.assertEqual(handler.handle_request(time, request_id, client_id), ans)

        handler = ExecuteOnlyOnce(15)
        times = [0, 1, 2, 4, 6, 8, 10, 12, 14, 16, 18, 19, 21, 22, 24, 26, 28, 30, 32, 33, 34, 35, 36, 38, 39, 41, 42, 44, 46, 47, 49, 51, 53, 55, 56, 57, 58, 59, 60, 61, 62, 64, 66, 67, 68, 70, 71, 73, 75, 77, 78, 79, 81, 83, 84, 86, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98, 100, 102, 104, 106, 108, 110, 111, 112, 114]
        request_ids = ['A', 'C', 'B', 'A', 'A', 'C', 'C', 'A', 'B', 'B', 'C', 'C', 'B', 'C', 'C', 'B', 'C', 'A', 'A', 'B', 'A', 'B', 'C', 'A', 'B', 'C', 'C', 'A', 'A', 'B', 'A', 'A', 'C', 'C', 'C', 'B', 'C', 'C', 'C', 'B', 'C', 'C', 'B', 'B', 'B', 'C', 'C', 'A', 'A', 'C', 'C', 'A', 'C', 'B', 'C', 'A', 'A', 'A', 'A', 'C', 'A', 'C', 'C', 'B', 'C', 'B', 'C', 'B', 'C', 'C', 'B', 'C', 'A', 'C', 'B']
        client_ids = ['A', 'C', 'C', 'A', 'C', 'C', 'A', 'A', 'B', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B', 'A', 'A', 'B', 'A', 'B', 'C', 'A', 'B', 'A', 'B', 'B', 'A', 'A', 'B', 'C', 'A', 'B', 'A', 'A', 'B', 'C', 'C', 'B', 'B', 'C', 'A', 'B', 'A', 'C', 'C', 'A', 'B', 'A', 'A', 'B', 'B', 'B', 'A', 'C', 'A', 'C', 'A', 'C', 'B', 'A', 'C', 'B', 'C', 'C', 'C', 'B', 'A', 'A', 'B', 'A', 'B', 'B', 'B']
        expected = [0, 0, 0, 1, 0, 1, 0, 2, 0, 1, 0, 1, 2, 1, 0, 3, 2, 0, 1, 0, 2, 1, 1, 3, 2, 0, 3, 0, 4, 0, 1, 0, 1, 4, 2, 1, 5, 0, 1, 0, 6, 2, 2, 1, 3, 3, 4, 0, 0, 0, 1, 1, 0, 0, 2, 0, 1, 1, 2, 0, 2, 3, 1, 1, 2, 0, 3, 2, 4, 5, 3, 6, 0, 0, 4]

        for time, request_id, client_id, ans in zip(times, request_ids, client_ids, expected):
            self.assertEqual(handler.handle_request(time, request_id, client_id), ans)

    def test_readme_xml_validity(self):

        path = "README.xml"
        xml_doc = minidom.parse(path)
        response = {}
        tags = ["netid", "feedback", "difficulty", "time", "citations", "type", "number"]

        # Assert that we can access all tags
        for tag in tags:
            raw = xml_doc.getElementsByTagName(tag)[0].firstChild.nodeValue
            lines = [s.strip() for s in raw.split("\n")]  # If multiple lines, strip each line
            clean = " ".join(lines).strip()  # Rejoin lines with spaces and strip leading space
            self.assertNotEqual("REPLACE", clean)  # Make sure entry was edited
            response[tag] = clean  # Save each entry

        # Assert that difficulty is a float between 0-10
        difficulty_float = float(response["difficulty"])
        self.assertGreaterEqual(difficulty_float, 0.0)
        self.assertLessEqual(difficulty_float, 10.0)

        # Assert that hours is a float between 0-100 (hopefully it didn't take 100 hours!)
        time_float = float(response["time"])
        self.assertGreaterEqual(time_float, 0.0)
        self.assertLessEqual(time_float, 100.0)

        # Assert assignment type and number was not changed
        self.assertEqual("Project", response["type"])
        self.assertEqual("4", response["number"])

"""
# Comprehensive Test Case Generator
random.seed(331)
def generate_comprehensive(size: int, max_time: int):
    times = [0]
    request_ids = ["A"]
    client_ids = ["A"]
    for _ in range(size - 1):
        times.append(times[-1] + random.randint(1, 2))
        request_ids.append(random.choice(["A", "B", "C"]))
        client_ids.append(random.choice(["A", "B", "C"]))

    handler = ExecuteOnlyOnce(max_time)
    expected = [handler.handle_request(times[i], request_ids[i], client_ids[i]) for i in range(size)]

    print(f'handler = ExecuteOnlyOnce({max_time})')
    print(f'{times = }')
    print(f'{request_ids = }')
    print(f'{client_ids = }')
    print(f'{expected = }\n')

    print(f'for time, request_id, client_id, ans in zip(times, request_ids, client_ids, expected):')
    print('\tself.assertEqual(handler.handle_request(time, request_id, client_id), ans)')

# The following was how the test comprehensive was generated
# generate_comprehensive(25, 6)
# generate_comprehensive(50, 10)
# generate_comprehensive(75, 15)

"""

if __name__ == '__main__':
    unittest.main()
