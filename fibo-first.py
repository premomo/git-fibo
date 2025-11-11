def fibo(k):

    if k < 2:
        return k
    return fibo(k - 1) + fibo(k - 2)

if __name__ == "__main__":
    print(fibo(10))
