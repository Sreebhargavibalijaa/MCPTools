from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import sys

# Initialize MCP server
mcp = FastMCP("nasa_apod")

# Constants
NASA_APOD_URL = "https://api.nasa.gov/planetary/apod"
API_KEY = "DEMO_KEY"

async def fetch_apod() -> dict[str, Any] | None:
    """Fetch Astronomy Picture of the Day from NASA."""
    params = {
        "api_key": API_KEY
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(NASA_APOD_URL, params=params, timeout=20.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"APOD fetch error: {e}", file=sys.stderr)
            return None

@mcp.tool()
async def get_apod() -> str:
    """Get NASA's Astronomy Picture of the Day."""
    data = await fetch_apod()
    if not data:
        return "Failed to retrieve the Astronomy Picture of the Day."

    title = data.get("title", "Unknown Title")
    date = data.get("date", "Unknown Date")
    explanation = data.get("explanation", "No explanation provided.")
    media_type = data.get("media_type", "unknown")
    url = data.get("url", "")

    result = f"""
📅 **Date**: {date}
🪐 **Title**: {title}

📖 **Explanation**:
{explanation}

🔗 **Media Link**:
{url if media_type in ['image', 'video'] else 'No viewable media.'}
"""
    return result.strip()

if __name__ == "__main__":
    print("NASA APOD MCP server is starting...", file=sys.stderr)
    mcp.run(transport="stdio")
