import random

ran_num = random.randint(1,100)
count = 0

while True:
	count += 1
	guess_number = input('請輸入數字: ')
	guess_number = int(guess_number)
	if guess_number < ran_num:
		print('比答案小')
	elif guess_number > ran_num:
		print('比答案大')
	else:
		print('你答對了答案就是: ', ran_num)
		print('一共猜了', count, '次')
		break
	print('一共猜了', count, '次')