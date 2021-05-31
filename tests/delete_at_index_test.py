from linked_list import MyLinkedList
from random import randint
import unittest

class DeleteAtIndexTest(unittest.TestCase):
    def setUp(self):
        self.list = MyLinkedList()

    def test_delete_at_index_0_empty_list(self):
        self.assertEqual(-1,self.list.deleteAtIndex(0))

    def test_delete_at_index_0_list_not_empty(self):
        self.list.addAtTail(14)
        self.list.addAtTail(63)
        self.list.addAtTail(35)
        self.list.deleteAtIndex(0)
        self.assertEqual(63,self.list.get(0))
        self.assertEqual(35,self.list.get(1))
        self.assertEqual(-1,self.list.get(2))

    def test_delete_at_last_index(self):
        self.list.addAtTail(14)
        self.list.addAtTail(63)
        self.list.addAtTail(96)
        self.list.deleteAtIndex(2)
        self.assertEqual(14,self.list.get(0))
        self.assertEqual(63,self.list.get(1))       

    def test_delete_at_invalid_index(self):
        self.list.addAtTail(14)
        self.list.addAtTail(63)
        self.list.deleteAtIndex(2)
        self.assertEqual(-1,self.list.deleteAtIndex(2))  

    def test_delete_at_middle_index(self):
        self.list.addAtTail(142)
        self.list.addAtTail(41)
        self.list.addAtTail(916)
        self.list.deleteAtIndex(1)
        self.assertEqual(142,self.list.get(0))
        self.assertEqual(916,self.list.get(1))

    def test_delete_at_index_after_get_operation(self):
        self.list.addAtTail(14)
        self.list.addAtTail(63)
        self.list.get(1)
        self.list.deleteAtIndex(0)
        self.assertEqual(63,self.list.get(0))

    def test_delete_at_index_after_add_to_head(self):
        self.list.addAtHead(14)
        self.list.addAtHead(63)
        self.list.deleteAtIndex(0)
        self.assertEqual(14,self.list.get(0))

    def test_delete_at_index_after_add_to_index(self):
        self.list.addAtHead(14)
        self.list.addAtHead(63)
        self.list.addAtIndex(1,55)
        self.list.deleteAtIndex(0)
        self.assertEqual(55,self.list.get(0))
        

if __name__=="__main__":
    unittest.main()