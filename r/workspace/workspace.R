library(azuremlsdk)

ws_name <- "rimiworkshop"
ws_subscription_id <- "<subscriptionId>"
ws_resource_group <- "rimi"
ws_location <- "westeurope"

ws <- create_workspace(
  name = ws_name,
  subscription_id = ws_subscription_id,
  resource_group = ws_resource_group,
  location = ws_location,
  create_resource_group = TRUE,
)

write_workspace_config(path = "../../", file_name = "ws_config.json")

new_ws <- load_workspace_from_config(path = "../../", file_name = "ws_config.json")
