if __name__ == '__main__':
    N = int(input())
    L = []
    for i in range(0, N):
        cmd, *args = input().rstrip().split()
        args = list(map(int, args))

        if cmd == 'print':
            print(L)
        else:
            getattr(L, cmd)(*args)
