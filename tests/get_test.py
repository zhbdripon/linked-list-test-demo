from linked_list import MyLinkedList
from random import randint
import unittest

class GetTest(unittest.TestCase):
    def setUp(self):
        self.list = MyLinkedList()

    def populate_list(self,total):
        for i in range(0,total):
            self.list.addAtHead(randint(1,1000))

    def test_get_from_empty_list(self):
        self.assertEqual(-1,self.list.get(0))
        self.assertEqual(-1,self.list.get(2))

    def test_get_from_invalid_index(self):
        self.populate_list(3)
        self.assertEqual(-1,self.list.get(-4))
        self.assertEqual(-1,self.list.get(3))

    def test_get_from_valid_index(self):
        self.list.addAtIndex(0,43)
        self.list.addAtIndex(1,147)
        self.list.addAtIndex(2,22)
        self.list.addAtIndex(3,423)
        self.assertEqual(22,self.list.get(2))
        self.assertEqual(43,self.list.get(0))

    def test_get_after_add_at_head(self):
        self.list.addAtHead(52)
        self.list.addAtHead(21)
        self.list.addAtHead(14)
        self.assertEqual(14,self.list.get(0))
        self.assertEqual(52,self.list.get(2))

    def test_get_after_add_at_tail(self):
        self.list.addAtTail(15)
        self.list.addAtTail(55)
        self.list.addAtTail(41)
        self.assertEqual(15,self.list.get(0))
        self.assertEqual(41,self.list.get(2))

    def test_get_after_delete_at_index_0(self):
        self.list.addAtIndex(0,43)
        self.list.addAtIndex(1,147)
        self.list.addAtIndex(2,22)
        self.list.deleteAtIndex(0)
        self.assertEqual(147,self.list.get(0))

    def test_get_last_index_after_delete_tail(self):
        self.list.addAtIndex(0,43)
        self.list.addAtIndex(1,147)
        self.list.addAtIndex(2,22)
        self.list.deleteAtIndex(2)
        self.assertEqual(-1,self.list.get(2))




if __name__=="__main__":
    unittest.main()