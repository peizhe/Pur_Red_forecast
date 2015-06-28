creat table if not exists lt_usr_balance_table_sum_baseline（
  report_date string comment '日期'
  total_purchase_amt bigint comment '日申购总额'
  total_redeem_amt bigint comment '日赎回总额'
）comment '日申购赎回汇总表' partitioned by (ds string);  

inset overwrite table lt_usr_balance_table_sum_baseline partition(ds = 'all')

select report_date,
       sum(total_purchase_amt) total_purchase_amt,
       sum(total_redeem_amt) total_redeem_amt
from tianchi_test.user_balance_table  --内部赛主办方提供的申购赎回记录表。
group by report_date;

--例如需要4到8月份的数据作为训练集
