# coding: UTF-8

# a = [1,2,3]
# print(a)

# nums = [0]*10
# print(nums)

# a = list(range(-5,6))
# print(a)

# a = list("aaa")
# print(a)

# r101 = "田中"
# r102 = "佐藤"
# r201 = "a"
# r202 = "d"
# floor1 = [r101,r102]
# floor2 = [r201,r202]
# apartment = [floor1,floor2]
# print(apartment)
# length = len(apartment)
# print(length)

# try:
#     pos = int(input("取り出す位置"))
#     colors = ["a","b","t","U"]
# except Exception as error :
#     print(error)
#
# try:
#     item = colors[pos]
#     print(item)
# except IndexError:
#     print("インデックスエラーです")
# except Exception as error :
#     print(error)
# finally:
#     print("エラーゃ")

# data = []
# data.append(10)
# print(data)
# data.insert(0,100)
# print(data)
# a = data.pop()
# print(a)
# print(data)

# a = ["a","s","u","j","g"]
# if a :
#     d = a.pop()
#     print(d)
# print(a)

# a = ["a","s","u","j","g"]
# print("削除前",a)
# b = "s"
# if b in a:
#     a.remove(b)
# print("削除後",a)

a = ["a","s","y"]
b = " and ".join(a)
print(b)
