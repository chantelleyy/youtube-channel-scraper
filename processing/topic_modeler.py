from collections import Counter
from sklearn.cluster import KMeans
from sentence_transformers import SentenceTransformer

def cluster_comments(texts, n_clusters=5):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(texts)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    return kmeans.fit_predict(embeddings)

def extract_top_tags(top_viewed, top_n=10):
    """Extract and display the top N most frequent tags from top-viewed videos."""
    tag_counter = Counter()

    for video in top_viewed:
        tags = video.get('tags', [])

        if isinstance(tags, str):
            tags = [tag.strip() for tag in tags.split(',')]
        if isinstance(tags, list):
            tag_counter.update(tags)

    top_tags = tag_counter.most_common(top_n)

    print(f"\nTop {top_n} Most Frequent Tags in Top Viewed Videos:")
    for tag, count in top_tags:
        print(f"{tag}: {count} times")

    return top_tags