# core/video_scraper.py

def fetch_channel_info(youtube, handle):
    search_response = youtube.search().list(
        part='snippet', q=handle, type='channel', maxResults=1
    ).execute()
    if not search_response['items']:
        raise ValueError(f"Channel '{handle}' not found.")
    
    channel_id = search_response['items'][0]['snippet']['channelId']
    channel_response = youtube.channels().list(
        part='contentDetails', id=channel_id
    ).execute()
    uploads_playlist_id = channel_response['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    return channel_id, uploads_playlist_id


def fetch_videos(youtube, uploads_playlist_id):
    videos = []
    request = youtube.playlistItems().list(
        part='snippet,contentDetails', playlistId=uploads_playlist_id, maxResults=50
    )
    while request:
        response = request.execute()
        for item in response['items']:
            snippet = item['snippet']
            video_id = snippet['resourceId']['videoId']
            title = snippet['title']
            publish_time = snippet['publishedAt']
            videos.append({'video_id': video_id, 'title': title, 'publishedAt': publish_time})
        request = youtube.playlistItems().list_next(request, response)
    return videos