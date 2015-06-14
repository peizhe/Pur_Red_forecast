## 天猫大数据竞赛——资金流入流出预测
###竞赛过程中的项目代码以及挖掘到的信息。
　　核心是进行时间序列分析.
**datasets：**<br>
####AfterApril_user_balance_table.txt: 从原始数据中截取4月份以后数据

####date_red_pur.txt:每天申购赎回总额
DATE　SUM_PUR　SUM_RED

####date_sort.txt: 将训练集中数据的采集日期排序
DATE<br>
20130701<br>
20130702<br>

####date_sum_all.txt:每日各统计分项汇总
DATE　 sum_pur_total　sum_red_total　sum_pur_direct　sum_pur_bal　sum_pur_bank　sum_share　sum_red_con　sum_red_tr　sum_red_tftobal　sum_red_tftocard　sum_cat1　sum_cat2　sum_cat3　sum_cat4 

####date_times_usr.txt:每天余额宝中记录的申购、赎回次数
USR_NO：操作人数；PUR：申购次数；USR_NO_PUR：申购人次；RED：赎回次数；USR_NO_RED：赎回人次；RED_PUR：同时申购赎回次数；USR_NO_RED_PUR：同时操作人次<br>
DATE　 TIMES　 USR_NO　 PUR　USR_NO_PUR 　RED　 USR_NO_RED 　RED_PUR 　USR_NO_RED_PUR<br>
20130701 　407 　407　　299   　299 　    29 　     29 　       26 　         26<br>

####usr.balance_table.csv:全部的原始数据

####usr_times.csv:April以后，超过5次操作的每位用户的操作次数和余额变化范围
USR_ID　TIMES　MAX_T_BALANCE　MIN_T_BALANCE<br>
<br>
####usr.csv: 每个ID号在整个时期被记录次数
ID　TIMES<br>
1　103<br>
2　1<br>


##Tianchi 2015 golden league——The Purchase and Redemption Forecasts
**Introduction**<br>
　　Ant Financial Services Group (AFSG) processes cash inflow and outflow for millions of its members. As one can imagine, predicting future cash flows based on historical data is an important part of AFSG's business. Participants will be challenged to predict future cash flows based on users' historical purchase and redemption data to help Ant Financial Services Group (AFSG) improve its funds management abilities. (Purchases refers to funds inflow, while redemptions refers to funds outflow.)<br>
　　This repository is used to store the source code for data analysis and important information obtained during data mining.<br>
　　The core of the model is to perform time-series analysis, including expotianal smoothing, ARIMA(AutoRegression Integrated Moving average )
　　
