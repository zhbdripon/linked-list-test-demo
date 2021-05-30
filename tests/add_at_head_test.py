from linked_list import MyLinkedList
from random import randint
from random import seed
import unittest

class AddAtHeadTest(unittest.TestCase):
    def setUp(self):
        self.list = MyLinkedList()

    def populate_list(self,total):
        for i in range(0,total):
            self.list.addAtHead(randint(1,1000))

    def test_add_at_head_empty_list(self):
        for i in range(1,1001):
            self.list.addAtHead(i)
            self.assertEqual(i,self.list.get(0))
            self.list = MyLinkedList()

    def test_add_at_head_in_a_row(self):
        for i in range(1,1001):
            self.list.addAtHead(i)
            self.assertEqual(i,self.list.get(0))

    def test_add_at_head_after_add_at_tail(self):
        for i in range(1,1001):
            self.list.addAtTail(-i)
            self.list.addAtHead(i)
            self.assertEqual(i,self.list.get(0))

    def test_add_at_head_after_get_operation(self):
        self.populate_list(5)
        for i in range(1,1001):
            self.list.get(0)
            self.list.addAtHead(i)
            self.assertEqual(i,self.list.get(0))

    def test_add_at_head_after_add_at_index_0(self):
        for i in range(1,1001):
            self.list.addAtIndex(0,-i)
            self.list.addAtHead(i)
            self.assertEqual(i,self.list.get(0))

    def test_add_at_head_after_add_at__last_index(self):
        last_index = 0
        for i in range(1,1001):
            self.list.addAtIndex(last_index,-i)
            self.list.addAtHead(i)
            self.assertEqual(i,self.list.get(0))
            last_index+=1

    def test_add_at_head_after_add_at_random_index(self):
        self.populate_list(1000)
        for i in range(1,1001):
            self.list.addAtIndex(randint(0,999),randint(0,999))
            self.list.addAtHead(i)
            self.assertEqual(i,self.list.get(0))

    def test_add_at_head_after_delete_at_index_0(self):
        self.populate_list(1000)
        for i in range(1,1001):
            self.list.deleteAtIndex(0)
            self.list.addAtHead(i)
            self.assertEqual(i,self.list.get(0))

    def test_add_at_head_after_delete_at_last_index(self):
        self.populate_list(1000)
        for i in range(1,1001):
            self.list.deleteAtIndex(999)
            self.list.addAtHead(i)
            self.assertEqual(i,self.list.get(0))

    def test_add_at_head_after_delete_at_random_index(self):
        self.populate_list(1000)
        for i in range(1,1001):
            self.list.deleteAtIndex(randint(0,999))
            self.list.addAtHead(i)
            self.assertEqual(i,self.list.get(0))

    def test_add_at_head_after_delete_at_all_elements(self):
        self.populate_list(1000)
        for i in range(0,1001):
            self.list.deleteAtIndex(0)
        for i in range(1,1001):
            self.list.addAtHead(i)
            self.assertEqual(i,self.list.get(0))
            self.list.deleteAtIndex(0)

if __name__=="__main__":
    unittest.main()
