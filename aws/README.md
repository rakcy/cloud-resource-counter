# Instructions

## Install Dependencies
Install dependencies by running the following command 
```
pip install -r ./requirements.txt
```

## Running the Script
There are 2 ways to run the script.

1. If you are using an aws profile, you can run the command by passing in the profile name.
    ```
    python count_resources.py --profile <profile>
    ```

2. If you are using an access key pair, you can run the command by passing them in as parameters.
    ```
    python count_resources.py --access <aws_access_key_id> --secret <aws_secret_access_key>
    ```

Run the script once for each AWS Account. Everytime the script is run, a csv file will be generated in the same folder with the name format `<aws_account_number>-<YYYYMMDD-HHMMSS>.csv`
