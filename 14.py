def myPow(x: float, n: int) -> float:
    ans = 1.0
    for i in range(n):
        ans = ans * x
    return ans

if __name__ == "__main__":
    print(myPow(2, 10))
