# src/bubble_sort.py

# Bubble Sort para Arrays
def bubble_sort_array(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return arr, comparisons, swaps

# Bubble Sort para Listas Ligadas
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def to_array(self):
        arr = []
        current = self.head
        while current:
            arr.append(current.data)
            current = current.next
        return arr

def bubble_sort_linked_list(linked_list):
    comparisons = 0
    swaps = 0
    if not linked_list.head or not linked_list.head.next:
        return linked_list, comparisons, swaps

    n = linked_list.to_array()  # Converte a lista ligada para array
    sorted_list, comparisons, swaps = bubble_sort_array(n)  # Usa a função bubble_sort_array
    linked_list.head = None
    for data in sorted_list:
        linked_list.append(data)

    return linked_list, comparisons, swaps
