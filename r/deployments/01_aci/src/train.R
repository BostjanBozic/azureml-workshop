library(azuremlsdk)
library(DAAG)

data(nassCDS)

accidents <- na.omit(nassCDS[,c("dead","dvcat","seatbelt","frontal","sex","ageOFocc","yearVeh","airbag","occRole")]) # nolint
accidents$frontal <- factor(accidents$frontal, labels = c("notfrontal","frontal")) #nolint
accidents$occRole <- factor(accidents$occRole) # nolint
summary(accidents)

mod <- glm(dead ~ dvcat + seatbelt + frontal + sex + ageOFocc + yearVeh + airbag  + occRole, family=binomial, data=accidents) # nolint
summary(mod)
predictions <- factor(ifelse(predict(mod) > 0.1, "dead", "alive"))
accuracy <- mean(predictions == accidents$dead)
log_metric_to_run("Accuracy", accuracy)

output_dir <- "outputs"
if (!dir.exists(output_dir)) {
  dir.create(output_dir)
}
saveRDS(mod, file = "./outputs/model.rds")
message("Model saved")
