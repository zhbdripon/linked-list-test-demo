from tests.utils import perform_operations
import unittest

class GetTest(unittest.TestCase):

    def test_get_from_empty_list(self):
        operations = [ "MyLinkedList", "get", "get" ]
        params = [ [], [0], [2] ]
        expected_output = [ [None], [-1], [-1] ]
        self.assertEqual(perform_operations(operations,params), expected_output)

    def test_get_from_invalid_index(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "get", "get" ]
        params = [ [], [0,43],[1,765],[2],[-5]]
        expected_output = [ [None], [None], [None], [-1], [-1] ]
        self.assertEqual(perform_operations(operations,params), expected_output)

    def test_get_from_valid_index(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "addAtIndex", "addAtIndex", "get", "get" ]
        params = [ [], [0,43], [1,147], [2,22], [3,423], [2], [0] ]
        expected_output = [ [None], [None], [None], [None], [None], [22], [43]]
        self.assertEqual(perform_operations(operations,params), expected_output)

    def test_get_after_add_at_head(self):
        operations = [ "MyLinkedList", "addAtHead", "addAtHead", "addAtHead", "get", "get" ]
        params = [ [], [52], [21], [14], [0], [2]]
        expected_output = [ [None], [None], [None], [None], [14], [52] ]
        self.assertEqual(perform_operations(operations,params), expected_output)

    def test_get_after_add_at_tail(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "addAtTail", "get", "get"  ]
        params = [ [], [15], [55], [41], [0], [2] ]
        expected_output = [ [None], [None], [None], [None], [15], [41]]
        self.assertEqual(perform_operations(operations,params), expected_output)

    def test_get_after_delete_at_index_0(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "addAtTail", "deleteAtIndex", "get", "get"  ]
        params = [ [], [15], [55], [41], [0], [2], [1]]
        expected_output = [ [None], [None], [None], [None], [None], [-1], [41]]
        self.assertEqual(perform_operations(operations,params), expected_output)

    def test_get_last_index_after_delete_tail(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "addAtTail", "deleteAtIndex", "get", "get"  ]
        params = [ [], [15], [55], [41], [2], [2], [0]]
        expected_output = [ [None], [None], [None], [None], [None], [-1], [15]]
        self.assertEqual(perform_operations(operations,params), expected_output)

if __name__=="__main__":
    unittest.main()