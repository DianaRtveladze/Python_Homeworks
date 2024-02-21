from Node import Node


class LinkedList:
    def __init__(self, value=None):
        if value is not None:
            self.head = Node(value)
        else:
            self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def remove_last(self):
        if not self.head:
            print("Error: The list is empty. Cannot remove from an empty list.")
            return

        if not self.head.next:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None

linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)

print("Original Linked List:")
current = linked_list.head
while current:
    print(current.value, end=" -> ")
    current = current.next

linked_list.remove_last()

print("\nLinked List after removing the last element:")
current = linked_list.head
while current:
    print(current.value, end=" -> ")
    current = current.next