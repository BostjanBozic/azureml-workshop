# Prepare AzureML CLI for private preview
```
export AZURE_ML_CLI_PRIVATE_FEATURES_ENABLED="true"
```

# Run commands
```
az ml data create -f data.yml
az ml component create -f train.yml
az ml component create -f score.yml
az ml component create -f eval.yml
az ml job create -f pipeline.yml
```
