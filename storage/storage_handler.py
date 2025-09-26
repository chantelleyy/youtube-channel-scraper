import csv

def save_stats_to_csv(stats, filename="video_stats.csv"):
    """Save clean, readable video statistics to a CSV file."""

    fields_to_save = [
        'video_id',
        'title',
        'views',
        'likes',
        'publishedAt',
        'tags',
        'description',
        'thumbnail_url'
    ]

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields_to_save, quoting=csv.QUOTE_ALL)
        writer.writeheader()

        for video in stats:
            # Prepare clean data
            row = {
                'video_id': video.get('video_id', ''),
                'title': video.get('title', '').replace('\n', ' ').strip(),
                'views': video.get('views', 0),
                'likes': video.get('likes', 0),
                'publishedAt': video.get('publishedAt', ''),
                'tags': video.get('tags', 'None'),
                'description': video.get('description', '').replace('\n', ' ').strip(),
                'thumbnail_url': video.get('thumbnail_url', 'N/A')
            }
            writer.writerow(row)

    print(f"Clean video stats saved to: {filename}")