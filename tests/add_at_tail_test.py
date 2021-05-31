from linked_list import MyLinkedList
from random import randint
import unittest

class AddAtTailTest(unittest.TestCase):
    def setUp(self):
        self.list = MyLinkedList()

    def populate_list(self,total):
        for i in range(0,total):
            self.list.addAtHead(randint(1,1000))

    def test_add_at_tail_empty_list(self):
        self.list.addAtTail(5)
        self.assertEqual(5,self.list.get(0))


    def test_add_at_tail_in_a_row(self):
        self.list.addAtTail(5)
        self.list.addAtTail(3)
        self.list.addAtTail(45)
        self.assertEqual(5,self.list.get(0))
        self.assertEqual(45,self.list.get(2))

    def test_add_at_tail_after_add_at_head(self):
        self.list.addAtHead(53)
        self.list.addAtTail(15)
        self.assertEqual(53,self.list.get(0))
        self.assertEqual(15,self.list.get(1))

    def test_add_at_tail_after_get_operation(self):
        self.populate_list(5)
        self.list.get(0)
        self.list.addAtTail(565)
        self.assertEqual(565,self.list.get(5))

    def test_add_at_tail_after_add_at_index_0(self):
        self.list.addAtIndex(0,1000)
        self.list.addAtTail(753)
        self.assertEqual(753,self.list.get(1))

    def test_add_at_tail_after_add_at_last_index(self):
        self.populate_list(5)
        self.list.addAtIndex(5,862)
        self.list.addAtTail(1)
        self.assertEqual(1,self.list.get(6))


    def test_add_at_tail_after_add_at_random_index(self):
        self.populate_list(500)
        self.list.addAtIndex(452,59)
        self.list.addAtTail(25)
        self.assertEqual(25,self.list.get(501))

    def test_add_at_tail_after_delete_at_index_0(self):
        self.list.addAtIndex(0,3)
        self.list.addAtIndex(1,45)
        self.list.deleteAtIndex(0)
        self.list.addAtTail(153)
        self.assertEqual(153,self.list.get(1))

    def test_add_at_tail_after_delete_at_last_index(self):
        self.populate_list(5)
        self.list.deleteAtIndex(5)
        self.list.addAtTail(258)
        self.assertEqual(258,self.list.get(5))

    def test_add_at_tail_after_delete_at_random_index(self):
        self.populate_list(5)
        self.list.deleteAtIndex(2)
        self.list.addAtTail(698)
        self.assertEqual(698,self.list.get(4))

    def test_add_at_tail_after_delete_all_elements(self):
        self.populate_list(3)
        self.list.deleteAtIndex(2)
        self.list.deleteAtIndex(1)
        self.list.deleteAtIndex(0)
        self.list.addAtTail(12)
        self.assertEqual(12,self.list.get(0))

if __name__=="__main__":
    unittest.main()
