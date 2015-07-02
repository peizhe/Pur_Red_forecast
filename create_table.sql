drop table if exists daily_purchase_redeem;
create table if not exists daily_purchase_redeem
(
    report_date string,
    purchase    bigint,
    redeem      bigint
);
insert overwrite table daily_purchase_redeem
select report_date, sum(total_purchase_amt), sum(total_redeem_amt)
from tianchi_test.user_balance_table
group by report_date
order by report_date
limit 10000
