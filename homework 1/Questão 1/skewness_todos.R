library(mlbench)
library(e1071)
library(ggplot2)
library(reshape2)
data("Glass")
vetor_todos = c(Glass$RI,Glass$Na,Glass$Mg,Glass$Al,Glass$Si,Glass$K,Glass$Ca,Glass$Ba,Glass$Fe)
vetor_skewness = c(skewness(vetor_todos)) 
vetor_skewness