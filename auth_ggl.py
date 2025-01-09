import os
from google.oauth2 import service_account
import google.auth.transport.requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Expand tilde to the user's home directory
ENV_VAR_FILE = os.path.expanduser(os.path.join("~/gpt_engineer/", os.getenv("ENV_VAR_FILE")))
print("Env var file: ", ENV_VAR_FILE)

ENV_VAR_NAME = os.getenv("ENV_VAR_NAME")
print("Env var name: ", ENV_VAR_NAME)

SCOPES = ["https://www.googleapis.com/auth/generative-language"]
SERVICE_ACCOUNT_FILE_PATH = os.path.expanduser(
    os.path.join("~/gpt_engineer/", os.getenv("SERVICE_ACCOUNT_JSON_CREDENTIALS_PATH"))
)
print(SERVICE_ACCOUNT_FILE_PATH)

# Authenticate with service account
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE_PATH, scopes=SCOPES
)

auth_request = google.auth.transport.requests.Request()
credentials.refresh(auth_request)
print("Access Token:", credentials.token)


def update_env_var(file_path, var_name, new_value, add_if_missing=True):
    """
    Updates the value of an environment variable in a .env file.

    Parameters:
        file_path (str): Path to the .env file.
        var_name (str): Name of the environment variable to update.
        new_value (str): New value for the environment variable.
        add_if_missing (bool): If True, adds the variable if it doesn't exist.

    Returns:
        bool: True if the variable was updated or added, False otherwise.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        updated = False
        for i, line in enumerate(lines):
            if line.strip().startswith(f"{var_name}="):
                lines[i] = f"{var_name}={new_value}\n"
                updated = True
                break

        if not updated and add_if_missing:
            lines.append(f"{var_name}={new_value}\n")
            updated = True

        with open(file_path, 'w') as file:
            file.writelines(lines)
            return updated

    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


if update_env_var(ENV_VAR_FILE, ENV_VAR_NAME, credentials.token):
    print(f"Successfully updated {ENV_VAR_NAME} in {ENV_VAR_FILE} with value ************** etc...")
else:
    print(f"Failed to update {ENV_VAR_NAME} in {ENV_VAR_FILE}.")
