#-*-utf-8-*-
#!/usr/bin/env python

usrID = open('usr.txt','r')

usr_list = []
for line in usrID:
    usr = line.split('\t')
    usr_list.append(int(usr[0]))

usrID.close()

print len(usr_list)

for usr_ID in usr_list:
    times = 0
    t_balance_list = []
    
    usr_data = open('AfterApril_user_balance_table.txt','r')

    for line in usr_data:
        usr_info = line.split(',')
        if int(usr_info[0]) == usr_ID:
            times = times + 1
            t_balance_list.append(int(usr_info[2]))
            
    
    usr_data.close()

    if len(t_balance_list) != 0:
        t_balance_max = max(t_balance_list)
        t_balance_min = min(t_balance_list)
        if times > 5:
            print str(usr_ID)+'\t' + str(times) + '\t' + str(t_balance_max) + '\t' + str(t_balance_min)

            usr_times = open('usr_times.txt.','a')

            usr_times.write(str(usr_ID)+'\t' + str(times) + '\t' + str(t_balance_max) + '\t' + str(t_balance_min) + '\n')

            usr_times.close()


