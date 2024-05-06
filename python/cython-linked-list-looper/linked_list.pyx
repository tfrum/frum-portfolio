cdef struct Node:
    int data
    Node* next

cdef class LinkedList:
    cdef Node* head

    def __cinit__(self):
        self.head = NULL

    cdef void append(self, int data):
        cdef Node* new_node = malloc(sizeof(Node))
        new_node.data = data
        new_node.next = NULL

        if self.head is NULL:
            self.head = new_node
        else:
            cdef Node* current = self.head
            while current.next is not NULL:
                current = current.next
            current.next = new_node

    cdef list to_python_list(self):
        cdef list python_list = []
        cdef Node* current = self.head
        while current is not NULL:
            python_list.append(current.data)
            current = current.next
        return python_list

def convert_python_list_to_c_linked_list(python_list):
    cdef LinkedList linked_list = LinkedList()
    for data in python_list:
        linked_list.append(data)
    return linked_list.to_python_list()
