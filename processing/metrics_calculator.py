def average_title_description_length(stats):
    title_lens = [len(v['title']) for v in stats]
    desc_lens = [len(v['description']) for v in stats if v['description']]
    return sum(title_lens)/len(title_lens), sum(desc_lens)/len(desc_lens)

def display_top_liked_videos(stats, top_n=5):
    """Display top N videos by like count."""
    sorted_stats = sorted(stats, key=lambda x: x['likes'], reverse=True)
    top = sorted_stats[:top_n]
    print("\nTop Liked Videos:")
    for i, video in enumerate(top, 1):
        print(f"{i}. {video['title']} — {video['likes']} likes")
    return top

def display_top_videos(stats, top_n=5):
    """Display top N videos by view count."""
    sorted_stats = sorted(stats, key=lambda x: x['views'], reverse=True)
    top = sorted_stats[:top_n]
    print("\nTop Viewed Videos:")
    for i, video in enumerate(top, 1):
        print(f"{i}. {video['title']} — {video['views']} views")
    return top

def display_top_descriptions(top_viewed):
    """Display descriptions of the top 5 most viewed videos."""
    print("\nDescriptions for Top 5 Viewed Videos:")
    for v in top_viewed[:5]:
        print(f"\nTitle: {v['title']}")
        desc = v['description']
        if len(desc) > 500:
            desc = desc[:500] + "..."
        print("Description:")
        print(desc)

def display_top_descriptions_and_tags(top_viewed):
    """Display descriptions and tags of the top 5 most viewed videos."""
    print("\nDescriptions & Tags for Top 5 Viewed Videos:")
    for v in top_viewed[:5]:
        print(f"\nTitle: {v['title']}")
        desc = v['description']
        if len(desc) > 500:
            desc = desc[:500] + "..."
        print("Description:")
        print(desc)
        print("Tags:", v['tags'])