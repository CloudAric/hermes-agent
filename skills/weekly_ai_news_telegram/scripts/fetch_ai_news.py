#!/usr/bin/env python3
"""
Fetch AI news from multiple sources
"""
import feedparser
import requests
from datetime import datetime, timedelta, timezone
import json

def fetch_techcrunch():
    """Fetch AI news from TechCrunch"""
    try:
        url = "https://techcrunch.com/tag/artificial-intelligence/feed/"
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries[:5]:
            # Filter for last 24 hours
            published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
            if published > datetime.now(timezone.utc) - timedelta(hours=24):
                articles.append({
                    'title': entry.title,
                    'url': entry.link,
                    'summary': entry.summary if hasattr(entry, 'summary') else '',
                    'source': 'TechCrunch'
                })
        return articles
    except Exception as e:
        print(f"TechCrunch error: {e}")
        return []

def fetch_reuters():
    """Fetch AI news from Reuters"""
    try:
        # Using a technology news feed - Reuters doesn't have a specific AI RSS
        url = "https://www.reuters.com/business/technology/"
        # For this implementation, we'll use a placeholder
        # In production, you'd use Reuters API or a specific technology feed
        return [
            {
                'title': 'AI Technology News from Reuters',
                'url': 'https://www.reuters.com/business/technology/',
                'summary': 'Latest technology and AI developments',
                'source': 'Reuters'
            }
        ]
    except Exception as e:
        print(f"Reuters error: {e}")
        return []

def fetch_bbc():
    """Fetch AI news from BBC"""
    try:
        url = "https://www.bbc.com/news/technology"
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries[:5]:
            published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
            if published > datetime.now(timezone.utc) - timedelta(hours=24):
                articles.append({
                    'title': entry.title,
                    'url': entry.link,
                    'summary': entry.summary if hasattr(entry, 'summary') else '',
                    'source': 'BBC'
                })
        return articles
    except Exception as e:
        print(f"BBC error: {e}")
        return []

def fetch_hacker_news():
    """Fetch AI stories from Hacker News"""
    try:
        # Search for AI stories on Hacker News
        search_url = "https://hn.algolia.com/api/v1/search?query=artificial+intelligence&tags=story&numericFilters=created_at_i>{}&hitsPerPage=5".format(
            int((datetime.now(timezone.utc) - timedelta(hours=24)).timestamp())
        )
        response = requests.get(search_url)
        data = response.json()
        articles = []
        for hit in data.get('hits', [])[:5]:
            articles.append({
                'title': hit.get('title', 'No title'),
                'url': hit.get('url', 'https://news.ycombinator.com/item?id=' + str(hit.get('objectID', ''))),
                'summary': hit.get('text', '')[:100],
                'source': 'Hacker News'
            })
        return articles
    except Exception as e:
        print(f"Hacker News error: {e}")
        return []

def fetch_arsenble():
    """Fetch AI papers from arsanble"""
    try:
        url = "https://arsenble.github.io/ai-papers/rss"
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries[:5]:
            published = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
            if published > datetime.now(timezone.utc) - timedelta(hours=24):
                articles.append({
                    'title': entry.title,
                    'url': entry.link,
                    'summary': entry.summary if hasattr(entry, 'summary') else '',
                    'source': 'ArsEnble'
                })
        return articles
    except Exception as e:
        print(f"ArsEnble error: {e}")
        return []

def fetch_all_news():
    """Fetch news from all sources"""
    sources = [
        ('TechCrunch', fetch_techcrunch),
        ('Reuters', fetch_reuters),
        ('BBC', fetch_bbc),
        ('Hacker News', fetch_hacker_news),
        ('ArsEnble', fetch_arsenble)
    ]
    
    results = {}
    for source_name, fetch_func in sources:
        try:
            results[source_name] = fetch_func()
        except Exception as e:
            print(f"Error fetching from {source_name}: {e}")
            results[source_name] = []
    
    return results

if __name__ == "__main__":
    news = fetch_all_news()
    print(json.dumps(news, indent=2))