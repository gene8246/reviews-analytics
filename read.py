data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0: #求餘數
			print(len(data))
print('loading reviews finished, we have', len(data), 'reviews')

sum_len = 0
for d in data:
	sum_len += len(d) #sum_len = sum_len + len(d)
average = sum_len / len(data)
print('average count is', average)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('review of less than 100 words:', len(new))

good = [d for d in data if 'good' in d]
print(len(good))

#good = []
#for d in data:
#	if 'good' in d:
#		good.append(d)
#print('review with good word:', len(good))
#print(good[50])
