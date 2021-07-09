
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (low+high)//2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid-1, x)
        else:
            return binary_search(arr, mid+1, high, x)
    else:
        return -1


if __name__ == '__main__':
    test_array = [3,4,1,9,7]
    arr = sorted(test_array)
    print(arr)
    x = 9
    res = binary_search(arr,0,len(arr)-1, x)
    # print(res)
    if res != -1:
        print("element found" + str(res))
    else:
        print("Element not found!")
