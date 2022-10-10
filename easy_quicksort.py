import random


def quick_sort(arr:list, i:int):
    if len(arr) <= 1:
        return arr
    pivot = arr[-1]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
        i += 1
    print(i)
    return quick_sort(lesser_arr, i) + equal_arr + quick_sort(greater_arr, i)
    

if (__name__ == "__main__"):
    input_arr = []
    with open("./input_arr.txt") as f:
        lines = f.readlines()
        for line in lines:
            input_arr.append(int(line))
            
    i = 0
    output_arr = quick_sort(input_arr, i)
    print("number of compare : ", i)