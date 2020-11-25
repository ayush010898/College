temp <- c(50,53,54,55,56,59,62,65,67,71,72,74,75,76,79)
yield <- c(122,118,128,121,125,136,144,142,149,161,167,168,162,171,175)
df<-data.frame(temp,yield)
head(df)

linear <- lm(yield~temp, data=df)
summary(linear)
names(linear)
linear$coefficients
plot(df$temp,df$yield,col="red")
abline(lm(yield ~ temp),col="red")
plot(linear,which=1)
fitted(linear)