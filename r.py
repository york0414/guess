import random
start = input('請輸入數字範圍開始值')
end = input('請輸入數字範圍結束值')
start = int(start)
end = int(end)

r = random.randint (start, end)
count = 0
while True:
	count  += 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('恭喜你猜中了！')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大了喔')

	elif num < r:
		print('比答案小了喔!')
	print('這是你猜的第', count, '次')
