from linked_list import MyLinkedList
from random import randint
import unittest

class AddAtHeadTest(unittest.TestCase):
    def setUp(self):
        self.list = MyLinkedList()

    def populate_list(self,total):
        for i in range(0,total):
            self.list.addAtHead(randint(1,1000))

    def test_add_at_head_empty_list(self):
        self.list.addAtHead(42)
        self.assertEqual(42,self.list.get(0))

    def test_add_at_head_in_a_row(self):
        self.list.addAtHead(42)
        self.list.addAtHead(15)
        self.assertEqual(42,self.list.get(1))
        self.assertEqual(15,self.list.get(0))

    def test_add_at_head_after_add_at_tail(self):
        self.list.addAtTail(85)
        self.list.addAtHead(45)
        self.assertEqual(45,self.list.get(0))

    def test_add_at_head_after_get_operation(self):
        self.populate_list(5)
        self.list.get(0)
        self.list.addAtHead(15)
        self.assertEqual(15,self.list.get(0))

    def test_add_at_head_after_add_at_index_0(self):
        self.list.addAtIndex(0,45)
        self.list.addAtHead(73)
        self.assertEqual(73,self.list.get(0))

    def test_add_at_head_after_add_at_last_index(self):
        self.list.addAtTail(45)
        self.list.addAtIndex(1,19)
        self.list.addAtHead(54)
        self.assertEqual(54,self.list.get(0))


    def test_add_at_head_after_add_at_random_index(self):
        self.populate_list(10)
        self.list.addAtIndex(7,28)
        self.list.addAtHead(82)
        self.assertEqual(82,self.list.get(0))

    def test_add_at_head_after_delete_at_index_0(self):
        self.populate_list(1000)
        self.list.deleteAtIndex(0)
        self.list.addAtHead(37)
        self.assertEqual(37,self.list.get(0))

    def test_add_at_head_after_delete_at_last_index(self):
        self.populate_list(1000)
        self.list.deleteAtIndex(999)
        self.list.addAtHead(13)
        self.assertEqual(13,self.list.get(0))

    def test_add_at_head_after_delete_at_random_index(self):
        self.populate_list(1000)
        self.list.deleteAtIndex(125)
        self.list.addAtHead(45)
        self.assertEqual(45,self.list.get(0))

    def test_add_at_head_after_delete_all_elements(self):
        self.populate_list(1000)
        for i in range(1,1001):
            self.list.deleteAtIndex(0)
        self.list.addAtHead(46)
        self.assertEqual(46,self.list.get(0))

if __name__=="__main__":
    unittest.main()
