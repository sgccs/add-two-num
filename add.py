import sys
def input():return sys.stdin.readline().strip()
def add(t):
    return (int(input())+add(t-1))
t=int(input())
add(t)

