array = [1, 2, 3]
N = len(array)

# 1
sel = [0] * N
check = [0] * N


def perm(idx):
    if idx == N:
        print(sel)
    else:
        for i in range(N):
            if not check[i]:
                check[i] = 1
                sel[idx] = array[i]
                perm(idx + 1)
                check[i] = 0


perm(0)
print('--------------')

check = [0] * N
sel = []


def powerset(idx):
    if idx == N:
        print(sel)
    else:
        check[idx] = 1
        sel.append(array[idx])
        powerset(idx + 1)
        check[idx] = 0
        sel.pop()
        powerset(idx + 1)


powerset(0)
