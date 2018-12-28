password = 'a123456'
i = 3
i = int(3)
while i > 0:
    KEY = input('请输入密码：')
    if KEY == password:
	    print('登陆成功！')
	    break
    else:
	    i = i - 1
	    print('密码错误！还有' ,i,'次机会')
	    
