# def solution(n):
#     # 4 < n < 12
#     n_m = n - 2

#     def binary_converting(n,i):
#         binary_boi = ""
#         while n > 0:
#             remainder = n % i
#             binary_boi = str(remainder) + binary_boi
#             n //= i
#         return binary_boi
    
#     res = []
#     for i in range(2,n-2):
#         print(i)
#     return True

# solution(4)

for i in range(2,4-2):
        print(i)