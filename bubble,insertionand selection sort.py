def bubble_sort(num):
    n = len(num)
    for i in range(n-1):
        for j in range(n-i-1):
            if num[j]>num[j+1]:
                num[j],num[j+1] = num[j+1],num[j]
    return num
l=[78,22,4,50,11,7,9,33]
b=bubble_sort(l)
print("sorted list:",b)


print("//////////////////////////////////////////////")


def insertion_sort(num):
    for i in range(1, len(num)):
        current = num[i]
        j = i - 1
        while j >= 0 and num[j] > current: #Shift elements greater than current to the right
            num[j + 1] = num[j]
            j -= 1
            num[j + 1] = current # Insert the current element in correct position
    return num
l1=[24,5,1,8,31,56,89]
res=insertion_sort(l1)
print(res)

print("//////////////////////////////////////////////")


def selection_sort(num):
    n = len(num)

    for i in range(n - 1):
        min_idx = i         # Find the minimum element in unsorted list
        for j in range(i + 1, n):
            if num[j] < num[min_idx]:
               min_idx = j
        num[i], num[min_idx] = num[min_idx], num[i]   # Swap the found minimum with the first element
    return num
l2=[92,45,3,67,2,9,1,32]
res=selection_sort(l2)
print(res)
