from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import sys
import os

# Initialize FastMCP server
mcp = FastMCP("news_headlines")

# Get NewsAPI key from environment variable
NEWS_API_KEY = os.environ.get("NEWS_API_KEY", "1912ff3da57b4453a3a9d262811c7159")
NEWS_API_URL = "https://newsapi.org/v2/top-headlines"
DEFAULT_COUNTRY = "us"

async def fetch_top_headlines(country: str = DEFAULT_COUNTRY) -> dict[str, Any] | None:
    """Fetch top headlines from NewsAPI for a given country."""
    params = {
        "apiKey": NEWS_API_KEY,
        "country": country
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(NEWS_API_URL, params=params, timeout=10.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"News API error: {e}", file=sys.stderr)
            return None

@mcp.tool()
async def get_top_news(country: str = "us") -> str:
    """Get top news headlines for a given country code (e.g. 'us', 'in', 'gb')."""
    data = await fetch_top_headlines(country)
    if not data or data.get("status") != "ok":
        return "Failed to fetch news headlines."

    articles = data.get("articles", [])[:5]  # Show top 5 headlines
    if not articles:
        return "No news articles found."

    result = []
    for i, article in enumerate(articles, start=1):
        title = article.get("title", "No title")
        source = article.get("source", {}).get("name", "Unknown source")
        url = article.get("url", "#")
        result.append(f"{i}. **{title}**\n   🔗 {source} – {url}")

    return "\n\n".join(result)

if __name__ == "__main__":
    print("News Headlines MCP server is starting...", file=sys.stderr)
    mcp.run(transport="stdio")
