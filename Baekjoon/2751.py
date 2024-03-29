import sys
sys.stdin = open("Baekjoon/test.txt", "r")

# 수 정렬하기

import sys
n = int(sys.stdin.readline())

def merge_sort(arr) :
    if len(arr) < 2 : 
        return arr
    
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    merged_arr = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr) :
        if low_arr[l] < high_arr[h] :
            merged_arr.append(low_arr[l])
            l += 1
        else : 
            merged_arr.append(high_arr[h])
            h += 1
    merged_arr += low_arr[l:]
    merged_arr += high_arr[h:]
    return merged_arr


num_list = []

for i in range(n) :
    num = int(sys.stdin.readline())
    num_list.append(num)
    
sorted_list = merge_sort(num_list)

for i in sorted_list : 
    print(i)