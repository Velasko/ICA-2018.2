library(mlbench)
data("Glass")
library(gclus)
dta <- Glass[c(1,2,3,4,5,6,7,8,9)] # get data
dta.r <- abs(cor(dta)) # get correlations
dta.col <- dmat.color(dta.r) # get colors
dta.o <- order.single(dta.r)
cpairs(dta, dta.o, panel.colors=dta.col, gap=.5,
       main="Variáveis ordenadas e coloridas por correlação" )

