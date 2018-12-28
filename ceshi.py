password = 'a123456'
i = 3
i = int(i)
while i > 0:

	key = input('输入密码:')
	if key == password:
		print('密码正确!')
		break
	else:
		i = i - 1
		print('密码错误！')
		if i > 0:
			print('你还有', i ,'次机会')
