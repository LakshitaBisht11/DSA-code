# Linear Search Program
arr = list(map(int, input("Enter array elements: ").split()))
key = int(input("Enter key element: "))

comparisons = 0
found = False

for i in range(len(arr)):
    comparisons += 1

    if arr[i] == key:
        found = True
        break

if found:
    print("Key Found")
else:
    print("Key Not Found")

print("Total Comparisons =", comparisons)
