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
    date_sum_all = open('date_sum_all.txt','a')
    sum_pur_total = 0        #4
    sum_red_total = 0        #8

    sum_pur_direct = 0       #5
    sum_pur_bal = 0          #6
    sum_pur_bank = 0         #7
    sum_share = 0            #13
    
    sum_red_con = 0          #9
    sum_red_tr = 0           #10
    sum_red_tftobal = 0      #11
    sum_red_tftocard = 0     #12
    sum_cat1 = 0             #14
    sum_cat2 = 0             #15 
    sum_cat3 = 0             #16
    sum_cat4 = 0             #17
    for line in usr_data:
        if True:
            line = line.split(',')
            line[17] = line[17].replace('\n','')
            if int(line[1]) == 20140831:
                sum_pur_total = sum_pur_total + int(line[4])   # 计算某一天总的申购量
                sum_red_total = sum_red_total + int(line[8])   # 计算某一天总的赎回量

                sum_pur_direct = sum_pur_direct + int(line[5])       #5
                sum_pur_bal = sum_pur_bal + int(line[6])         #6
                sum_pur_bank = sum_pur_bank + int(line[7])         #7
                sum_share = sum_share + int(line[13])             #13
    
                sum_red_con = sum_red_con + int(line[9])          #9
                sum_red_tr = sum_red_tr + int(line[10])           #10
                sum_red_tftobal = sum_red_tftobal + int(line[11])      #11
                sum_red_tftocard = sum_red_tftocard + int(line[12])     #12

                if line[14] == '':
                    line[14] = 0
                sum_cat1 = sum_cat1 + int(line[14])             #14
                if line[15] == '':
                    line[15] = 0
                sum_cat2 = sum_cat2 + int(line[15])             #15
                if line[16] == '':
                    line[16] = 0                
                sum_cat3 = sum_cat3 + int(line[16])             #16
                if line[17] == '':
                    line[17] = 0                   
                sum_cat4 = sum_cat4 + int(line[17])             #17

    date_sum_all.write(str(20140831) + '\t' + str(sum_pur_total) + '\t' + str(sum_red_total) + '\t') 
    date_sum_all.write(str(sum_pur_direct) + '\t' + str(sum_pur_bal) + '\t' + str(sum_pur_bank) + '\t' + str(sum_share) + '\t')
    date_sum_all.write(str(sum_red_con) + '\t' + str(sum_red_tr) + '\t' + str(sum_red_tftobal) + '\t' + str(sum_red_tftocard) + '\t')
    date_sum_all.write(str(sum_cat1) + '\t' + str(sum_cat2) + '\t' + str(sum_cat3) + '\t' + str(sum_cat4) + '\n')
    time2 = time.time()
    
    print '日期：',
    print '总购买金额：', sum_pur_total
    print '总赎回金额：', sum_red_total
    print '计算花费时间:',time2-time1
    
    usr_data.close()
