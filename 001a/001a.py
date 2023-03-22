import random

#Laver 1000 random tal mellem 0-100
A = [random.randint(0, 100) for _ in range(1000)]

#tilføjer 10 nye tal til listen
A.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

#laver liste b med tal fra a mellem 50-60 og fjerne dem fra a
B = [x for x in A if 50 <= x <= 60]
A = [x for x in A if x not in B]

# bubble search
n = len(A)
for i in range(n):
    for j in range(0, n-i-1):
        if A[j] > A[j+1]:
            A[j], A[j+1] = A[j+1], A[j]

#printer lister
print("Liste A:", A)
print("Liste B:", B)