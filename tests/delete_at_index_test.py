from tests.utils import perform_operations
import unittest

class DeleteAtIndexTest(unittest.TestCase):

    def test_delete_at_index_0_empty_list(self):
        operations = [ "MyLinkedList", "deleteAtIndex", "get" ]
        params = [ [] , [0], [0] ]
        expected_output = [ [None], [None], [-1] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_delete_at_index_0_list_not_empty(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "addAtTail", "deleteAtIndex", "get", "get" ,"get"]
        params = [ [] , [14], [63], [35], [0], [0], [1], [2] ]
        expected_output = [ [None], [None], [None], [None], [None], [63], [35], [-1] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_delete_at_last_index(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "addAtTail", "deleteAtIndex", "get", "get"]
        params = [ [] , [14], [63], [35], [2], [0], [1] ]
        expected_output = [ [None], [None], [None], [None], [None], [14], [63] ]
        self.assertEqual(perform_operations(operations,params), expected_output )       

    def test_delete_at_invalid_index(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "deleteAtIndex", "get" ]
        params = [ [] , [14], [63], [2], [2] ]
        expected_output = [ [None], [None], [None], [None], [-1] ]
        self.assertEqual(perform_operations(operations,params), expected_output )  

    def test_delete_at_middle_index(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "addAtTail", "deleteAtIndex", "get", "get" ]
        params = [ [] , [142], [41], [916], [1], [0], [1] ]
        expected_output = [ [None], [None], [None], [None], [None], [142], [916] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_delete_at_index_after_get_operation(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "get", "deleteAtIndex", "get" ]
        params = [ [] , [14], [63], [1], [0], [0] ]
        expected_output = [ [None], [None], [None], [63], [None], [63] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_delete_at_index_after_add_to_head(self):
        operations = [ "MyLinkedList", "addAtHead", "addAtHead", "deleteAtIndex", "get" ]
        params = [ [] , [14], [63], [0], [0] ]
        expected_output = [ [None], [None], [None], [None], [14] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_delete_at_index_after_add_to_index(self):
        operations = [ "MyLinkedList", "addAtHead", "addAtHead", "addAtIndex", "deleteAtIndex", "get" ]
        params = [ [] , [14], [63], [1,55], [0], [0] ]
        expected_output = [ [None], [None], [None], [None], [None], [55] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

if __name__=="__main__":
    unittest.main()