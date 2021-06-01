from tests.utils import perform_operations
import unittest

class AddAtTailTest(unittest.TestCase):

    def test_add_at_tail_empty_list(self):
        operations = [ "MyLinkedList", "addAtTail", "get"]
        params = [ [], [5], [0] ]
        expected_output = [ [None], [None], [5] ]
        self.assertEqual(perform_operations(operations,params), expected_output)

    def test_add_at_tail_in_a_row(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtTail", "addAtTail", "get", "get" ]
        params = [ [], [5], [3], [45], [0], [2] ]
        expected_output = [[None], [None], [None], [None], [5], [45] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_tail_after_add_at_head(self):
        operations = [ "MyLinkedList", "addAtHead", "addAtTail", "get", "get" ]
        params = [ [], [53], [15], [0], [1]]
        expected_output = [ [None], [None], [None], [53], [15] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_tail_after_get_operation(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "get", "addAtTail", "get" ]
        params = [ [], [0,53], [1,445], [1], [514], [2] ]
        expected_output = [ [None], [None], [None], [445], [None], [514] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_tail_after_add_at_index_0(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "addAtTail", "get" ]
        params = [ [], [0,54], [0,19], [73], [2] ]
        expected_output = [ [None], [None], [None], [None], [73] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_tail_after_add_at_last_index(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "addAtIndex", "addAtTail", "get" ]
        params = [ [], [0,54], [0,19], [2,359], [73], [3] ]
        expected_output = [ [None], [None], [None], [None], [None], [73] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_tail_after_add_at_middle_index(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "addAtIndex", "addAtIndex", "addAtTail", "get" ]
        params = [ [], [0,54], [0,19], [0,359], [1,548], [147], [4] ]
        expected_output = [ [None], [None], [None], [None], [None], [None], [147] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_tail_after_delete_at_index_0(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "deleteAtIndex", "addAtTail", "get"]
        params = [ [], [0,54], [0,458], [0], [212], [1] ]
        expected_output = [ [None], [None], [None], [None], [None], [212] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_tail_after_delete_at_last_index(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "deleteAtIndex", "addAtTail", "get"]
        params = [ [], [0,12], [0,56], [1], [76], [1] ]
        expected_output = [ [None], [None], [None], [None], [None], [76] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_tail_after_delete_at_middle_index(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "addAtIndex", "deleteAtIndex", "addAtTail", "get" ]
        params = [ [], [0,54], [0,359], [1,548], [1], [147], [2] ]
        expected_output = [ [None], [None], [None], [None], [None], [None], [147] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_tail_after_delete_all_elements(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "deleteAtIndex", "deleteAtIndex", "addAtTail", "get" ]
        params = [ [], [0,54], [0,19], [0], [0], [11], [0] ]
        expected_output = [ [None], [None], [None], [None], [None], [None], [11] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

if __name__=="__main__":
    unittest.main()
