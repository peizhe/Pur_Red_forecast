#usr/bin/env python
import time
import matplotlib.pyplot as plt


date = open('date_sort.txt','r')     # “date_sort.txt”存储20130701 ~ 20140831间的每个日期
Date_List = []
for line in date:
    if True:
        line = line.replace('\n','')
        line = line.split(',')
        Date_List.append(line[0])

date.close()

usr_list = []
usr = open('user.csv','r')          # “usr.csv”存储每天排好序的个用户ID号：1 ~ 28366
for line in usr:
    if True:
        line = line.split('\t')
        usr_list.append(line[0])
usr.close()
print '日期建表完成！'

for i in Date_List:                 #对日期为 i 的用户进行统计
    time1  = time.time()
    user_balance = open('user_balance_table.csv','r')   #“user_balance_table.csv”存储28366名用户在20130701 ~ 20140831期间全部的操作记录（共2811370条）
    date_times_usr_no = open('date_times_usr.txt','a')
    times = 0                       # 申购/赎回操作次数
    red = 0                         # 赎回次数
    pur = 0                         # 申购次数
    red_pur = 0                     # 同时申购和赎回次数
    usr_no = []                     # 操作人次
    usr_no_pur = []                 # 申购人次
    usr_no_red = []                 # 赎回人次
    usr_no_red_pur = []             # 同时申购和赎回次数
    
    for line in user_balance:      
        if True:
            line = line.split(',')
            if line[1] == i:                                      # line[1]存储操作日期
                times = times + 1
                usr_no.append(line[0])
                if int(line[4]) != 0:                             # line[4]存储当日总购买量：总购买量 = 直接购买 + 收益
                    pur = pur + 1
                    usr_no_pur.append(line[0])
                if int(line[8]) != 0:                             # line[8]存储当日总赎回量：今日总赎回量 = 消费 + 转出
                    red = red + 1
                    usr_no_red.append(line[0])
                if int(line[4]) != 0 and int(line[8]) != 0:
                    red_pur = red_pur + 1
                    usr_no_red_pur.append(line[0])

    usr_no = list(set(usr_no))
    usr_no = [int(x) for x in usr_no]
    usr_no = len(usr_no)                                         # 当日购买购买或赎回人次

    usr_no_pur = list(set(usr_no_pur))
    usr_no_pur = [int(x) for x in usr_no_pur]
    usr_no_pur = len(usr_no_pur)                                 # 当日购买购买人次
    
    usr_no_red = list(set(usr_no_red))
    usr_no_red = [int(x) for x in usr_no_red]
    usr_no_red = len(usr_no_red)                                 # 当日赎回人次

    usr_no_red_pur = list(set(usr_no_red_pur))
    usr_no_red_pur = [int(x) for x in usr_no_red_pur]
    usr_no_red_pur = len(usr_no_red_pur)                         # 当日同时购买和赎回人次
    


    date_times_usr_no.write(str(i))
    date_times_usr_no.write('\t')
    date_times_usr_no.write(str(times))
    date_times_usr_no.write('\t')
    date_times_usr_no.write(str(usr_no))
    date_times_usr_no.write('\t')
    date_times_usr_no.write(str(pur))
    date_times_usr_no.write('\t')
    date_times_usr_no.write(str(usr_no_pur))
    date_times_usr_no.write('\t')
    date_times_usr_no.write(str(red))
    date_times_usr_no.write('\t')
    date_times_usr_no.write(str(usr_no_red))
    date_times_usr_no.write('\t')
    date_times_usr_no.write(str(red_pur))
    date_times_usr_no.write('\t')
    date_times_usr_no.write(str(usr_no_red_pur))
    date_times_usr_no.write('\n')
    
    date_times_usr_no.close()
    user_balance.close()

    time2 = time.time()

    
    print '日期：',i
    print '今日的申购/赎回操作总次数：', times
    print '今日的申购/赎回操作总人数：', usr_no
    print '今日的申购操作次数', pur
    print '今日的申购人次：', usr_no_pur
    print ''
    print '今日的赎回操作次数：', red
    print '今日的赎回人次：', usr_no_red
    print ''
    print '今日的申购+赎回次数：', red_pur
    print '今日的申购+赎回人次：', usr_no_red_pur
    print ''
    print '计算时间：', time2 - time1
    print ''
    print ''
    print ''
    print ''
