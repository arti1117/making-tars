# This is comment

# Remove variables
rm(list=ls())

a<-c(1:10)
f<-factor(c(10:11))
f1<-factor("A", c("A", "B"))
gender<-factor("M", c("M", "F"))

comb<-stack(list(v1=c(1:5), v2=c(6:10), v3=c(11:15)))
