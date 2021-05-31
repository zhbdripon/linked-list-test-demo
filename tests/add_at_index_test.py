from linked_list import MyLinkedList
from random import randint
import unittest

class AddAtIndexTest(unittest.TestCase):
    def setUp(self):
        self.list = MyLinkedList()

    def test_add_at_index_0_empty_list(self):
        self.list.addAtIndex(0,85)
        self.assertEqual(85,self.list.get(0))

    def test_add_at_index_0_list_not_empty(self):
        self.list.addAtHead(14)
        self.list.addAtHead(63)
        self.list.addAtIndex(0,85)
        self.assertEqual(85,self.list.get(0))
        self.assertEqual(63,self.list.get(1))
        self.assertEqual(14,self.list.get(2))

    def test_add_at_middle_index(self):
        self.list.addAtTail(14)
        self.list.addAtTail(63)
        self.list.addAtTail(96)
        self.list.addAtIndex(1,85)
        self.assertEqual(14,self.list.get(0))
        self.assertEqual(85,self.list.get(1))
        self.assertEqual(63,self.list.get(2))
        self.assertEqual(96,self.list.get(3))

    def test_add_at_invalid_index(self):
        self.list.addAtTail(14)
        self.list.addAtTail(63)
        self.list.addAtIndex(4,85)
        self.assertEqual(14,self.list.get(0))
        self.assertEqual(63,self.list.get(1))
        self.assertEqual(-1,self.list.get(4))

    def test_add_at_index_after_get_operation(self):
        self.list.addAtTail(14)
        self.list.addAtTail(63)
        self.list.get(1)
        self.list.addAtIndex(2,85)
        self.assertEqual(85,self.list.get(2))

    def test_add_at_index_after_delete_operation(self):
        self.list.addAtTail(14)
        self.list.addAtTail(63)
        self.list.deleteAtIndex(0)
        self.list.addAtIndex(1,15)
        self.assertEqual(63,self.list.get(0))
        self.assertEqual(15,self.list.get(1))

    def test_add_at_index_after_delete_all_elements(self):
        self.list.addAtTail(14)
        self.list.addAtTail(63)
        self.list.deleteAtIndex(0)
        self.list.deleteAtIndex(0)
        self.list.addAtIndex(0,15)
        self.assertEqual(15,self.list.get(0))
        

if __name__=="__main__":
    unittest.main()