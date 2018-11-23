library(AppliedPredictiveModeling)
data(solubility)
library(caret)
library(lattice)
library(elasticnet)
library(MASS)
indx <- createFolds(solTrainY, returnTrain = TRUE)

##Treinando e validando o RidgeRegression model


ridgeModelo <- enet(x = as.matrix(solTrainXtrans), y=solTrainY, lambda = 0.001)
ridgePredict <- predict(ridgeModelo, newx = as.matrix(solTestXtrans), s=1, mode="fraction", type="fit")

#variavel de controle do trainin, Utilizando Cross-Validation
ctrl <- trainControl(method = "cv", number = 10)

#Modelo de RR usando a funcao train
#Necessitamos de um Grid
ridgeGrid <- data.frame(.lambda = seq(0, .1, length = 15))
set.seed(100)
ridgeRegFit <- train(solTrainXtrans, solTrainY,method = "ridge", tuneGrid = ridgeGrid,trControl = ctrl,preProc = c("center", "scale"))
ridgeRegFit

ridgePredict2 <- predict(ridgeRegFit, solTestXtrans)
ridgeValores2 <- data.frame(obs= solTestY,pred = ridgePred2)
#No summary temos o RMSE, R2 e O MAE (Mean Absolute Error)
defaultSummary(ridgeValores2)

plot(ridgeRegFit$results$lambda, ridgeRegFit$results$RMSE
     , xlab="Penalty", ylab="RMSE (C-V") 