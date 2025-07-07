"""
This module provides a standardized way to authenticate with the OpenSilex API
and initialize a configured client.

It centralizes the authentication logic, making it easy to reuse the API client
across different parts of an application. This module uses a username and
password to fetch a temporary access token, which is the recommended and
more secure approach.

It also includes an optional interactive mode to select the API host from your
SSH config file.

General Usage Pattern:
1. Import the setup function from this module.
   `from api_connection import authenticate_and_get_client`
   `from openapi_client.api import YourApiClass`
   `from openapi_client.exceptions import ApiException`

2. Call `authenticate_and_get_client()` to get an authenticated ApiClient.
   For interactive host selection: `authenticate_and_get_client(interactive_host_selection=True)`
   `api_client = authenticate_and_get_client()`
   
3. If the client is successfully created, proceed with your API calls.
   `if api_client:`
   `    api_instance = YourApiClass(api_client)`
   `    # ... make your calls`
"""

import openapi_client
from openapi_client.api import AuthenticationApi
from openapi_client.models import AuthenticationDTO
from openapi_client.exceptions import ApiException
from get_host import SSHConfigParser # Import the SSH config parser

# --- Configuration ---
# TODO: Replace these placeholder values with your actual API host and credentials.
# This is the default host. It can be overridden with interactive selection.
API_HOST = "http://20.86.69.55:28081/rest"
API_USER = "admin@opensilex.org"
API_PASSWORD = "admin"


def authenticate_and_get_client(interactive_host_selection=False):
    """
    Authenticates with the API using credentials and returns a configured client.

    This function performs a two-step process:
    1. Creates a temporary client to call the authentication endpoint.
    2. If authentication is successful, it uses the received token to create
       a second, fully authenticated client for subsequent API calls.

    Args:
        interactive_host_selection (bool): If True, prompts the user to select
                                           a host from their ~/.ssh/config file.

    Returns:
        openapi_client.ApiClient or None: An initialized and authenticated 
        API client if successful, otherwise None.
    """
    
    host_to_use = API_HOST
    if interactive_host_selection:
        print("--- Interactive Host Selection ---")
        try:
            parser = SSHConfigParser()
            selected_ip = parser.select_host_ip()
            if selected_ip:
                host_to_use = f"http://{selected_ip}/rest"
                print(f"Using selected host: {host_to_use}")
            else:
                print("No host selected or found. Falling back to default host.")
        except FileNotFoundError:
            print("SSH config file not found. Falling back to default host.")
        except Exception as e:
            print(f"An error occurred during host selection: {e}. Falling back to default host.")
        print("---------------------------------")


    # Step 1: Create a basic, unauthenticated client for the login request.
    unauthenticated_config = openapi_client.Configuration(host=host_to_use)
    unauthenticated_client = openapi_client.ApiClient(unauthenticated_config)
    
    auth_api = AuthenticationApi(unauthenticated_client)
    
    print(f"Attempting to authenticate user '{API_USER}' at host: {host_to_use}")

    try:
        # Step 2: Call the authenticate endpoint with user credentials.
        auth_dto = AuthenticationDTO(identifier=API_USER, password=API_PASSWORD)
        
        # The authenticate method returns a TokenGetDTO
        token_dto = auth_api.authenticate(body=auth_dto)
        
        access_token = token_dto.token
        print("Successfully authenticated and received access token.")

        # Step 3: Create a new configuration with the received bearer token.
        authenticated_config = openapi_client.Configuration(
            host=host_to_use,
            access_token=access_token
        )

        # Step 4: Create and return the fully authenticated client.
        authenticated_client = openapi_client.ApiClient(authenticated_config)
        return authenticated_client, access_token

    except ApiException as e:
        print(f"Authentication failed: {e.reason} (Status: {e.status})")
        if "not found" in str(e.body).lower():
            print("Hint: The API host might be incorrect or the service isn't running.")
        print(f"Body: {e.body}")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred during authentication: {e}")
        return None, None

def main():
    """
    An example demonstrating how to use the authenticate_and_get_client function
    to connect to the API and make a simple call.
    
    This example runs in interactive mode.
    """
    print("--- Running API Connection Example ---")
    
    # 1. Get the authenticated API client using interactive host selection.
    #    Set to False to use the default API_HOST from the config section.
    api_client = authenticate_and_get_client(interactive_host_selection=True)
    print("API Client created successfully." if api_client else "Failed to create API Client.")
    print("\n--- Example Finished ---")


if __name__ == "__main__":
    main()

