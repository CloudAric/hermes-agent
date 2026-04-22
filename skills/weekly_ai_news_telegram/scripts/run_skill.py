#!/usr/bin/env python3
"""
Run the weekly AI news telegram skill
"""
import json
import sys
from datetime import datetime, timezone
from fetch_ai_news import fetch_all_news

def format_news(news_data):
    """Format news data for Telegram"""
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    
    output = []
    output.append("🚀 Weekly AI News Update")
    output.append(f"📅 {timestamp}")
    output.append("")
    
    # Define emoji mapping for sources
    emojis = {
        'TechCrunch': '📰',
        'Reuters': '📰',
        'BBC': '📰',
        'Hacker News': '🔥',
        'ArsEnble': '📄'
    }
    
    for source, articles in news_data.items():
        if articles:
            emoji = emojis.get(source, '📰')
            output.append(f"{emoji} **{source}**")
            output.append("-" * 40)
            
            for i, article in enumerate(articles, 1):
                title = article.get('title', 'No Title')
                url = article.get('url', '#')
                summary = article.get('summary', '')[:100] + '...' if article.get('summary') else ''
                
                output.append(f"{i}. [{title}]({url})")
                if summary:
                    output.append(f"   {summary}")
                output.append("")
        else:
            output.append(f"⚠️ {source}: No recent articles")
            output.append("")
    
    return '\n'.join(output)

def main():
    try:
        # Fetch news from all sources
        news_data = fetch_all_news()
        
        # Format for Telegram
        formatted_news = format_news(news_data)
        
        # Output the result (would be sent to Telegram in production)
        print(formatted_news)
        
        # Also save to file for debugging
        with open('/tmp/ai_news_output.txt', 'w') as f:
            f.write(formatted_news)
            
    except Exception as e:
        print(f"Error in main: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()