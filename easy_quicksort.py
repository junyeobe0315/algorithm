import random
import numpy as np

def pivot(input_arr : list, used_item : list):
    N = len(input_arr)
    P = int(N/2) 
    while (P in used_item):
        P = random.choice(input_arr)
    used_item.append(P)
    left_arr = []
    right_arr = []
    for idx, num in enumerate(input_arr):
        if (num > P):
            right_arr.append(idx)
        elif (num == P):
            pass
        else:
            left_arr.append(idx)
    output_arr = [0 for i in left_arr]
    for idx, num in enumerate(left_arr):
        output_arr[idx] = input_arr[num]
    output_arr.append(P)
    for num in right_arr:
        output_arr.append(input_arr[num])
    return output_arr, used_item

def quick_sort(input_arr : list):    
    correct_arr = [i for i in range(len(input_arr))]
    pivot_time = 0
    used_item = []
    while True:
        input_arr, used_item = pivot(input_arr, used_item)
        pivot_time += 1
        if (input_arr == correct_arr):
            break
    return input_arr, pivot_time

if (__name__ == "__main__"):
    input_arr = [i for i in range(30)]
    random.shuffle(input_arr)
    print("first arr : ", input_arr)
    output_arr, pivot_time = quick_sort(input_arr)
    print("output : ", output_arr)
    print("pivot used : ", pivot_time)
    