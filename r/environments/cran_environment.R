library(azuremlsdk)

ws <- load_workspace_from_config(path = "../../")

cran_pkg1 <- cran_package("ggplot2", version = "3.3.0")
cran_pkg2 <- cran_package("stringr")
cran_pkg3 <- cran_package(
  name = "adagio",
  version = "0.8.4",
  repo = "http://cran.us.r-project.org"
)

env <- r_environment(
  name = "cran-environment",
  r_version = "3.6.0",
  cran_packages = list(cran_pkg1, cran_pkg2, cran_pkg3)
)

register_environment(
  environment = env,
  workspace = ws
)
