"""
Fill Website with Mock Data
"""
import os
import sys
import openapi_client
from openapi_client.api import authentication_api, organizations_api, projects_api, experiments_api, scientific_objects_api, devices_api
from openapi_client.models import AuthenticationDTO
from mock import MockClient
import argparse
from get_host import SSHConfigParser

def main():
    """
    Main function to fill the website with mock data.
    """
    parser = argparse.ArgumentParser(description="Fill website with mock data.")
    parser.add_argument("--host", help="The host of the OpenSilex API")
    args = parser.parse_args()

    host = args.host
    if not host:
        # Get base URL from SSH config
        try:
            ssh_parser = SSHConfigParser()
            host = ssh_parser.select_host_ip()
            if not host:
                print("No host selected. Exiting.")
                return
        except (ValueError, FileNotFoundError) as e:
            print(f"Error getting base URL: {e}")
            print("Please ensure your SSH config is set up correctly, or provide a host with the --host argument.")
            return

    # Initialize clients
    configuration = openapi_client.Configuration(host=host)
    api_client = openapi_client.ApiClient(configuration=configuration)
    mock_client = MockClient()

    # Authenticate
    print("Authenticating with default admin credentials...")
    auth_api = authentication_api.AuthenticationApi(api_client)
    auth_dto = AuthenticationDTO(identifier="admin@opensilex.org", password="admin")
    
    try:
        token_response = auth_api.authenticate(body=auth_dto)
        print(token_response)
        token = token_response.token
        api_client.set_default_header("Authorization", "Bearer " + token)
        print("Authentication successful.")
    except openapi_client.ApiException as e:
        print(f"Authentication failed: {e}")
        return

    org_api = organizations_api.OrganizationsApi(api_client)
    proj_api = projects_api.ProjectsApi(api_client)
    exp_api = experiments_api.ExperimentsApi(api_client)
    sci_obj_api = scientific_objects_api.ScientificObjectsApi(api_client)
    dev_api = devices_api.DevicesApi(api_client)

    # Create organizations
    print("\nCreating mock organizations...")
    mock_organizations = mock_client.create_mock_organizations(3)
    for org_data in mock_organizations:
        try:
            org_api.create_organization(body=org_data)
            print(f"  - Created organization: {org_data.name}")
        except openapi_client.ApiException as e:
            print(f"  - Failed to create organization: {org_data.name} ({e.body})")

    # Create projects, experiments, and scientific objects
    print("\nCreating mock projects, experiments, and scientific objects...")
    mock_projects = mock_client.create_mock_projects(2)
    for project_data in mock_projects:
        # Create project
        try:
            project_response = proj_api.create_project(body=project_data)
            project_uri = project_response.result[0]
            print(f"\n- Created project: {project_data.name}")

            # Create experiments for the project
            mock_experiments = mock_client.create_mock_experiments(2, project_uri)
            for exp_data in mock_experiments:
                try:
                    exp_response = exp_api.create_experiment(body=exp_data)
                    exp_uri = exp_response.result[0]
                    print(f"  - Created experiment: {exp_data.name}")

                    # Create scientific objects for the experiment
                    mock_objects = mock_client.create_mock_scientific_objects(5, exp_uri)
                    for obj_data in mock_objects:
                        try:
                            sci_obj_api.create_scientific_object(body=obj_data)
                            print(f"    - Created scientific object: {obj_data.name}")
                        except openapi_client.ApiException as e:
                            print(f"    - Failed to create scientific object: {obj_data.name} ({e.body})")
                except openapi_client.ApiException as e:
                    print(f"  - Failed to create experiment: {exp_data.name} ({e.body})")
        except openapi_client.ApiException as e:
            print(f"\n- Failed to create project: {project_data.name} ({e.body})")

    # Create devices
    print("\nCreating mock devices...")
    mock_devices = mock_client.create_mock_devices(4)
    for device_data in mock_devices:
        try:
            dev_api.create_device(body=device_data)
            print(f"  - Created device: {device_data.name}")
        except openapi_client.ApiException as e:
            print(f"  - Failed to create device: {device_data.name} ({e.body})")

    # Logout
    print("\nLogging out...")
    try:
        auth_api.logout(authorization="Bearer " + token)
        print("Done.")
    except openapi_client.ApiException as e:
        print(f"Logout failed: {e}")


if __name__ == "__main__":
    main()
