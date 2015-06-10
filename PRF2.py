import matplotlib.pyplot as plt
user = open('user.csv','r')#用户ID--操作次数
user_list = []
for line in user:
  if True:
    data = line.replace('\n','')
    data = line.split('\t')
    user_list.append(int(data[1]))


user_index = list(user_list)
user_index=[int(x) for x in user_index]
user_index.sort()
index = list(xrange(450))

count = []
for i in index:

    count_i = user_list.count(i)
    count.append(count_i)

print len(index)

print len(count)

plt.scatter(index[5:],count[5:])
plt.xlabel('operation times(begin at 5 times)')
plt.ylabel('number of people')
plt.show()


user.close()
