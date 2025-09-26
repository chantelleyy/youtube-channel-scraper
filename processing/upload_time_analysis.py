from datetime import datetime
import csv

def show_top_upload_times(stats, top_n=10, save_to=None):
    top_viewed = sorted(stats, key=lambda x: x['views'], reverse=True)[:top_n]
    upload_times = []
    lines = []

    for v in top_viewed:
        try:
            dt = datetime.strptime(v['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
            upload_times.append(dt.time())
            line = f"{v['title']} → {dt.strftime('%H:%M:%S')} UTC"
        except KeyError:
            line = f"Missing 'publishedAt' for: {v['title']}"
        print(line)
        lines.append(line)

    if save_to:
        if save_to.endswith(".csv"):
            with open(save_to, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Title", "Upload Time (UTC)"])
                for v, t in zip(top_viewed, upload_times):
                    writer.writerow([v['title'], t.strftime('%H:%M:%S')])
        else:
            with open(save_to, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))