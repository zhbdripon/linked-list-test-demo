from tests.utils import perform_operations
import unittest

class AddAtHeadTest(unittest.TestCase):

    def test_add_at_head_empty_list(self):
        operations = [ "MyLinkedList", "addAtHead", "get" ]
        params = [ [] , [42] , [0] ]
        expected_output = [[None], [None], [42]]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_head_in_a_row(self):
        operations = [ "MyLinkedList", "addAtHead", "addAtHead", "get" ]
        params = [ [], [42], [15], [0] ]
        expected_output = [[None], [None], [None], [15]]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_head_after_add_at_tail(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtHead", "get" ]
        params = [ [], [85], [45], [0] ]
        expected_output = [[None], [None], [None], [45]]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_head_after_get_operation(self):
        operations = [ "MyLinkedList", "addAtIndex", "get", "addAtHead", "get" ]
        params = [ [], [0,654], [0],[63], [0] ]
        expected_output = [[None], [None], [654], [None], [63]]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_head_after_add_at_index_0(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtHead", "get" ]
        params = [ [], [ 0, 45], [73], [0]]
        expected_output = [[None], [None], [None], [73]]
        self.assertEqual(perform_operations(operations,params), expected_output )
    
    def test_add_at_head_after_add_at_last_index(self):
        operations = [ "MyLinkedList", "addAtTail", "addAtIndex", "addAtHead", "get" ]
        params = [ [], [45], [1,19], [95], [0] ]
        expected_output = [ [None], [None], [None], [None], [95]]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_head_after_add_at_middle_index(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "addAtIndex", "addAtIndex", "addAtHead", "get" ]
        params = [ [], [0,25], [0,951],[0,28], [1,75], [82], [0] ]
        expected_output = [ [None], [None], [None], [None], [None], [None], [82]]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_head_after_delete_at_index_0(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "addAtIndex", "deleteAtIndex", "addAtHead", "get" ]
        params = [ [], [0,25], [1,951], [0,28], [0],[37], [0] ]
        expected_output = [ [None], [None], [None], [None], [None], [None], [37]]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_head_after_delete_at_last_index(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "addAtIndex", "deleteAtIndex", "addAtHead", "get" ]
        params = [ [], [0,25], [1,951], [0,28], [2],[13], [0] ]
        expected_output = [ [None], [None], [None], [None], [None], [None], [13]]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_head_after_delete_at_middle_index(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "addAtIndex", "deleteAtIndex", "addAtHead", "get", "get"]
        params = [ [], [0,25], [1,951], [0,28], [1],[96], [0] ]
        expected_output = [ [None], [None], [None], [None], [None], [None], [96]]
        self.assertEqual(perform_operations(operations,params), expected_output )

    def test_add_at_head_after_delete_all_elements(self):
        operations = [ "MyLinkedList", "addAtIndex", "addAtIndex", "addAtIndex", "deleteAtIndex", "deleteAtIndex","deleteAtIndex", "addAtHead", "get" ]
        params = [ [], [0,25], [1,951], [0,28], [0], [0], [0], [96], [0] ]
        expected_output = [ [None], [None], [None], [None], [None], [None], [None], [None], [96] ]
        self.assertEqual(perform_operations(operations,params), expected_output )

if __name__=="__main__":
    unittest.main()
