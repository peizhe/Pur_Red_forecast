天猫大数据竞赛——资金流入流出预测
---


竞赛过程中挖掘到的信息及决赛注意事项
---
**模型选择**<br>
1. ARIMA (HW)+ LM 预测整月的数据<br>
2. 对一些特征点进行调优 (中秋，调休，国庆前)<br>

决赛相对之前的升级：<br>
模型方面主要是增加了数据预处理 和 线性模型中的特征；<br>
特殊时间点方面，主要是更好的刻画了月初、月末的特征.<br>

**关于评测**<br>
1. 如果评测机会比较充足，了解一下自己的purchase得分和redeem得分对后续方向的指导意义比较大，purchase由于比较稳定，所以得分应该更高；而redeem会因为波动比较大，预测难一些;<br>
2. 不要迷信用八月份的数据做线下评测得到的效果，八月份数据略坑，及早从坑里爬出来.一般来说;<br>
3. 评估函数不是线性的，越准确上分速度越快，加入一些小幅的噪声有可能能够提高成绩；<br>

**基本流程**<br>
1. 需要对整体数据做一个处理，比如数据预处理、分解、汇总，这个正好使用*ODPS*，语法同HIVE，可以查HIVE的语法手册<br>
2. 汇总每日的申购、赎回数据分别放到表A 和 B中，然后用PAI平台的R脚本读取这两张表，做时间序列分析，或者回归，分别输出到结果C 和 D中；<br>
3. 单点调优后，替换C 和 D中的某些日期的数据，然后合并结果到输出表E中<br>
注：用ARIMA中的XREG参数做 时间序列分析 + 线性回归。(example code)[https://github.com/chibaofang/Pur_Red_forecast/blob/master/example%20code%20for%20ODPS.R]


**PAI-R**<br>
到实验的页面下，新建一个实验，然后在画布上拖三个东西，一个是数据源，一个是R脚本，一个是数据目标。依次用线进行连接。大概变成这样:PICTURE  <br>
数据源需要把表A或者表B的名字填进去，然后R脚本自动会增加语句获取该表的输入；这是一个dataframe的数据结果，可以通过列名把数组形式的数据取出来。<br>
获取到数据之后，一般先转为一个时间序列的对象，然后调用模型，如ARIMA，decompose对时序进行处理，然后预测9月的数据。<br>
预测得到的数据，需要构造为一个dataframe的对象，然后赋值给一个叫dataname的变量，平台最终会自动把dataname中的数据，放到输出目标表中。<br>
这里有个小窍门，PAI上的R编辑起来不是很友好，其实平台上的R与本地的R是没有差别的，只有数据输入输出的差别；所以如果程序能够在本地跑通，拷贝到平台上，然后改一下输入输出就可以了。
当然，要是用了平台没有的R包，就比较麻烦了。
对于一个程序员来说，粗浅的了解一下R，所花费的学习成本并不高，不过R的资料毕竟没有其他热门语言那么多。特别是，如果脚本跑失败了，是没有错误提示信息的，所以本地跑通显得尤为重要。

**PAI-机器学习**
单点预测的话，能够挖掘出于当前点最相似的时间节点是比较有用的，可以用聚类方法来试一下。主要分两步:<br>
1. 构造特征，把特征放到数据表中<br>
2. 拖拽算法模块进行聚类<br>



阿里巴巴ODPS计算平台使用说明及注意事项
---
　　因为建模主要考虑回归分析和时间序列建模，所以对于算法平台模型主要可以考虑使用GBDT回归和R脚本，其中GBDT回归注意设置：DminLeafSampleCount，并且控制DmaxDepth、DtreeCount，防止过拟合，本身GBDT更适合于大数据量的情况。此外R脚本中提供很多R的相关包可以使用：包的引入方式：library("包名")，内部赛复赛时提供的R包主要有：<br>
```
ISOweek :日期处理
timeDate：时间处理
forecast :时间预测
RandomForest：随机森林
rpart：决策树
e1071：svm算法
tseries：时间序列
glmnet：线性回归
discretization：离散化
cluster：聚类
entropy：信息熵、互信息，用于特征选择。
reshape：数据矩阵整形
nnet：神经网络
```
R脚本必须至少有一个数据源（OPDS表），并且ODPS表在R脚本中是data.frame的形式。<br>
下面以构建baseline举例：<br>
1、算法平台，上传要预测的9月份30天的日期数据：可以通过R脚本以data.frame的形式写入到ODPS表中。（PS：test=c(20140901,20140902)默认元素类型是double而非int，所以需要在R中做as.integer(20140901)转换，此外必须制定一个ODPS源）<br>
```
# 请链接输入数据
# 链接完成后，系统会自动生成映射代码，将输入数据映射成变量参数，用户可直接使用
# 切记不可修改系统生成代码，否则运行将报错
#端口1的表数据映射成dataset1
dataset1 <- pai.inputPort(1) # class: data.frame
report_date = c(  
    as.integer(20140901)
, as.integer(20140902)
, as.integer(20140903)
, as.integer(20140904)
, as.integer(20140905)
, as.integer(20140906)
, as.integer(20140907)
, as.integer(20140908)
, as.integer(20140909)
, as.integer(20140910)
, as.integer(20140911)
, as.integer(20140912)
, as.integer(20140913)
, as.integer(20140914)
, as.integer(20140915)
, as.integer(20140916)
, as.integer(20140917)
, as.integer(20140918)
, as.integer(20140919)
, as.integer(20140920)
, as.integer(20140921)
, as.integer(20140922)
, as.integer(20140923)
, as.integer(20140924)
, as.integer(20140925)
, as.integer(20140926)
, as.integer(20140927)
, as.integer(20140928)
, as.integer(20140929)
, as.integer(20140930)

                                  )
dataname = data.frame(report_date)
# 用户指定数据变量dataname(class:data.frame)到输出端口
# 平台会将该数据生成ODPS表
# dataname务必修改成自己的变量名称
pai.outputPort(1, dataname)
```
2、开发平台,使用ODPS SQL构建特征（初级特征仅供参考）:
```
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
```
3、算法平台，训练模型并预测：这里使用R脚本的lm做线性回归模型。
```
# 请链接输入数据
# 链接完成后，系统会自动生成映射代码，将输入数据映射成变量参数，用户可直接使用
# 切记不可修改系统生成代码，否则运行将报错
#端口2的表数据映射成dataset2
dataset2 <- pai.inputPort(2) # class: data.frame
#端口1的表数据映射成dataset1
dataset1 <- pai.inputPort(1) # class: data.frame

formulaStr = "total_purchase_amt~ monday+tuesday +wednesday + thursday+friday+saturday+sunday"
model = lm(as.formula(formulaStr),dataset1,interval="prediction")
dataname <-data.frame( predict(model,dataset2,interval = "prediction",level=0.95,se.fit=FALSE))
dataname$report_date = dataset2$report_date

# 用户指定数据变量dataname(class:data.frame)到输出端口
# 平台会将该数据生成ODPS表
# dataname务必修改成自己的变量名称
pai.outputPort(1, dataname)
```
R脚本训练并预测赎回：
```
# 请链接输入数据
# 链接完成后，系统会自动生成映射代码，将输入数据映射成变量参数，用户可直接使用
# 切记不可修改系统生成代码，否则运行将报错
#端口2的表数据映射成dataset2
dataset2 <- pai.inputPort(2) # class: data.frame
#端口1的表数据映射成dataset1
dataset1 <- pai.inputPort(1) # class: data.frame

formulaStr = "total_redeem_amt~ monday+tuesday +wednesday + thursday+friday+saturday+sunday"
model = lm(as.formula(formulaStr),dataset1,interval="prediction")
dataname <-data.frame( predict(model,dataset2,interval = "prediction",level=0.95,se.fit=FALSE))
dataname$report_date = dataset2$report_date

# 用户指定数据变量dataname(class:data.frame)到输出端口
# 平台会将该数据生成ODPS表
# dataname务必修改成自己的变量名称
pai.outputPort(1, dataname)
```
4、合并申购、赎回结果并提交:
```
--合并申购赎回结果并提交：
create table lt_baseline_commit as
select   t1.report_date
        ,cast(round(t1.fit,0) as bigint) purchase
        ,t2.redeem
from lt_basic_feature9_predict_purchase t1
join(
     select   report_date
            ,cast(round(fit,0) as bigint) redeem
    from lt_basic_feature9_predict_redeem
) t2
on t1.report_date = t2.report_date;

--提交结果到官方评测表：
insert overwrite table tc_comp_predict_table
select * from lt_baseline_commit;
--查看提交结果是否正确
select * from tc_comp_predict_table;
desc tc_comp_predict_table;
```









比赛过程中构建出的预处理数据集备注datasets：<br>
---
**成绩README.docx：记录每一次提交的数据的模型**<br>
**关键数据.xlsx ：内涵每一天每一单项的总额**<br>
**AfterApril_user_balance_table.txt: 从原始数据中截取4月份以后数据**<br>
**date_red_pur.txt:每天申购赎回总额**<br>
DATE　SUM_PUR　SUM_RED<br>

**date_sort.txt: 将训练集中数据的采集日期排序**<br>
DATE<br>
20130701<br>
20130702<br>

**date_sum_all.txt:每日各统计分项汇总**<br>
DATE　 sum_pur_total　sum_red_total　sum_pur_direct　sum_pur_bal　sum_pur_bank　sum_share　sum_red_con　sum_red_tr　sum_red_tftobal　sum_red_tftocard　sum_cat1　sum_cat2　sum_cat3　sum_cat4 <br>

**date_times_usr.txt:每天余额宝中记录的申购、赎回次数**<br>
USR_NO：操作人数；PUR：申购次数；USR_NO_PUR：申购人次；RED：赎回次数；USR_NO_RED：赎回人次；RED_PUR：同时申购赎回次数；USR_NO_RED_PUR：同时操作人次<br>
DATE　 TIMES　 USR_NO　 PUR　USR_NO_PUR 　RED　 USR_NO_RED 　RED_PUR 　USR_NO_RED_PUR<br>
20130701 　407 　407　　299   　299 　    29 　     29 　       26 　         26<br>

**usr.balance_table.csv:全部的原始数据**<br>

**usr_times.csv:April以后，超过5次操作的每位用户的操作次数和余额变化范围**<br>
USR_ID　TIMES　MAX_T_BALANCE　MIN_T_BALANCE<br>

**usr.csv: 每个ID号在整个时期被记录次数**<br>
ID　TIMES<br>
1　103<br>
2　1<br>


Tianchi 2015 golden league——The Purchase and Redemption Forecasts
---
**Introduction**<br>
　　Ant Financial Services Group (AFSG) processes cash inflow and outflow for millions of its members. As one can imagine, predicting future cash flows based on historical data is an important part of AFSG's business. Participants will be challenged to predict future cash flows based on users' historical purchase and redemption data to help Ant Financial Services Group (AFSG) improve its funds management abilities. (Purchases refers to funds inflow, while redemptions refers to funds outflow.)<br>
　　This repository is used to store the source code for data analysis and important information obtained during data mining.<br>
　　The core of the model is to perform time-series analysis, including expotianal smoothing, ARIMA(AutoRegression Integrated Moving average )
　　
