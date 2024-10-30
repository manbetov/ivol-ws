import os
from dotenv import load_dotenv
import json

# Load environment variables from the credentials file
load_dotenv('credentials.env')

# Retrieve the values of the environment variables
ivolApiKey = os.getenv('ivolApiKey')
ivolUserName = os.getenv('ivolUserName')
ivolUserPassword = os.getenv('ivolUserPassword')

# Create an object for the Thunder Client environment
environment = {
    "name": "My Thunder Client Environment",
    "variables": [
        {"key": "ivolApiKey", "value": ivolApiKey, "enabled": True},
        {"key": "ivolUserName", "value": ivolUserName, "enabled": True},
        {"key": "ivolUserPassword", "value": ivolUserPassword, "enabled": True}
    ],
    "_id": "your_unique_id_here"  # You can replace this with any unique identifier
}

# Write the environment to a JSON file
environment_file = 'thunder_client_environment.json'
with open(environment_file, 'w') as json_file:
    json.dump(environment, json_file, indent=4)

print(f"Environment successfully generated and saved to {environment_file}.")
print("To import this environment into Thunder Client:")
print("1. Open Thunder Client in Visual Studio Code.")
print("2. Go to the 'Environments' section.")
print("3. Click on 'Import' and select the file: thunder_client_environment.json")
print("4. Your environment will now be available for use in requests.")