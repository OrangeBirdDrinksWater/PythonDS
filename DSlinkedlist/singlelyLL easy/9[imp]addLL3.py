class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def reverse_list(self, list):
        prev = None
        curr = list
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def add2(self, first, second):
        first = self.reverse_list(first)
        second = self.reverse_list(second)
        carry = 0
        sum_list = None
        while first or second or carry == 1:
            new_val = carry
            if first:
                new_val += first.data
            if second:
                new_val += second.data
            carry = new_val // 10
            new_val %= 10

            new_node = Node(new_val)
            new_node.next = sum_list
            sum_list = new_node

            if first:
                first = first.next
            if second:
                second = second.next
        self.print_list(sum_list)

    def print_list(self, head):
        while head is not None:
            print(head.data, end=" ")
            head = head.next
        print()


L = LinkedList()
L.head1 = Node(7)
L.head1.next = Node(5)
L.head1.next.next = Node(9)
L.head1.next.next.next = Node(4)
L.head1.next.next.next.next = Node(6)
L.head2 = Node(8)
L.head2.next = Node(4)
print("Sum is:", end=" ")
L.add2(L.head1, L.head2)
