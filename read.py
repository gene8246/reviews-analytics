data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 #count = count + 1
		if count % 1000 == 0: #求餘數
			print(len(data))
print('loading reviews finished, we have', len(data), 'reviews')
print(data[0])

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

#文字計數
wc = {} # words_counts
for d in data:
	words = d.split() #split預設值為切割空白,且不會對連續空白鍵切割
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1

for word in wc:
	if wc[word] > 10000:
		print(word, wc[word])

print(len(wc))

while True:
	word = input('please enter the word you would like to look for: ')
	if word == 'q':
		break
	elif word in wc:
		print(word, 'has been writen in', wc[word], 'times')
	else:
		print(word, 'is not in all reviewes' ) 

#good = []
#for d in data:
#	if 'good' in d:
#		good.append(d)
#print('review with good word:', len(good))
#print(good[50])
