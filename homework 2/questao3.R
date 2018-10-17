installed.packages("pls")
library(pls)
#PLS com C-V usando k = 10
ctrl <- trainControl(method = "cv", number = 10)
set.seed(100)
plsTune <- train(solTrainXtrans , solTrainY ,method = "pls",
                 tuneGrid = expand.grid(ncomp= 1:30),trControl = ctrl ,
                 preProc = c("center", "scale"))
plsTune

plsPredict1 <- predict(plsTune, solTestXtrans
                       ,ncomp=21)
plsValores1<- data.frame(pred=plsPredict1,
                         obs= solTestY)

#mostrando os valores do RMSE, R2 e MAE (Mean Absolute Error) da predicao com o solTestXtrans
defaultSummary(plsValores1)
