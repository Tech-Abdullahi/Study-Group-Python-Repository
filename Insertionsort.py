# Insertion Sort Algorithm

# Function to do insertion sort
def InsertionSort(arr):
 
    # Traverse through 1 to len(arr)
    # Since Python list are indexed using zero-based numbering,
    # meaning that the first element in a list is at index 0, the second elementis at indexed 1 and so on
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key

#Test Code
arr = [31, 41, 59, 26, 41, 58]
InsertionSort(arr)
print(arr)
