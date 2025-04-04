# src/utils.py
import time
import numpy as np
import random
import csv
from src.bubble_sort import LinkedList 


def measure_time_and_metrics_array(bubble_sort_function, arr):
    start_time = time.time()
    sorted_array, comparisons, swaps = bubble_sort_function(arr)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, comparisons, swaps

def measure_time_linked_list(bubble_sort_function, linked_list):
    start_time = time.time()
    sorted_list, comparisons, swaps = bubble_sort_function(linked_list)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time, comparisons, swaps

def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

def generate_random_linked_list(size):
    linked_list = LinkedList()
    for _ in range(size):
        linked_list.append(random.randint(0, 10000))
    return linked_list

def save_results(filename, sizes, times, comparisons, swaps):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Size', 'Time (s)', 'Comparisons', 'Swaps'])
        for size, time, comparison, swap in zip(sizes, times, comparisons, swaps):
            writer.writerow([size, time, comparison, swap])
