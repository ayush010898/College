library(ggplot2)
dotchart(mtcars$mpg, labels = row.names(mtcars),cex = 0.6, xlab = "mpg")
