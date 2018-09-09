library(mlbench)
data("Glass")
#install.packages("corrplot")
library(corrplot)
attach(Glass)
pairs(dta,panels = points, col = dta$Type.of.glass,pch=16)
correlation <- cor(dta)
corrplot(correlation, order = "hclust")

