library(foreign)

##reading data
path_to_file = "survey_data/"
births_data <- read.dta(paste(path_to_file, "ZZBR62FL.DTA", sep=""))
couples_data <- read.dta(paste(path_to_file, "ZZCR61FL.DTA", sep=""))
household_data <- read.dta(paste(path_to_file, "ZZHR62FL.DTA", sep=""))
childrens_data  <- read.dta(paste(path_to_file,"ZZKR62FL.DTA", sep=""))
household_member_data <- read.dta(paste(path_to_file, "ZZPR62FL.DTA" , sep=""))


## processing data
births_data <- births_data[,colSums(is.na(births_data))<nrow(births_data)]
couples_data <- couples_data[,colSums(is.na(couples_data))<nrow(couples_data)]
household_data <- household_data[,colSums(is.na(household_data))<nrow(household_data)]
childrens_data <- childrens_data[,colSums(is.na(childrens_data))<nrow(childrens_data)]
household_member_data <- household_member_data[,colSums(is.na(household_member_data))<nrow(household_member_data)]


## write csv for python
write.csv(births_data, paste(path_to_file, "births.csv", sep=""))
write.csv(couples_data, paste(path_to_file, "couples.csv", sep=""))
write.csv(household_data, paste(path_to_file, "households.csv", sep=""))
write.csv(childrens_data, paste(path_to_file, "children.csv", sep=""))
write.csv(household_member_data, paste(path_to_file, "household_members.csv", sep=""))