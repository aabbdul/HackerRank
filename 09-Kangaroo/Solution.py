def kangaroo(x1, v1, x2, v2):
    if v1<=v2:
        return 'NO'
    
    while x1<x2:
        x1+=v1
        x2+=v2

    return 'YES' if x1==x2 else 'NO'
if __name__ == '__main__':
    
    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])
    
    v1 = int(x1V1X2V2[1])
    
    x2 = int(x1V1X2V2[2])
    
    v2 = int(x1V1X2V2[3])

    res = kangaroo(x1, v1, x2, v2)

    print(res)
