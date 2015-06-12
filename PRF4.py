usr_balance = open ('user_balance_table1.csv', 'r')
AfterApril = open('AfterApril.csv', 'a')

line_no = 1
batch_limit = 100000
batch_no = 1

for line in user_balance:
  if True:
    if batch == batch_limit:
      print 'a new batch of data start outputing\n'
      batch = 1
      AfterApril.close()
      AfterApril = open('AfterApril.csv', 'a')
    else:
      batch = batch + 1
      
    line = line.split(',')
    if int(line[1]) >= 20140401:
      sep = ','
      new_line =sep.join(line)
      AfterApril.write(new_line)
      line_no = line_no + 1
      print str(line_no)
      
user_balance.close()
