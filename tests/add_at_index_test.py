from tests.utils import perform_operations
import unittest

class AddAtIndexTest(unittest.TestCase):

    def test_add_at_index_0_empty_list(self):
        operations = [ "MyLinkedList", "addAtIndex", "get" ]
        params = [ [] , [0,85], [0] ]
        expected_output = [ [None], [None], [85] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_index_0_list_not_empty(self):
        operations = [ "MyLinkedList", "addAtHead", "addAtHead", "addAtIndex", "get", "get", "get"]
        params = [ [] , [14], [63], [0,85], [0], [1], [2]  ]
        expected_output = [ [None], [None], [None], [None], [85], [63], [14]]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_valid_last_index(self):
        operations = [ "MyLinkedList", "addAtHead", "addAtHead", "addAtIndex", "get", "get", "get"]
        params = [ [] , [14], [63], [2,85], [0], [1], [2]  ]
        expected_output = [ [None], [None], [None], [None], [63], [14], [85]]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_middle_index(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "addAtTail", "addAtIndex", "get", "get", "get", "get" ]
        params = [ [] , [14], [63], [96], [1,85], [0], [1], [2], [3] ]
        expected_output = [ [None], [None], [None], [None], [None], [14], [85], [63], [96] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_invalid_index(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "addAtIndex", "get", "get", "get" ]
        params = [ [] , [14], [63], [4,85], [0], [1], [4] ]
        expected_output = [ [None], [None], [None], [None], [14], [63], [-1] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_index_after_get_operation(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "get", "addAtIndex", "get" ]
        params = [ [] , [14], [63], [1], [2,85], [2] ]
        expected_output = [ [None], [None], [None], [63], [None], [85] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_index_after_delete_operation(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "deleteAtIndex", "addAtIndex", "get", "get" ]
        params = [ [] , [14], [63], [0], [1,85], [0], [1] ]
        expected_output = [ [None], [None], [None], [None], [None], [63], [85] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_index_after_delete_all_elements(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "deleteAtIndex", "deleteAtIndex", "addAtIndex", "get" ]
        params = [ [] , [14], [63], [0], [0], [0,15], [0] ]
        expected_output = [ [None], [None], [None], [None], [None], [None], [15] ]
        self.assertEqual(perform_operations(operations,params), expected_output )
        
if __name__=="__main__":
    unittest.main()