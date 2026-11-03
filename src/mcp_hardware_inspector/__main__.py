"""Run the MCP server over stdio."""
import asyncio
from mcp.server.fastmcp import FastMCP
from .hardware import cpu_info, memory_info, disk_info, network_interfaces, hardware_summary

mcp = FastMCP("MCP Hardware Inspector")
mcp.tool()(cpu_info)
mcp.tool()(memory_info)
mcp.tool()(disk_info)
mcp.tool()(network_interfaces)
mcp.tool()(hardware_summary)

if __name__ == "__main__":
    mcp.run(transport="stdio")
