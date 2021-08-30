library(jsonlite)

init <- function() {
  model_path <- Sys.getenv("AZUREML_MODEL_DIR")
  model <- readRDS(file.path(model_path, "model.rds"))
  message("logistic regression model loaded")

  function(data) {
    vars <- as.data.frame(jsonlite::fromJSON(data))
    prediction <- as.numeric(predict(model, vars, type = "response") * 100)
    jsonlite::toJSON(prediction)
  }
}
