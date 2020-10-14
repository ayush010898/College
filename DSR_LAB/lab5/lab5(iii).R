getwd()
setwd("C:/Users/ayush/OneDrive/Desktop/college/7th sem/DSR/DSR Lab/R files")
bk<-read.csv("Churn_Modelling.csv")
bk
nrow(bk)
colnames(bk)
class(bk)
str(bk)
bk$EstimatedSalary
min(bk$EstimatedSalary)
max(bk$EstimatedSalary)
income_group<-vector(mode="character",length=length(bk$EstimatedSalary))
income_group
income_group[bk$EstimatedSalary<10000]<-"Low"
income_group
income_group[bk$EstimatedSalary>=10000 & bk$EstimatedSalary < 100000]<-"middle"
income_group[bk$EstimatedSalary>100000]<-"High"
income_group
spender<-factor(income_group,levels=c("Low","middle","High"),ordered=TRUE)
spender
bk<-cbind(bk,spender)
bk
str(bk$spender)
head(bk$spender)
head(bk)
tail(bk)
bk$spender
bk[1:6,]
bk[1:10,]
write.csv(bk,'exportNewData.csv',row.names = FALSE)

