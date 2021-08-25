# Azure Machine Learning with Python and R 

This repository includes sample code how to interact with Azure Machine Learning using either Python or R SDK.

## Prerequisites

### Python

For running all available samples, following packages have to be installed:
* azureml-core
* azureml-pipeline
* azureml-dataset-runtime

All samples are available under `python` directory.

### R

Communicating with Azure Machine Learning using R SDK requires installation of R package from CRAN and AzureML Python SDK compiled code. This can be set using following commands:
* Install Azure ML SDK from CRAN: `install.packages("azuremlsdk")`
* Install compiled code from AzureML Python SDK: `azuremlsdk::install_azureml()`

All samples are available under `r` directory. Those samples include similar examples to Python examples, excluding Pipelines, which are not available in R SDK.

Due to current issue with installing `r-essentials` package in Azure Machine Learning container images, custom image has to be built using Azure Container Registry and used within all experiment samples (image is reused for every sample, you do not have to build it every time). Help script is provided under `r/environments/dockerfile_env.sh`:
* review `Dockerfile` in same directory and adjust it if required
* adjust `WORKSPACE` and `RESOURCE_GROUP` variable
* run script

Every experiment `run_script.R` includes environment creation. Just update `custom_docker_image` parameter to point to newly generated image.

## Usage

Before running any samples, `config.json` file has to be configured in root directory of repository. This file can be downloaded directly from Azure Machine Learning workspace (click on your account and follow `Download config file`) or created manually using following structure:
```
{
  "subscription_id": "<subscriptionId>",
  "resource_group": "<resourceGroupName>",
  "workspace_name": "<workspaceName>"
}
```

For running provided samples, simply navigate to them and run following:
* python: `python <script_name>`
* R: `RScript <script_name>`

Some samples work with data. Be sure to check README under those samples to download the files locally.
