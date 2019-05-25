import random

max_num = input('請輸入最大範圍數字: ')
max_num = int(max_num)
min_num = input('請輸入最小範圍數字: ')
min_num = int(min_num)
ran_num = random.randint(min_num, max_num)
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