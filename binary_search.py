#binary search algorithm

def BinarySearch(mylist,value):
    high = len(mylist) - 1
    low = 0
    count = 0
    
    while low <= high:
        mid = (high + low) // 2
       
        if mylist[mid] == value:
            print(f"value: {mylist[mid]}")
            print(f"index: {mid}")
            print(f"try: {count}")
            return mid  
        
        elif value > mylist[mid]:
            low = mid +1
        
        else:
            high = mid - 1
            
        count += 1
    
    print("value not found")
    print(f"try: {count}")
    return -1

