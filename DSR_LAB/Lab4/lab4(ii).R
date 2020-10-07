getwd()
setwd("C:/Users/ayush/OneDrive/Desktop/college/7th sem/DSR/DSR Lab/R files")
dataset<-read.delim("bank-data.csv",sep=',')
dataset
head(dataset)
summary(dataset)
colnames((dataset))
ncol(dataset)
nrow(dataset)
str(dataset)
numbers<-seq(1,600)
numbers
new_dataset<-cbind(dataset,numbers)
new_dataset
colnames(new_dataset)
write.csv(new_dataset,'exportData.csv',row.names = FALSE)
