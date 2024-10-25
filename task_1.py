class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse_list(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        mid = self.get_middle(head)
        next_to_mid = mid.next
        mid.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_mid)

        return self.merge(left, right)

    def merge(self, left, right):
        """ Слияние двух половин ОДНОГО списка """
        dummy = Node(0)
        tail = dummy

        while left is not None and right is not None:
            if left.data <= right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left is not None:
            tail.next = left
        else:
            tail.next = right

        return dummy.next

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge_two_sorted_lists(self, list1, list2):
        """ Слияние двух независимых списков """
        dummy = Node(0)
        tail = dummy

        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Если остались элементы в одном из списков, добавляем их
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next

llist = LinkedList()

llist.insert_at_end(5)
llist.insert_at_end(3)
llist.insert_at_end(8)
llist.insert_at_end(1)
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)

# Реверс списка
llist.reverse_list()
print("\nСписок після реверсування:")
llist.print_list()

# Сортування списку
llist.head = llist.merge_sort(llist.head)
print("\nСписок після сортування злиттям:")
llist.print_list()


list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)

merged_head = llist.merge_two_sorted_lists(list1.head, list2.head)
print("\nОб'єднаний відсортований список:")
current = merged_head
while current:
    print(current.data)
    current = current.next
