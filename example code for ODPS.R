library('forecast')

# 读入purchase的数据，处理为时序对象
data<-read.csv("D:/alipay/sample_train_data.txt")
ts1<-ts(data, start=0, frequency=7)
print (ts1)

# 读入purchase的特征，处理为 data.frame 对象
f<-read.csv("D:/alipay/sample_train_feature.txt")
f1 <- f[[1]]
f2 <- f[[2]]
feature_frame <- data.frame(f1, f2)
print (feature_frame)


# 进行模型训练
arima_model <- auto.arima(ts1, max.p=20, max.q=20, d=2, trace=T, xreg=feature_frame)
# arima_model <- auto.arima(ts1, max.p=20, max.q=20, d=2, trace=T)


# 读入待预测日期的特征，处理为 data.frame 对象
ftest<-read.csv("D:/alipay/sample_test_feature.txt")
ftest1 <- ftest[[1]]
ftest2 <- ftest[[2]]
feature_test_frame <- data.frame(ftest1 , ftest2 )
print (feature_test_frame)


# 进行未来30天的预测, 这里的h参数可以不设置，因为forecast函数如果带有xreg参数
# 是根据xreg参数的长度来进行预测的
p_predict <- forecast(arima_model, xreg=feature_test_frame)


# 打印和plot来看看
plot(p_predict)
print(p_predict$mean)
