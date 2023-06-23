# 密碼重試程式
# password = 'a123456'
# 讓使用者重複輸入密碼
# 最多輸入3次
# 如果正確 就印出 " pass! "
# 如果不正確 就印出 "error! last _ times!"
password = '123'
t = 3 # 剩餘機會
while t > 0:
    answer = input('please enter password: ')
    if answer == password:
        print('pass!')
        break
    elif answer != password:
        t = t - 1
        if t == 2:
            print('error! last',t,'times!')
        elif t == 1:
            print('error! last',t,'time!')
        else:
            print('no more chance!')
    elif t == 0:
        break