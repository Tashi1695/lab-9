def bubble_sort_2d(arr):
    n = len(arr)
    m = len(arr[0])
    total_element = n * m

    for i in range (total_element -1):
        for j in range (total_element - 1 - i):
            row1 = j // m
            col1 = j % m

            row2 = (j + 1) // m
            col2 = (j + 1) % m

            if arr[row1][col1] > arr[row2][col2]:
                arr[row1][col1], arr[row2][col2] = arr[row2][col2], arr[row1][col2]

def search_element(arr, element):
    found = False
    for i in range (len(arr)):
        for j in range (len(arr[i])):
            if arr[i][j] == element:
                print(f"element found at: row = {i} , col = {j}")
                found = True
                return 
    if not found:
        print("element not found")


arr = [[9,3,4],[4,5,6],[4,6,3]]

print(arr)
bubble_sort_2d(arr)
print(arr)

#searching element
search = int(input("enter element to search:"))
search_element(arr, search)