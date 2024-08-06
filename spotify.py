import requests
import pandas as pd

# Load the CSV file
file_path = r'your-file-path'
df = pd.read_csv(file_path, encoding='latin1')

# Spotify API credentials
client_id = 'your-client-id'
client_secret = 'your-client-secret-key'

# Get the access token
auth_url = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(auth_url, {
    'grant_type': 'client_credentials',
    'client_id': client_id,
    'client_secret': client_secret,
})
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']

# Function to get the cover URL and song URL of a track using its ISRC code
def get_track_info(isrc, access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    search_url = f'https://api.spotify.com/v1/search?q=isrc:{isrc}&type=track'
    response = requests.get(search_url, headers=headers)
    data = response.json()
    if data['tracks']['items']:
        track_info = data['tracks']['items'][0]
        album_cover_url = track_info['album']['images'][0]['url']
        track_url = track_info['external_urls']['spotify']
        return album_cover_url, track_url
    return None, None

# Add new columns for cover URLs and song URLs
df['Cover URL'], df['Song URL'] = zip(*df['ISRC'].apply(lambda x: get_track_info(x, access_token)))


# Save the updated dataframe to a new CSV file
output_path = 'your-file-path'
df.to_csv(output_path, index=False)
print(f"Updated CSV file saved to {output_path}")
