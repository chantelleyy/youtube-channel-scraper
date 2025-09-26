# YouTube Channel Scraper & Analyzer

This project is a customizable pipeline for scraping and analyzing all videos from a specific Space/technology YouTube channel using the YouTube Data API v3. It scrapes a YouTube channel’s video data, fetching key metrics such as category IDs, titles, views, likes, descriptions, publishedAt dates, tags, and thumbnails to tackle placement strategies. The pipeline displays the top 10 most viewed videos and extracts and prints keywords (tags) from the top 5 viewed videos. Additionally, it enables the understanding of trends related to space topics through tag frequency analysis, description and tag exploration, and basic statistics like average title and description lengths, culminating in sentiment analysis of viewers' comments.
---

## About Channel Scraping

This project uses a channel handle to look up the channel ID and its upload playlist, scrape all videos in that playlist, and retrieve statistics and comments for each video. This method is ideal for content creators analyzing their own channel, researchers studying public YouTube creators, and building dashboards for channel performance insights.

---

## Project Structure

```bash
youtube_channel_scraper/
├── config/
│   └── config_handler.py             # Load API key from .env or config
│
├── core/
│   ├── youtube_client.py            # YouTube API wrapper
│   ├── video_scraper.py             # Fetch channel uploads
│   ├── video_data_fetcher.py        # Fetch video stats
│   ├── comment_scraper.py           # Fetch video comments
│   └── sentiment_analyzer.py        # Sentiment analysis (HuggingFace)
│
├── processing/
│   ├── data_cleaner.py              # Clean and structure data
│   ├── metrics_calculator.py        # Calculate metrics (title/desc length)
│   ├── topic_modeler.py             # Topic clustering
│   └── upload_time_analysis.py      # Analyze upload times
│
├── storage/
│   └── storage_handler.py           # Save data to CSV
│
├── visualizations/
│   └── comment_insights.py          # Display stats, tags, and trends
│
├── notebooks/
│   └── youtube_pipeline_demo.ipynb  # Jupyter demo of pipeline
│
├── astrum_video_stats.csv           # Output CSV: video metadata + stats
├── top_10_upload_times.csv          # Output CSV: top video upload times
├── requirements.txt                 # Python dependencies
├── main.py                          # Main CLI script
├── .env                             # API key (not versioned)
├── .gitignore                       # Ignore .env, __pycache__, etc.
└── README.md                        # Project overview and outputs


## Output Examples

### Top Viewed Videos: 
Top 10 Most Viewed Videos:
{'video_id': 'D5XPuS-Y0fg', 'title': 'The Final Images We Will Ever See of Pluto and Arrokoth', 'views': '17669028', 'likes': '228391'}
{'video_id': '6EbuAEagQj4', 'title': 'The Deepest We Have Ever Seen Into the Sun | SDO 4K', 'views': '9336423', 'likes': '113227'}
{'video_id': '6l4kr36TzQ4', 'title': "What did NASA's New Horizons discover around Pluto?", 'views': '9196621', 'likes': '122894'}
{'video_id': 'iogVVja1MYY', 'title': 'The Gravity Illusion', 'views': '9070146', 'likes': '173380'}
{'video_id': 'tyMbktsAScE', 'title': "NASA Cassini's Final Images of Saturn Stunned Me", 'views': '8997449', 'likes': '183846'}
{'video_id': 'mggRl80WzbE', 'title': 'What El Niño Will Do to Earth', 'views': '6991834', 'likes': '90602'}
{'video_id': 'H-hZsoyUEXs', 'title': "The Tragic Final Images of NASA's Opportunity Rover | Opportunity Episode 7", 'views': '6902904', 'likes': '89713'}
{'video_id': 'UyzBoUvN3PM', 'title': 'What Voyager Detected at the Edge of the Solar System', 'views': '5926816', 'likes': '77872'}
{'video_id': 'u4tzK89ZfmA', 'title': "Everything We Know About 'Oumuamua", 'views': '5698821', 'likes': '84006'}
{'video_id': 'YpyXVkqkQgg', 'title': 'Time Does Not Exist. Let me explain with a graph.', 'views': '5519012', 'likes': '120726'}

### Tags (frequent in top videos):
Top 10 Most Frequent Tags in Top Viewed Videos:
astrum: 8 times
astrumspace: 6 times
nasa: 5 times
solar system: 4 times
space: 4 times
pluto: 3 times
astronomy: 3 times
physics: 3 times
new horizons: 2 times
charon: 2 times

### Video Upload Time
The Final Images We Will Ever See of Pluto and Arrokoth → Uploaded at 21:58:35 UTC
The Deepest We Have Ever Seen Into the Sun | SDO 4K → Uploaded at 19:30:00 UTC
What did NASA's New Horizons discover around Pluto? → Uploaded at 14:03:26 UTC
The Gravity Illusion → Uploaded at 17:00:23 UTC
NASA Cassini's Final Images of Saturn Stunned Me → Uploaded at 15:06:10 UTC
What El Niño Will Do to Earth → Uploaded at 21:20:58 UTC
The Tragic Final Images of NASA's Opportunity Rover | Opportunity Episode 7 → Uploaded at 17:26:44 UTC
What Voyager Detected at the Edge of the Solar System → Uploaded at 17:30:04 UTC
Everything We Know About 'Oumuamua → Uploaded at 16:01:29 UTC
Time Does Not Exist. Let me explain with a graph. → Uploaded at 18:06:22 UTC

### Continuous Enhancement Strategies for the Channel
Throughout the project, continuous implementation focuses on understanding trends or recent top searches related to space, earth, and astronaut topics on the internet, utilizing data from Google Trends to continually enrich channel content variety. By referring to channel data analytics reports, the project adjusts video placement strategies, while performing A/B tests on content, upload times, thumbnails, titles, and description strategies to better understand viewer behavior. Additionally, it includes competitor analysis to compare performance with other channels, reply-thread comment scraping, and LDA or embedding-based comment topic modeling to deepen insights. The goal is to increase the CTR rate while keeping track of all strategies implemented on the content to seek performance improvements.