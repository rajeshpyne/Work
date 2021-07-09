from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next: int = None


@dataclass
class LinkedList:
    head: int = None

    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def push_node_head(self, new_data):
        n = Node(new_data)
        n.next = self.head
        self.head = n

    def push_node(self, prev_node, new_data):
        if prev_node is None:
            self.push_node_head(new_data)
        else:
            n = Node(new_data)
            n.next = prev_node.next
            prev_node.next = n

    def insert_last(self, new_data):
        n = Node(new_data)
        if self.head is None:
            self.head = n
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = n

    def delete_node(self,node):
        node.next = node.next.next


if __name__=='__main__':
    llist = LinkedList()
    llist.insert_last(1)

    llist.push_node_head(2)
    llist.insert_last(4)


    llist.push_node(llist.head,9)
    llist.print_list()
    print("deleting")
    llist.delete_node(llist.head)
    llist.print_list()
    # llist.head = Node(1)
    # second = Node(3)
    # third = Node(2)
    #
    # llist.head.next = second
    # second.next = third
    #
    # llist.print_list()
