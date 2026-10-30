def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

    for k in range(n):
        print(k)


print_items(10)

# Since the O(n^2) trumps the O(n) we just drop it instead of writing O(n^2 + n), we just write O(n^2)
