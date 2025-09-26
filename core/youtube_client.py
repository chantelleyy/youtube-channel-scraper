from googleapiclient.discovery import build

def get_youtube_client(api_key):
    return build("youtube", "v3", developerKey=api_key)

def fetch_channel_info(youtube, handle):
    """Return channel ID and uploads playlist ID."""
    search_response = youtube.search().list(
        part='snippet',
        q=handle,
        type='channel',
        maxResults=1
    ).execute()

    if not search_response['items']:
        raise ValueError(f"Channel '{handle}' not found.")
    channel_id = search_response['items'][0]['snippet']['channelId']
    print("Channel ID:", channel_id)

    channel_response = youtube.channels().list(
        part='contentDetails',
        id=channel_id
    ).execute()

    uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    print("Uploads Playlist ID:", uploads_playlist_id)

    return channel_id, uploads_playlist_id