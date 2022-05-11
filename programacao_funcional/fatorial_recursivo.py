def fatorial(n):
    return n * (fatorial(n - 1) if (n - 1) > 1 else 1)


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')
    # 6 SEMANAS EM SEGUNDOS É IGUAL A 10!(FATORIAL)
