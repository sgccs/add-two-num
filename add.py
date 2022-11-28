import sys
def input():return sys.stdin.readline().strip()
def add(t):
    while(t>0):
        a,b=map(int,input().split())
        print(a+b)
t=int(input())
add(t)