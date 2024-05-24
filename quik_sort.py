def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def replace_elements(arr, target, replacement):
    return [replacement if x == target else x for x in arr]

def main():
    # Prompt the user to input an array of integers
    user_input = input("Enter a list of integers separated by spaces: ")
    array = list(map(int, user_input.split()))

    # Sort the array using quick sort
    sorted_array = quick_sort(array)
    print(f"Sorted array: {sorted_array}")

    # Allow the user to specify a target element to search for in the sorted array
    target = int(input("Enter the target element to replace: "))

    # Check if the target element is in the array
    if target in sorted_array:
        replacement = int(input(f"Enter the replacement for {target}: "))

        # Replace all occurrences of the target element with the replacement element
        modified_array = replace_elements(sorted_array, target, replacement)
        print(f"Modified array: {modified_array}")
    else:
        print(f"Element {target} not found in the array")

if __name__ == "__main__":
    main()
