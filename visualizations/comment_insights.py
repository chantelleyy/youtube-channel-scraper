# visualizations/comment_insights.py
from collections import Counter

def display_top_videos(stats, top_n=10):
    top = sorted(stats, key=lambda x: int(x['views']), reverse=True)[:top_n]
    print("\nTop {} Most Viewed Videos:".format(top_n))
    for v in top:
        print(f"{{'video_id': '{v['video_id']}', 'title': '{v['title']}', 'views': '{v['views']}', 'likes': '{v['likes']}'}}")
    return top

def display_top_liked_videos(stats, top_n=10):
    top = sorted(stats, key=lambda x: int(x['likes']), reverse=True)[:top_n]
    print("\nTop {} Most Liked Videos:".format(top_n))
    for v in top:
        print(f"{{'video_id': '{v['video_id']}', 'title': '{v['title']}', 'views': '{v['views']}', 'likes': '{v['likes']}'}}")
    return top

def display_top_descriptions_and_tags(videos):
    print("\nDescriptions & Tags for Top {} Viewed Videos:\n".format(len(videos)))
    for v in videos:
        print(f"Title: {v['title']}")
        print(f"Description:\n{v['description'].strip()[:1000]}...\n")
        print(f"Tags: {v.get('tags', 'None')}\n")

def extract_top_tags(videos):
    tag_counter = Counter()
    for v in videos:
        if 'tags' in v and isinstance(v['tags'], str):
            tags = [tag.strip() for tag in v['tags'].split(',')]
            tag_counter.update(tags)
    print("\nTop 10 Most Frequent Tags in Top Viewed Videos:")
    for tag, count in tag_counter.most_common(10):
        print(f"{tag}: {count} times")