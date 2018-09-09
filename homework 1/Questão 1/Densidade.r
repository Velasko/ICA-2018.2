
library(mlbench)
library(e1071)
library(ggplot2)
library(reshape2)
data("Glass")
ggplot(Glass, aes(x = Type, fill = Type)) + geom_density()
