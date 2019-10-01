t = 3
while t > 0 :
	pw = input('請輸入密碼')
	if pw == 'a123456':
		print('登入成功')
		break
	else:
		t = t - 1
		if t == 0:
			print('沒機會了，再見')
			break
		print('密碼錯誤！還有' , t , '次機會')