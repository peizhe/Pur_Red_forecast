## 天猫大数据竞赛——资金流入流出预测
###竞赛过程中的项目代码以及挖掘到的信息。
　　核心是进行时间序列分析.
**datasets：**<br>
####AfterApril_user_balance_table.txt: 从原始数据中截取4月份以后数据
####date_sort.txt: 将训练集中数据的采集日期排序<br>
DATE<br>
20130701<br>
20130702<br>
####date_times_usr.txt:每天余额宝中记录的申购、赎回次数
USR_NO：操作人数；PUR：申购次数；USR_NO_PUR：申购人次；RED：赎回次数；USR_NO_RED：赎回人次；RED_PUR：同时申购赎回次数；USR_NO_RED_PUR：同时操作人次
DATE　 TIMES　 USR_NO　 PUR　USR_NO_PUR 　RED　 USR_NO_RED 　RED_PUR 　USR_NO_RED_PUR<br>
20130701 　407 　407　 299 　299 　29 　29 　26 　26<br>
####usr.balance_table.csv:全部的原始数据
####usr.csv: 每个ID号在整个时期被记录次数
ID　TIMES<br>
1　103<br>
2　1<br>


##Tianchi 2015 golden league——The Purchase and Redemption Forecasts
**Introduction**<br>
　　Ant Financial Services Group (AFSG) processes cash inflow and outflow for millions of its members. As one can imagine, predicting future cash flows based on historical data is an important part of AFSG's business. Participants will be challenged to predict future cash flows based on users' historical purchase and redemption data to help Ant Financial Services Group (AFSG) improve its funds management abilities. (Purchases refers to funds inflow, while redemptions refers to funds outflow.)<br>
　　This repository is used to store the source code for data analysis and important information obtained during data mining.<br>
　　The core of the model is to perform time-series analysis, including expotianal smoothing, ARIMA(AutoRegression Integrated Moving average )
　　
