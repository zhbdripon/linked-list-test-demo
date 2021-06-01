from linked_list import MyLinkedList

def perform_operations(actions, params):
    list = None
    output = []
    for action,param in zip(actions, params):
        if action == "MyLinkedList":
            list = MyLinkedList()
            output.append([None])
        elif action == "get":
            output.append([list.get(param[0])])
        elif action == "addAtHead":
            output.append([list.addAtHead(param[0])])
        elif action == "addAtTail":
            output.append([list.addAtTail(param[0])])
        elif action == "addAtIndex":
            output.append([list.addAtIndex(param[0],param[1])])
        elif action == "deleteAtIndex":
            output.append([list.deleteAtIndex(param[0])])
    return output 