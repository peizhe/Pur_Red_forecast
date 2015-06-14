import time

Date_sort = open('Date_sort.txt','r')
Date_List = []
for line in Date_sort:
    if True:
        line = line.split('\n')
        Date_List.append(int(line[0]))
Date_sort.close()

for i in Date_List:
    time1 = time.time()
    usr_data = open('user_data.csv','r')
    date_sum = open('date_sum.txt','a')
    sum_pur = 0
    sum_red = 0
    for line in usr_data:
        if True:
            line = line.split(',')
            if int(line[1]) == i:
                sum_pur = sum_pur + int(line[4])   # 计算某一天总的申购量
                sum_red = sum_red + int(line[8])   # 计算某一天总的赎回量
    date_sum.write(str(i) + '\t' + str(sum_pur) + '\t' + str(sum_red) + '\n')
    time2 = time.time()
    
    print '日期：',i
    print '总购买金额：', sum_pur
    print '总赎回金额：', sum_red
    print '计算花费时间:',time2-time1
    
    usr_data.close()
