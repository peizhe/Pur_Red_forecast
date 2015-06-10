#这个脚本用于对全部用户在过去几个月的操作次数进行统计分析。
#-*-utf-8-*-

#!/usr/bin/env python
user_data = open('user_data.csv','r')#原始的用户数据
user = open('user.csv','w')#用户ID--操作次数

user_list = []


for line in user_data:
    data = line.split(',')
    user_list.append(int(data[0]))

user_index = list(set(user_list))

user_index=[int(x) for x in user_index]
user_index.sort()

for i in user_index:
    count_i = user_list.count(i)
    print count_i
    user.write(str(i))
    user.write('\t')
    user.write(str(count_i))
    user.write('\n')
        

user_data.close()
user.close()
