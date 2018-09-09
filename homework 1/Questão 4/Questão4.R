library(mlbench)
library(ggplot2)
library(ggfortify)
data(Glass)

par(mfrow = c(1,2))

PCA <- prcomp(Glass[,1:9], center = TRUE,scale. = TRUE)
plot(PCA)
autoplot(PCA, data= Glass, colour = 'Type', loadings = TRUE, 
         loadings.colour= 'red', loadings.labels = TRUE, loadings.label.size = 5)


