import argparse
from config.config_handler import load_api_key
from googleapiclient.discovery import build

from core.video_scraper import fetch_channel_info, fetch_videos
from core.video_data_fetcher import fetch_video_stats
from storage.storage_handler import save_stats_to_csv
from processing.metrics_calculator import average_title_description_length, display_top_videos, display_top_liked_videos
from processing.topic_modeler import extract_top_tags
from visualizations.comment_insights import display_top_descriptions_and_tags
from processing.upload_time_analysis import show_top_upload_times

def main(handle="astrum"):
    """Main function to scrape and display YouTube channel video stats."""
    api_key = load_api_key()
    youtube = build("youtube", "v3", developerKey=api_key)

    # Fetch channel & playlist
    channel_id, uploads_playlist_id = fetch_channel_info(youtube, handle)
    print(f"Channel ID: {channel_id}")
    print(f"Uploads Playlist ID: {uploads_playlist_id}")

    # Fetch video metadata
    videos = fetch_videos(youtube, uploads_playlist_id)
    print(f"Total videos retrieved from channel: {len(videos)}")

    # Fetch stats
    video_ids = [v["video_id"] for v in videos]
    stats = fetch_video_stats(youtube, video_ids)

    # Save to CSV
    save_stats_to_csv(stats, filename=f"{handle}_video_stats.csv")

    # Basic metrics
    avg_title_len, avg_desc_len = average_title_description_length(stats)
    print(f"\nAvg Title Length: {avg_title_len:.2f} characters")
    print(f"Avg Description Length: {avg_desc_len:.2f} characters\n")

    # Top content and tags
    top_viewed = display_top_videos(stats)
    top_liked = display_top_liked_videos(stats)
    display_top_descriptions_and_tags(top_viewed[:5])
    extract_top_tags(top_viewed[:5])

    show_top_upload_times(stats, save_to="top_10_upload_times.csv")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape YouTube channel data.")
    parser.add_argument('--handle', default='astrum', help="YouTube channel handle (e.g., astrumextra)")
    args = parser.parse_args()
    main(args.handle)