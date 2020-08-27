# coding: UTF-8

# a = 1 + 2 \
# + 3
# print(a)
# c = """aaaa
#     aaaaa
#     aaaa"""
# print(c)
#
# b = str(2500) + "円です"
# print(b)

# print(type(b))

# a = "3"
# print(int(a))

# a = 20
# a += 1
# print(a)

# a = "あああ"
# b = "今"
# b += a
# print(b)

# import math
# a = math.ceil(15.2)
# print(a)

# a = "Hello"
# print(type(a))
# print(a.upper())

# s = "aaa{}と{}"
# b = s.format("a","a")
# print(b)

# s = "{name}選手,年齢{age}"
# t = s.format(name = "ああ",age = 27)
# print(t)

# a = 4
# if a == 3:
#     print("お")
# else:
#     print("違う")
#
# a += 5
# print(a)

# sum = 100
# limit = 100x
#
# if sum > limit:
#     result = "合格"
# elif sum == limit:
#     result = "補欠合格"
# else:
#     result = "不合格"
#     result += "/" + str(sum - limit)
#
# print(sum)
# print("-" * 10)
# print(result)

# from random import randint
# a = randint(0,100)
# b = randint(0,100)
#
# result = "合格" if a >= 40 and b >= 40 and (a+b) >= 120 else "不合格"
#
# print(result)

# c =  1
# count = 0
# while c == 1:
#     count += 1
#     print("継続"+ str(count))
#     if count == 10:
#         c +=1
#         print("終了")

# from random import randint
# t = 5
# p = 0
# fmt = "{:>3}"
# while t > 0:
#     v = randint(1,20)
#     print(fmt.format(v))
#     p += v
#     t -= 1
#     if  p > 20:
#         break
#
# print("-"*20)
# print(fmt.format(p))

# from random import randint
# miss = 0
# correct = 0
# print("問題！3回間違えるか,qを押すと終了する")
# while miss < 3:
#     a = randint(1,100)
#     b = randint(1,100)
#     ans = a + b
#     question = "{}+{}は?".format(a,b)
#     value = input(question)
#
#     if value == q:
#         break
#
#     if value == ans:
#         correct +=1
#         print("正解です")
#     else:
#         miss += 1
#         print("不正解です")
#
# print("-"*30)
# print("正解数" + str(correct))
# print("不正解" + str(miss))

# from random import randint
# numbers = []
# while len(numbers) < 10:
#     n = randint(1,100)
#     if n in numbers:
#         continue
#     numbers.append(n)
# print(numbers)

# color = ["a","d","D"]
# for i in range(10):
#     print(i)

# for i in range(4):
#     print()
#     for j in range(3):
#         x = j*2
#         y = i*3
#         print("({},{})".format(x,y))
# print()

# n = [3,4,5,6,5]
# sum = 0
# for num in n:
#     if not isinstance(num,(int,float)):
#         print(" 違う")
#         break
#     sum += num
#     print (num,"/",sum)
# else:
#     print("処理終わったで〜")

# while True:
#     num = input("何個ですか?(qで終了)")
#     if num == "q":
#         print("終了します")
#         break
#     try :
#         price = 120 * int(num)
#         print("金額")
#     except :
#         print("エラーです。正しい数値を入れてください")
#     finally:
#         print("計算終わり")
# num = 0
# try :
#     value = 120 /num
#     value = 120 /num
#     print(value)
# except Exception as b:
#     print("エラー")
#     print(b)
# finally :
#     print("計算終わり")
