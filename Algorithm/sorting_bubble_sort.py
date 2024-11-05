
def bubble_sort(arr):

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]

                print(arr)


# Sample list to be sorted
arr = [39, 12, 18, 85, 72, 10, 2, 18]
print("The UNSORTED list ",arr)

bubble_sort(arr)

print("\nThe SORTED list")
print(arr)
