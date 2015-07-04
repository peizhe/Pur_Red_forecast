--日申购赎回汇总表
create table if not exists lt_user_balance_table_sum_baseline(
     report_date string comment '日期'
    ,total_purchase_amt bigint comment '日申购总额'
    ,total_redeem_amt bigint comment '日赎回总额'
) comment '日申购赎回汇总表' partitioned by (ds string);--ds：不同的分区，不同的时间区间。
insert overwrite table lt_user_balance_table_sum_baseline partition(ds='all')
select   report_date
        ,sum(total_purchase_amt) total_purchase_amt
        ,sum(total_redeem_amt) total_redeem_amt
from tianchi_test.user_balance_table --内部赛主办方提供的申购赎回记录表。
group by report_date;
--例如要用4-8月数据作为训练集
insert overwrite table  lt_user_balance_table_sum_baseline partition(ds='45678month')
select   report_date
        ,total_purchase_amt
        ,total_redeem_amt
from lt_user_balance_table_sum_baseline
where ds = 'all' and report_date >='20140401' and report_date < '20140901';

--构建训练集基础特征：
create table if not exists  lt_basic_feature4to8_baseline as 
select   t1.report_date
        ,case when t1.dayOfWeek=0 then  1 else 0 end as monday
        ,case when t1.dayOfWeek=1 then  1 else 0 end as tuesday 
        ,case when t1.dayOfWeek=2 then  1 else 0 end as wednesday
        ,case when t1.dayOfWeek=3 then  1 else 0 end as thursday
        ,case when t1.dayOfWeek=4 then  1 else 0 end as friday
        ,case when t1.dayOfWeek=5 then  1 else 0 end as saturday
        ,case when t1.dayOfWeek=6 then  1 else 0 end as sunday
        ,total_purchase_amt
        ,total_redeem_amt
from (
    select report_date
         ,weekday(to_date(report_date,"yyyyMMdd")) dayOfWeek
         ,total_purchase_amt
         ,total_redeem_amt
    from lt_user_balance_table_sum_baseline
    where ds = '45678month' 
) t1;
--构建线上基础特征：
create table if not exists  lt_basic_feature9_baseline as 
select   t1.report_date
        ,case when t1.dayOfWeek=0 then  1 else 0 end as monday
        ,case when t1.dayOfWeek=1 then  1 else 0 end as tuesday 
        ,case when t1.dayOfWeek=2 then  1 else 0 end as wednesday
        ,case when t1.dayOfWeek=3 then  1 else 0 end as thursday
        ,case when t1.dayOfWeek=4 then  1 else 0 end as friday
        ,case when t1.dayOfWeek=5 then  1 else 0 end as saturday
        ,case when t1.dayOfWeek=6 then  1 else 0 end as sunday
from (
    select report_date
         ,weekday(to_date(report_date,"yyyyMMdd")) dayOfWeek
    from lt_predict_day9month_baseline --9月份日期数据可以通过R脚本上传。
) t1;
