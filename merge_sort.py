# merge sort algorithm

# input : array (len : n) not sorted
# output : array (len : n) sorted

import random
input_arr = list()
for i in range(32):
    input_arr.append(random.randint(0,1000))
print(input_arr)
output_arr = list()

A = list()
B = list()
N = len(input_arr)
n = int(N/2)
for idx in range(n):
    A.append(input_arr[idx])
for idx in range(n):
    B.append(input_arr[idx+n])

A.sort()
B.sort()

print(A, B)
i = 0
j = 0
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
    print(output_arr)

print(output_arr)
print(len(output_arr))