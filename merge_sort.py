# merge sort algorithm

# input : array (len : n) not sorted
# output : array (len : n) sorted

import random
input_arr = list()
for i in range(16):
    input_arr.append(random.randint(0,1000))

def lower_level(input_arr):
    temp = list()
    N = len(input_arr)
    n = int(N/2)
    A = list()
    B = list()
    for idx in range(n):
        A.append(input_arr[idx])
        B.append(input_arr[idx+n])
    temp.append(A)
    temp.append(B)
    return temp

def two_pointer(A, B):
    assert len(A) == len(B)
    N = int(len(A) + len(B))
    n = int(N/2)
    i = 0
    j = 0
    output_arr = list()
    for idx in range(N):
        if A[i] >= B[j]:
            output_arr.append(B[j])
            j += 1
        elif A[i] < B[j]:
            output_arr.append(A[i])
            i += 1
        if i == n:
            while j < n:
                output_arr.append(B[j])
                j += 1
            break
        elif j == n:
            while i < n:
                output_arr.append(A[i])
                i += 1
            break
    return output_arr

def merge_sort(input_arr:list):
    '''
    input : non-sorted array 
    output : sorted array 
    '''
    
    temp1 = lower_level(input_arr)
    temp2 = list()
    for arr in temp1:
        temp_ = lower_level(arr)
        temp2.extend(temp_)
    while True:
        temp = list()
        for arr in temp2:
            temp_ = lower_level(arr)
            temp.extend(temp_)
        temp2 = temp
        if len(temp2[0]) == 2:
            break
    for arr in temp2:
        temp = arr[0]
        temp_ = arr[1]
        if temp >= temp_:
            arr[0] = temp_
            arr[1] = temp

    while len(temp2) != 1:
        temp = list()
        for idx in range(len(temp2)):
            if idx % 2 == 0:
                temp1 = two_pointer(temp2[idx], temp2[idx+1])
                temp.append(temp1)
            else:
                pass
        temp2 = temp
    output = temp2[0]
    return output

output = merge_sort(input_arr)
print(output)

