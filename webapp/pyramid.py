# # Python 3.x code to demonstrate star pattern
#
# def pypart(n):
#     k = n-1
#     for i in range(0, n):
#         for j in range(0, k):
#             print(end=" ")
#
#         k = k-1
#         for j in range(0, i + 1):
#
#             print("* ", end="")
#
#         print("\r")
#
#
#
# n = int(input())
# pypart(n)
def pyramid(row):

    for i in range(row, 0, -1):
        for j in range(row-i):
            print(" ", end=" ")
        for j in range(2*i-1):
            print("*", end=" ")
        print()


row = int(input('Enter row: '))
pyramid(row)