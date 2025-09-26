def fetch_videos(youtube, uploads_playlist_id):
    """Return list of videos with ID, title, and published date."""
    videos = []
    request = youtube.playlistItems().list(
        part='snippet,contentDetails',
        playlistId=uploads_playlist_id,
        maxResults=50
    )

    while request:
        response = request.execute()
        for item in response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            title = item['snippet']['title']
            publish_time = item['snippet']['publishedAt']
            videos.append({
                'video_id': video_id,
                'title': title,
                'publishedAt': publish_time
            })
        request = youtube.playlistItems().list_next(request, response)

    return videos

def fetch_video_stats(youtube, video_ids):
    """Return video statistics and thumbnail URLs."""
    stats = []
    for i in range(0, len(video_ids), 50):
        batch = video_ids[i:i+50]
        v_response = youtube.videos().list(
            part='statistics,snippet',
            id=','.join(batch)
        ).execute()

        for vi in v_response['items']:
            snippet = vi['snippet']
            statistics = vi['statistics']
            thumbnails = snippet.get('thumbnails', {})

            # Safely extract thumbnail
            thumbnail_url = None
            for quality in ['maxres', 'standard', 'high', 'medium', 'default']:
                if quality in thumbnails:
                    thumbnail_url = thumbnails[quality]['url']
                    break

            stats.append({
                'video_id': vi['id'],
                'title': snippet.get('title', 'N/A'),
                'views': int(statistics.get('viewCount', 0)),
                'likes': int(statistics.get('likeCount', 0)),
                'description': snippet.get('description', ''),
                'categoryId': snippet.get('categoryId', ''),
                'tags': ', '.join(snippet.get('tags', [])) if 'tags' in snippet else 'None',
                'publishedAt': snippet.get('publishedAt'),
                'thumbnail_url': thumbnail_url
            })
    return stats