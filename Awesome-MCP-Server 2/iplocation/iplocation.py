from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP
import sys

# Initialize FastMCP server
mcp = FastMCP("ip_geolocator")

# API base
GEOLOCATION_API = "http://ip-api.com/json/"

async def fetch_ip_data(ip: str) -> dict[str, Any] | None:
    """Fetch geolocation data for a given IP address."""
    url = f"{GEOLOCATION_API}{ip}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"IP lookup error: {e}", file=sys.stderr)
            return None

@mcp.tool()
async def geolocate_ip(ip: str) -> str:
    """Get geolocation data for a given IP address.

    Args:
        ip: A valid IP address (e.g. 8.8.8.8)
    """
    data = await fetch_ip_data(ip)
    if not data or data.get("status") != "success":
        return "Could not retrieve geolocation info for this IP."

    return f"""
🌐 IP: {ip}
📍 Location: {data.get('city', 'N/A')}, {data.get('regionName', 'N/A')}, {data.get('country', 'N/A')}
🌎 Coordinates: {data.get('lat', 'N/A')}, {data.get('lon', 'N/A')}
🏢 ISP: {data.get('isp', 'N/A')}
🕹️ Org: {data.get('org', 'N/A')}
"""

if __name__ == "__main__":
    print("IP Geolocation MCP server is starting...", file=sys.stderr)
    mcp.run(transport="stdio")
