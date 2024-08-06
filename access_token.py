import base64
import requests

client_id = 'your-client-id'
client_secret = 'your-client-secret-key'

# Encode client ID and client secret
client_creds = f"{client_id}:{client_secret}"
client_creds_b64 = base64.b64encode(client_creds.encode())

# Request access token
auth_url = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
}, headers={
    'Authorization': f'Basic {client_creds_b64.decode()}'
})

# Check for successful response
if auth_response.status_code in range(200, 299):
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to get access token: {auth_response.status_code}")
