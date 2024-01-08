from shareplum import Site
from shareplum.site import Version
import requests
import streamlit as st
from requests_ntlm import HttpNtlmAuth

# SharePoint credentials
site_url = "https://bistecglobal.sharepoint.com"
client_id = "8e597d3d-4f9a-4a64-bf76-3d82e3625019"
client_secret = "dPW8Q~P4C3ZhLnTBcaHk6Necnc9O.e3RpOxcFb87"
tenant_id = "d5e769b0-fd19-45e4-a4a8-b73545450234"  # Replace with your actual tenant ID

if not (client_id and client_secret and tenant_id):
    st.error("Please provide SharePoint app credentials including the tenant ID.")
    st.stop()

# Azure AD endpoint for token retrieval
token_url = f"https://login.microsoftonline.com/{tenant_id}/oauth2/token"

# SharePoint app permissions request
permissions_request_xml = """
    <AppPermissionRequests AllowAppOnlyPolicy="true">
        <AppPermissionRequest Scope="http://sharepoint/content/sitecollection" Right="Read" />
        <AppPermissionRequest Scope="http://sharepoint/content/sitecollection" Right="Write" />
        <AppPermissionRequest Scope="http://sharepoint/content/sitecollection" Right="FullControl" />
        <AppPermissionRequest Scope="http://sharepoint/content/sitecollection/web" Right="Manage" />
    </AppPermissionRequests>
"""

# SharePoint app registration data
registration_data = {
    'grant_type': 'client_credentials',
    'client_id': f"{client_id}@{tenant_id}",
    'client_secret': client_secret,
    'resource': site_url,
    'scope': ' '.join(["http://sharepoint/content/sitecollection"]),
}

# Requesting an OAuth token
token_response = requests.post(token_url, data=registration_data)

# Print the token response
st.write(token_response.json())
auth_json = token_response.json()
access_token = auth_json['access_token']

# Specify the SharePoint list name
list_name = "Interview-Tracker"

# SharePoint API endpoint for adding permissions to a list
api_endpoint = f"{site_url}/_api/web/lists/getbytitle('{list_name}')/roleassignments/addroleassignment"

# Specify the principal (user or group) to which you want to grant permissions
principal_name = "buddhika@bistecglobal.com"  # Replace with the actual user or group

# Specify the role (permission level) to grant
role_def_id = 1073741824 #1073741829  # Contribute permission level

# Construct the request headers
headers = {
    'Authorization': f'Bearer {access_token}',
    'Accept': 'application/json;odata=verbose',
    'Content-Type': 'application/json;odata=verbose',
}

# Construct the request payload
payload = {
    'principalId': principal_name,
    'principalType': 1,  # 1 for user, 4 for group
    'roleDefId': role_def_id,
}

# Make the request to add permissions
response = requests.post(api_endpoint, json=payload, headers=headers)

# Check the response
if response.status_code == 200:
    st.write(f"Permissions granted successfully to {principal_name}")
else:
    st.write(f"Failed to grant permissions. Status code: {response.status_code}, Response: {response.text}")



auth = HttpNtlmAuth(access_token,"Budjan@bistec&8790")

# Connect to SharePoint using App-Only authentication
site = Site(site_url, version=Version.v365, auth=auth)



try:
    # Get the list data
    sp_list = site.List(list_name)
    data = sp_list.GetListItems()
except Exception as e:
    st.error(f"Error retrieving SharePoint data: {str(e)}")
    st.stop()

# Streamlit app code
st.title("SharePoint Data Viewer")

# Display SharePoint data in a table
st.write("SharePoint Data:")
st.table(data)

