def binarySearch(arr, l, r, x): 
  
    while l <= r: 
        mid = int(l + (r - l)/2) 
        if arr[mid] == x: 
            return mid 
        elif arr[mid] < x: 
            l = mid + 1
        else: 
            r = mid - 1 
    return -1
  

arr = []
n = int(input("enter number of elemnts in list:"))
for i in range(0,n):
    ele=int(input("enter number in sorted order"))
    arr.append(ele)
x = int(input("enter number to search"))
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index % d" % result) 
else: 
    print ("Element is not present in array")
