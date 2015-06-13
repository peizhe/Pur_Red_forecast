library(TTR)
library(forecast)
setwd("D:/Program File/R")
ls()
pur <- scan("pur.txt")

plot.ts(pur)
log_pur <- log(pur)
pur_timeseries <- ts(log_pur, frequency=7, start=c(1,1))

pur_forecasts <- HoltWinters(pur_timeseries)
pur_forecasts2 <- forecast.HoltWinters(pur_forecasts, h=35)
