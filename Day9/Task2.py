# Cyclically Shifted Array

def find(A):
    pass
    low = 0
    high = len(A)-1

    if high < low:
        return A[0]
    if high == low:
        return A[low]
    
    mid = int((low + high)/2) 
    if mid < high and A[mid+1] < A[mid]: 
        return A[mid+1] 
    if mid > low and A[mid] < A[mid - 1]: 
        return A[mid] 
  
    if A[high] > A[mid]: 
        return find(A) 
    return find(A) 