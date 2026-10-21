"""Fetches the Medium feed and writes posts.json for the Blog page. Run by .github/workflows/medium.yml."""
import json, re, html, urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

FEED = "https://medium.com/feed/@topper1728"
NS = {"content": "http://purl.org/rss/1.0/modules/content/"}

req = urllib.request.Request(FEED, headers={"User-Agent": "Mozilla/5.0 (compatible; site-builder)"})
root = ET.fromstring(urllib.request.urlopen(req, timeout=30).read())
posts = []
for item in root.iter("item"):
    body = item.findtext("content:encoded", "", NS) or item.findtext("description", "")
    img = next((m for m in re.finditer(r'<img[^>]+src="([^"]+)"', body) if "/_/stat" not in m.group(1)), None)
    text = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", body))).strip()
    posts.append({
        "title": item.findtext("title", "").strip(),
        "link": item.findtext("link", "").split("?")[0],
        "date": parsedate_to_datetime(item.findtext("pubDate")).strftime("%b %-d, %Y"),
        "thumbnail": img.group(1) if img else "",
        "excerpt": text[:160],
    })
json.dump(posts, open("posts.json", "w"), indent=1, ensure_ascii=False)
print(f"wrote {len(posts)} posts")
