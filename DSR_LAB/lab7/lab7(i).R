library(gcookbook)
df = cabbage_exp
head(df)
barplot(Weight ~ Cultivar+Date, data=df, xlab = "Date", ylab = "weight", beside=TRUE, legend = TRUE,col =c("black","grey"))
