### Section 6.2 Linear Regression

### Create a control function that will be used across models. We
### create the fold assignments explicitly instead of relying on the
### random number seed being set to identical values.

set.seed(100)
indx <- createFolds(solTrainY, returnTrain = TRUE)
ctrl <- trainControl(method = "cv", index = indx)

################################################################################
### Section 6.3 Partial Least Squares

## Run PLS and PCR on solubility data and compare results
set.seed(100)
plsTune <- train(x = solTrainXtrans, y = solTrainY,
                 method = "pls",
                 tuneGrid = expand.grid(ncomp = 1:20),
                 trControl = ctrl)
plsTune
plot(plsTune)

pcrTune <- train(x = solTrainXtrans, y = solTrainY,
                 method = "pcr",
                 tuneGrid = expand.grid(ncomp = 1:208),
                 trControl = ctrl)
pcrTune

A = matrix( 
     c(2, 4, 3, 1, 5, 7,1,1,1), # the data elements 
     nrow=3,              # number of rows 
     ncol=3,              # number of columns 
     byrow = TRUE)        # fill matrix by rows
Y = matrix( 
  c(2, 4, 3), # the data elements 
  nrow=3,              # number of rows 
  ncol=1,              # number of columns 
  byrow = TRUE)        # fill matrix by rows
t(A)
solve(A)

#(Xtrans * x ) _1 *X trans * Y
xa <- as.matrix(solTrainXtrans)

##y <- as.matrix(solTrainY)
beta <- solve(t(xa)%*%xa) %*% t(xa) %*% y
##beta
U <- matrix(1,951,1)
##U
x<- cbind(U,xa)


x[1:10,1:10]

ya <- xa%*%beta
testx_matrix = as.matrix(solTestX)
yt <- testx_matrix%*%beta
solTestY - yt