# for i in range(11):
#     print(f"the number{i}")

# dict1=[{"name":"girish",
#         "status":"present"},
#       {"name":"srujan",
#        "status":"absent"},
#        {"name":"srujan1",
#        "status":"absent"},
#        {"name":"srujan3",
#        "status":"present"}]
# for stundents in dict1:
#     if stundents["status"] == "present":
#         print(stundents["name"])
#     else:
#         print("remaning students are absent")
# for i in range(4):
#     for j in range(4):
#         print("*",end="")
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()

# while loop
# n=100
# i=1
# while i<=n:
#     print(i)
#     i+=1

# n=100
# i=1
# while n>=i:
#     print(n)
#     n-=1

# n=11
# i=1
# while i<=10:
#     print(n*i)
#     i+=1

# list1=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# i=0
# while i<len(list1):
#     print(list1[i])
#     i+=1

# x = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# i = 0
# x1 = 6

# while i < len(x):
#     if i == x1:
#         print(x[i])
#         break
#     i += 1

# n=[1,2,3,4,5]
# i=0
# sum=0
# while i<len(n):
#     sum+=n[i]
#     i+=1
# print(sum)


# list1=(1, 4, 9, 16, 25, 36, 49, 64, 81,100)
# x=49
# i=0
# found=False
# for i in list1:
#     if list1[i]==x:
#         print(f"{x} is found at index{i}")
#         found=True
#         break
# if not found:
#     print(f"{x} is not found in list1")

fact=5
n=1
for i in range(1,fact+1):
    n*=i
print(n)

   
