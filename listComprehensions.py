#Program to print a list of all possible coordinates given by(i,j,k) on a 3D grid where the sum of i,j,k  is not equal to n
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print(list([a,b,c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1) if (( a + b + c ) != n )))

#Simple Py program to print second largest number in a list of inputs
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    l=list(arr)
    z=max(l)
    while max(l)==z:
        l.remove(max(l))
    print(max(l))
