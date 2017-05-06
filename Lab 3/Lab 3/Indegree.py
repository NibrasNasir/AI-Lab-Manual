p = int(input("Enter Node No.:\t"))

p = p - 1
c = 0
l = [[0, 0, 0, 0, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [1, 0, 1, 1, 0]]
for a in range(0, 5):
    t = l[a][p]
    if (t == 1):
        c = c + 1
print("        Indegre", c)
