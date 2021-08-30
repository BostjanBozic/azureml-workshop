#! /bin/bash

IMAGE_NAME="r-azureml"
IMAGE_TAG="0.0.1"

WORKSPACE="rimiworkshop"
RESOURCE_GROUP="rimi"

REGISTRY_NAME=$(az ml workspace show -w ${WORKSPACE} -g ${RESOURCE_GROUP} | jq -r .container_registry | sed 's/.*\///')

az acr login --name ${REGISTRY_NAME}

az acr build -t ${IMAGE_NAME}:${IMAGE_TAG} -t ${IMAGE_NAME}:latest --registry ${REGISTRY_NAME} --file Dockerfile .
