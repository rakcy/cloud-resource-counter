# Instructions

## Install Dependencies
Install dependencies by running the following command 
```
pip3 install -r ./requirements.txt
```

## Prerequisities

### Azure CLI
You will have to install [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli), which is used for authentication prior to running the resource counter script.

### Azure Permissions
The script uses the Azure Resource Graph to query for resources. As a user, you must have at least read access to the resources you want to query. 
Without at least read permissions to the Azure object or object group, results won't be returned.

We recommend having at least the `Reader` role for all relevant subscriptions.

## Running the Script
First, log into Azure by running the command
```
az login
```
This will open up a web browser prompting you to login to your Azure Domain. Log in to complete the authentication process.

Next, run the script with the command
```
python ./count_resources.py
```

Everytime the script is run, a csv file will be generated in the same folder with the name format `azure-resources-<YYYYMMDD-HHMMSS>.csv`
