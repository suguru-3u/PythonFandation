# # # # coding: UTF-8
# # # # 「Hello World」と出力してください
# # # print('Hello World')
# # #
# # # # 数値の7を出力してください
# # # print(7)
# # #
# # # # 9に3足した値を出力してください
# # # print(9+3)
# # #
# # # # 「9 + 3」を文字列として出力してください
# # # print('9+3')
# # #
# # # # 9を2で割った値を出力してください
# # # print(9/2)
# # #
# # # # 7に5を掛けた値を出力してください
# # # print(7*5)
# # #
# # # # 5を2で割った時の余りを出力してください
# # # print(5%2)
# # #
# # # # 変数nameに文字列「にんじゃわんこ」を代入してください
# # # name = 'にんじゃわんこ'
# # #
# # # # 変数nameの値を出力してください
# # # print(name)
# # #
# # # # 変数numberに数値の7を代入してください
# # # number = 7
# # #
# # # # 変数numberの値を出力してください
# # # print(number)
# # #
# # # apple_price = 200
# # # apple_count = 8
# # #
# # # # apple_priceとapple_countを掛けた結果を、変数total_priceに代入してください
# # # total_price = apple_price * apple_count
# # #
# # # # total_priceの値を出力してください
# # # print(total_price)
# # #
# # # money = 2000
# # # print(money)
# # #
# # # # 変数moneyに5000を足して、変数moneyを上書きしてください
# # # money += 5000
# # #
# # # # 変数moneyの値を出力してください
# # # print(money)
# # #
# # # # my_nameという変数に「にんじゃわんこ」という文字列を代入してください
# # # my_name = 'にんじゃわんこ'
# # #
# # # # my_nameを用いて、「私はにんじゃわんこです」となるように変数と文字列を連結して出力してください
# # # print('私は' + my_name)
# # #
# # # age = 24
# # # # ageを用いて「私は24歳です」と出力してください
# # # print('私は' +  str(age) + 'です')
# # #
# # # count = '5'
# # # # countに1を足した値を出力してください
# # # print(int(count) + 1)
# # #
# # # x = 7 * 10
# # # y = 5 * 6
# # #
# # # # xが70と等しい場合に「xは70です」と出力してください
# # # if x == 70:
# # #     print('xは70です')
# # #
# # #
# # # # yが40と等しくない場合に「yは40ではありません」と出力してください
# # # if y != 40:
# # #     print('yは40ではありません')
# # #
# # # x = 10
# # # # xが30より大きい場合に「xは30より大きいです」と出力してください
# # # if x > 30:
# # #     print('xは30より大きいです')
# # #
# # #
# # # money = 500
# # # apple_price = 200
# # # # moneyの値がapple_priceの値以上の時、「りんごを買うことができます」と出力してください
# # # if money > apple_price:
# # #     print('りんごを買うことができます')
# # #
# # # money = 100
# # # apple_price = 200
# # #
# # # if money >= apple_price:
# # #     print('りんごを買うことができます')
# # # # if文の条件に当てはまらない場合に「お金が足りません」と出力してください
# # # else:
# # #     print('お金が足りません')
# # #
# # # money = 100
# # # apple_price = 100
# # #
# # # if money > apple_price:
# # #     print('りんごを買うことができます')
# # # # 変数の値が等しい場合に「りんごを買うことができますが所持金が0になります」と出力してください
# # # elif  money == apple_price:
# # #     print('りんごを買うことができますが所持金が0になります')
# # #
# # # else:
# # #     print('お金が足りません')
# # #
# # # x = 20
# # # # xが10以上30以下の場合に「xは10以上30以下です」と出力してください
# # # if 10 <= x and x <= 30:
# # #     print('xは10以上30以下です')
# # #
# # #
# # # y = 60
# # # # yが10未満または30より大きい場合に「yは10未満または30より大きいです」と出力してください
# # # if y < 10 or 30 < y:
# # #     print('yは10未満または30より大きいです')
# # #
# # # z = 55
# # # # zが77ではない場合に「zは77ではありません」と出力してください
# # # if not z == 77:
# # #     print('zは77ではありません')
# # #
# # # if money > apple_price:
# # #     print('りんごを買うことができます')
# # # # 変数の値が等しい場合に「りんごを買うことができますが所持金が0になります」と出力してください
# # # elif  money == apple_price:
# # #     print('りんごを買うことができますが所持金が0になります')
# # #
# # # else:
# # #     print('お金が足りません')
# # #
# # # x = 20
# # # # xが10以上30以下の場合に「xは10以上30以下です」と出力してください
# # # if 10 <= x and x <= 30:
# # #     print('xは10以上30以下です')
# # #
# # #
# # # y = 60
# # # # yが10未満または30より大きい場合に「yは10未満または30より大きいです」と出力してください
# # # if y < 10 or 30 < y:
# # #     print('yは10未満または30より大きいです')
# # #
# # # z = 55
# # # # zが77ではない場合に「zは77ではありません」と出力してください
# # # if not z == 77:
# # #     print('zは77ではありません')
# # #
# # # # apple_priceという変数に数値200を代入してください
# # # apple_price = 200
# # #
# # # # countという変数に数値5を代入してください
# # # count = 5
# # #
# # # # total_priceという変数に、apple_priceとcountを掛けたものを代入してください
# # # total_price = apple_price * count
# # #
# # # # 「購入するりんごの個数は○○個です」となるように出力してください
# # # print('購入するりんごの個数は' + str(count) + '個です')
# # #
# # # # 「支払い金額は○○円です」となるように出力してください
# # # print('支払い金額は' + str(total_price) + '円です')
# # #
# # # apple_price = 200
# # #
# # # # inputを用いて入力を受け取り、変数input_countに代入してください
# # # input_count = input('購入するりんごの個数を入力してください：')
# # #
# # # # input_countを数値として代入してください
# # # count = int(input_count)
# # # total_price = apple_price * count
# # #
# # # print('購入するりんごの個数は' + str(count) + '個です')
# # # print('支払い金額は' + str(total_price) + '円です')
# # #
# # # apple_price = 200
# # # # 変数moneyに数値1000を代入してください
# # # money = 1000
# # #
# # # input_count = input('購入するりんごの個数を入力してください：')
# # # count = int(input_count)
# # # total_price = apple_price * count
# # #
# # # print('購入するりんごの個数は' + str(count) + '個です')
# # # print('支払い金額は' + str(total_price) + '円です')
# # #
# # # # moneyとtotal_priceの比較結果によって条件を分岐してください
# # # if money > total_price:
# # #     print('りんごを'  + str(count) +  '個買いました')
# # #     print('残金は' +  str(money - total_price)  + '円です')
# # # elif money == total_price:
# # #     print('りんごを'  + str(count) +  '個買いました')
# # #     print('財布が空になりました')
# # # else:
# # #     print('お金が足りません')
# # #     print('りんごを買えませんでした')
# #
# # # 変数fruitsに、複数の文字列を要素に持つリストを代入してください
# # fruits = ['apple','banana','orange']
# #
# # # インデックス番号が0の要素を出力してください
# # print(fruits[0])
# #
# # # インデックス番号が2の要素を文字列と連結して出力してください
# # print('好きな果物は'+ fruits[2] +'です')
# #
# # fruits = ['apple', 'banana', 'orange']
# #
# # # リストの末尾に文字列「grape」を追加してください
# # fruits.append('grape')
# #
# # # 変数fruitsに代入したリストを出力してください
# # print(fruits)
# #
# # # インデックス番号が0の要素を文字列「cherry」に更新してください
# # fruits[0] = 'cherry'
# #
# # # インデックス番号が0の要素を出力してください
# # print(fruits[0])
# #
# # fruits = ['apple', 'banana', 'orange']
# #
# # # for文を用いてリストの要素を1つずつ取り出し、「好きな果物は◯◯です」と出力してください
# # for fruit in fruits:
# #     print('好きな果物は'+ fruit +'です')
# #
# # # 変数fruitsに辞書を代入してください
# # fruits = {'apple':'りんご','banana':'バナナ'}
# #
# # # 辞書fruitsのキー「banana」に対応する値を出力してください
# # print(fruits['banana'])
# #
# # # 辞書fruitsを用いて、「appleは◯◯という意味です」となるように出力してください
# # print('appleは'+fruits['apple']+'という意味です')
# #
# # fruits = {'apple': 100, 'banana': 200, 'orange': 400}
# #
# # # キー「banana」の値を数値「300」に更新してください
# # fruits['banana'] = 300
# #
# # # キーが「grape」、値が数値の「500」の要素を辞書fruitsに追加してください
# # fruits['grape'] = 500
# #
# # # fruitsの値を出力してください
# # print(fruits)
# #
# # fruits = {'apple': 'りんご', 'banana': 'バナナ', 'grape': 'ぶどう'}
# #
# # # for文を用いて、辞書のキーを1つずつ取り出し、繰り返しの中で「◯◯は△△という意味です」と出力させてください
# # for fruit_key in fruits:
# #     print(fruit_key + 'は' +fruits[fruit_key] +'という意味です')
# #
# # x = 10
# #
# # # while文を用いて、「変数xが0より大きい」間、繰り返される繰り返し処理を作ってください
# # while x > 0:
# #     # 変数xを出力してください
# #     print(x)
# #     # 変数xから1引いてください
# #     x -= 1
# #
# # numbers = [765, 921, 777, 256]
# # for number in numbers:
# #     print(number)
# #     # 変数numberが777のとき「777が見つかったので処理を終了します」と出力した後、処理を終了させてください
# #     if number == 777:
# #         print('777が見つかったので処理を終了します')
# #         break
# #
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # for number in numbers:
# #     # 変数numberの値が3の倍数のとき、繰り返し処理をスキップしてください
# #     if number % 3 == 0:
# #         continue
# #     print(number)
# #
# # # 文字列のキーと数値の値を持つ辞書を作って、変数itemsに代入してください
# # items = {'apple':100,'banana':200,'orange':400}
# #
# # # for文を用いて、辞書itemsのキーを1つずつ取り出していく繰り返し処理を作成してください
# # for item_name in items:
# #     # 「---------------------------------------------」を出力してください
# #     print('---------------------------------------------')
# #     # 「◯◯は1個△△円です」となるように出力してください
# #     print(item_name + 'は1個' + str(items[item_name]) + '円です')
# #
# # items = {'apple': 100, 'banana': 200, 'orange': 400}
# # for item_name in items:
# #     print('--------------------------------------------------')
# #     print(item_name + 'は1個' + str(items[item_name]) + '円です')
# #
# #     # inputを用いて入力を受け取り、変数input_countに代入してください
# #     input_count = input('購入する' + item_name + 'の個数を入力してください：')
# #     # キーと変数input_countを用いて「購入する◯◯の個数は△△個です」となるように出力してください
# #     print('購入する'+item_name+'の個数は'+input_count+'個です')
# #
# #     # input_countを数値として変数countに代入してください
# #     count = int(input_count)
# #     # 変数total_priceに果物1個の値段と変数countを掛けた値を代入してください
# #     total_price = items[item_name] * count
# #     # 変数total_priceと型変換を用いて、「支払い金額は◯◯円です」となるように出力してください
# #     print('支払い金額は'+str(total_price)+'円です')
# #
# # # 変数moneyに数値1000を代入してください
# # money = 1000
# #
# # items = {'apple': 100, 'banana': 200, 'orange': 400}
# # for item_name in items:
# #     print('--------------------------------------------------')
# #     # 変数moneyを用いて「財布には◯◯円入っています」のように出力してください
# #     print('財布には'+ str(money) +'円入っています')
# #
# #     print(item_name + 'は1個' + str(items[item_name]) + '円です')
# #
# #     input_count = input('購入する' + item_name + 'の個数を入力してください：')
# #     print('購入する' + item_name + 'の個数は' + input_count + '個です')
# #
# #     count = int(input_count)
# #     total_price = items[item_name] * count
# #     print('支払い金額は' + str(total_price) + '円です')
# #
# #     # moneyとtotal_priceの比較結果によって条件を分岐してください
# #     if money >= total_price:
# #         print(item_name+'を'+str(count) +'個買いました')
# #         money = money - total_price
# #     else:
# #         print('お金が足りません')
# #         print(item_name+'を買えませんでした')
# #
# # money = 1000
# # items = {'apple': 100, 'banana': 200, 'orange': 400}
# # for item_name in items:
# #     print('--------------------------------------------------')
# #     print('財布には' + str(money) + '円入っています')
# #     print(item_name + 'は1個' + str(items[item_name]) + '円です')
# #
# #     input_count = input('購入する' + item_name + 'の個数を入力してください：')
# #     print('購入する' + item_name + 'の個数は' + input_count + '個です')
# #
# #     count = int(input_count)
# #     total_price = items[item_name] * count
# #     print('支払い金額は' + str(total_price) + '円です')
# #
# #     if money >= total_price:
# #         print(item_name + 'を' + input_count + '個買いました')
# #         money -= total_price
# #         # if文を用いて、moneyの値が0のときの条件を分岐してください
# #         if money == 0:
# #             print('財布が空になりました')
# #             break
# #     else:
# #         print('お金が足りません')
# #         print(item_name + 'を買えませんでした')
# # # 変数moneyと型変換を用いて、「残金は◯◯円です」となるように出力してください
# # print('残金は'+str(money)+'円です')
#
# # print(max(3,5,6))
# # import math
# # a = math.ceil(15.2)
# # print(a)
# #
# # # from random import randint
# # # b = randint(1,6)
# # # print(b)
# #
# # from random import randint as c
# # b = c(1,6)
# # print(b)
#
# a = 'hello'
# print(type(a))
# print(a.upper())
# print(a.count('e'))
# print(a.replace('e','x'))

# money = 1000
# items = {'apple': 100, 'banana': 200, 'orange': 400}
# for item_name in items:
#     print('--------------------------------------------------')
#     print('財布には' + str(money) + '円入っています')
#     print(item_name + 'は1個' + str(items[item_name]) + '円です')
#
#     input_count = input('購入する' + item_name + 'の個数を入力してください：')
#     print('購入する' + item_name + 'の個数は' + input_count + '個です')
#
#     count = int(input_count)
#     total_price = items[item_name] * count
#     print('支払い金額は' + str(total_price) + '円です')
#
#     if money >= total_price:
#         print(item_name + 'を' + input_count + '個買いました')
#         money -= total_price
#         # if文を用いて、moneyの値が0のときの条件を分岐してください
#         if money == 0:
#             print('財布が空になりました')
#             break
#     else:
#         print('お金が足りません')
#         print(item_name + 'を買えませんでした')
# # 変数moneyと型変換を用いて、「残金は◯◯円です」となるように出力してください
# print('残金は'+str(money)+'円です')


# 変数moneyに数値1000を代入してください
money = 1000

items = {'apple': 100, 'banana': 200, 'orange': 400}
for item_name in items:
    print('--------------------------------------------------')
    # 変数moneyを用いて「財布には◯◯円入っています」のように出力してください
    print('財布には'+ str(money) +'円入っています')

    print(item_name + 'は1個' + str(items[item_name]) + '円です')

    input_count = input('購入する' + item_name + 'の個数を入力してください：')
    print('購入する' + str(item_name) + 'の個数は' + str(input_count) + '個です')

    count = int(input_count)
    total_price = items[item_name] * count
    print('支払い金額は' + str(total_price) + '円です')

    # moneyとtotal_priceの比較結果によって条件を分岐してください
    if money >= total_price:
        print(item_name+'を'+str(count) +'個買いました')
        money = money - total_price
    else:
        print('お金が足りません')
        print(item_name+'を買えませんでした')
