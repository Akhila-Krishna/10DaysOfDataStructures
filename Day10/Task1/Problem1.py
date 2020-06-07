def recursive_multiply(x, y):
    tsum = 0
    i = 0
    while i != y: 
        tsum += x
        i += 1
    return tsum

f = recursive_multiply(5,3)
print(f)
