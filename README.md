<h2>YouTube Channel Scraper & Analyzer</h2>
<p style="font-size: 14px;">
This project is a customizable pipeline for scraping and analyzing all videos from a specific Space/technology YouTube channel using the YouTube Data API v3. It scrapes a YouTube channel’s video data, fetching key metrics such as category IDs, titles, views, likes, descriptions, publishedAt dates, tags, and thumbnails to tackle placement strategies. The pipeline displays the top 10 most viewed videos and extracts and prints keywords (tags) from the top 5 viewed videos. Additionally, it enables the understanding of trends related to space topics through tag frequency analysis, description and tag exploration, and basic statistics like average title and description lengths, culminating in sentiment analysis of viewers' comments.</p>

<p style="font-size: 14px;">
About Channel Scraping
This project uses a channel handle (e.g., astrum) to look up the channel ID and its upload playlist, scrape all videos in that playlist, and retrieve statistics and comments for each video. This method is ideal for content creators analyzing their own channel, researchers studying public YouTube creators, and building dashboards for channel performance insights.</p>
---

## Project Structure
<pre style="font-size: 13px;">
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
</pre>

## Output Examples

### Top 10 Most Viewed Videos:
| Title                                                                   | Views      | Likes    |
|-------------------------------------------------------------------------|------------|----------|
| The Final Images We Will Ever See of Pluto and Arrokoth                | 17,669,028 | 228,391  |
| The Deepest We Have Ever Seen Into the Sun \| SDO 4K                   | 9,336,423  | 113,227  |
| What did NASA's New Horizons discover around Pluto?                    | 9,196,621  | 122,894  |
| The Gravity Illusion                                                   | 9,070,146  | 173,380  |
| NASA Cassini's Final Images of Saturn Stunned Me                       | 8,997,449  | 183,846  |
| What El Niño Will Do to Earth                                          | 6,991,834  | 90,602   |
| The Tragic Final Images of NASA's Opportunity Rover                    | 6,902,904  | 89,713   |
| What Voyager Detected at the Edge of the Solar System                  | 5,926,816  | 77,872   |
| Everything We Know About 'Oumuamua                                     | 5,698,821  | 84,006   |
| Time Does Not Exist. Let me explain with a graph.                      | 5,519,012  | 120,726  |
---

### Top 10 Most Frequent Tags in Top Viewed Videos:

| Tag           | Frequency |
|---------------|-----------|
| astrum        | 8         |
| astrumspace   | 6         |
| nasa          | 5         |
| solar system  | 4         |
| space         | 4         |
| pluto         | 3         |
| astronomy     | 3         |
| physics       | 3         |
| new horizons  | 2         |
| charon        | 2         |
---

### Upload Times (Top Viewed Videos)
| Title                                                             | Upload Time (UTC) |
|-------------------------------------------------------------------|--------------------|
| The Final Images We Will Ever See of Pluto and Arrokoth          | 21:58:35           |
| The Deepest We Have Ever Seen Into the Sun \| SDO 4K             | 19:30:00           |
| What did NASA's New Horizons discover around Pluto?              | 14:03:26           |
| The Gravity Illusion                                             | 17:00:23           |
| NASA Cassini's Final Images of Saturn Stunned Me                 | 15:06:10           |
| What El Niño Will Do to Earth                                    | 21:20:58           |
| The Tragic Final Images of NASA's Opportunity Rover              | 17:26:44           |
| What Voyager Detected at the Edge of the Solar System            | 17:30:04           |
| Everything We Know About 'Oumuamua                               | 16:01:29           |
| Time Does Not Exist. Let me explain with a graph.                | 18:06:22           |
---

## Continuous Enhancement Strategies for the Channel
Throughout the project, continuous implementation focuses on understanding trends or recent top searches related to space, earth, and astronaut topics on the internet, utilizing data from Google Trends to continually enrich channel content variety. By referring to channel data analytics reports, the project adjusts video placement strategies, while performing A/B tests on content, upload times, thumbnails, titles, and description strategies to better understand viewer behavior. Additionally, it includes competitor analysis to compare performance with other channels, reply-thread comment scraping, and LDA or embedding-based comment topic modeling to deepen insights. The goal is to increase the CTR rate while keeping track of all strategies implemented on the content to seek performance improvements.