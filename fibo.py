def recursive_nth_fibo(n):

    number = 0
    nas = []

    while n > 0:
        if n == 0:
            number += 0
            n -= 1
            nas.append(number)
        elif n == 1:
            number += 1
            n -= 1
            nas.append(number)
        else:
            fib = (n-1) + (n-2)
            number += fib
            n -= 1
            nas.append(number)

    return nas


def main():

    print(recursive_nth_fibo(3))

if __name__ == "__main__":
    main()
