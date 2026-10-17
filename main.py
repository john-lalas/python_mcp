from mcp.server.mcpserver import MCPServer
from python_mcp.tools import read_only

# Create a small MCP server for my project
# This server gives my AI coding agent safe project context
mcp = MCPServer("python_mcp")


@mcp.tool()
def list_project_files() -> str:
    return read_only.list_project_files()


@mcp.tool()
def read_project_file(relative_file_path: str) -> str:
    return read_only.read_project_file(relative_file_path=relative_file_path)


@mcp.tool()
def search_notes(keyword: str) -> str:
    return read_only.search_notes(keyword=keyword)
