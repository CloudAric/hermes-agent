---
name: weekly_ai_news_telegram
description: Fetches AI news from reliable sources and sends a formatted update to Telegram
category: productivity
scripts:
  - fetch_ai_news.py
  - run_skill.py
---

# Working AI News Telegram Update Skill

This skill fetches AI news from reliable sources with working RSS feeds and APIs, then sends a formatted update to Telegram.

## Sources
- TechCrunch AI (RSS)
- Reuters AI (RSS)
- BBC News Technology (RSS)
- Hacker News AI stories (API)
- arsanble AI Papers (RSS)

## Format
Clean, reliable overview optimized for Telegram:
- 🚀 Header with timestamp
- Emoji headers for each source
- Numbered list with [Title](URL) format
- Brief, informative summaries
- Visual separation between sections

## Workflow
1. Execute the run_skill.py script which:
   - Runs the fetch_ai_news.py script in the scripts directory
   - Fetches from proven RSS feeds and APIs
   - Parses content reliably with error handling
   - Focuses on last 24 hours of developments
   - Formats into clear sections with emojis
2. Script handles:
   - TechCrunch: /tag/artificial-intelligence/feed/
   - Reuters: technology news RSS
   - BBC: technology news RSS
   - Hacker News: AI stories via Algolia API
   - arsanble: latest AI cs.AR RSS
3. Includes UTC timestamp in header
4. When run as cron job, auto-delivers response

## Tools Required
- terminal (for curl/fetching feeds via script)
- execute_code (for Python script execution)
- No browser dependency (more reliable)

## Notes
- Built for maximum reliability: tested sources and fallback handling
- Graceful degradation: if one source fails, others still deliver
- Focuses on signal over noise with real AI developments
- Environment variable driven configuration
- Designed specifically for cron job execution