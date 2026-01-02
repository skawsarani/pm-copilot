# MCP Servers

Extend PM Co-Pilot with real-time data access.

## Requirements

Python 3.10+, `pip install mcp anthropic-mcp python-dotenv`

## Quick Start

1. Copy `example-server.py`
2. Define tools
3. Implement logic
4. Configure in AI assistant

## Template

See `example-server.py` for full template. Basic structure:

```python
from mcp.server import Server
from mcp.types import Tool, TextContent

server = Server("my-pm-tool")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [Tool(name="fetch-data", description="...", inputSchema={...})]

@server.call_tool()
async def call_tool(name: str, arguments: dict):
    # Your logic here
    return [TextContent(type="text", text=result)]
```

## Configuration

Add to `~/.claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "my-pm-tool": {
      "command": "python",
      "args": ["/absolute/path/to/my-server.py"]
    }
  }
}
```

## Environment Variables

Use `.env` (gitignored):
```bash
API_KEY=your_key
API_URL=https://api.example.com
```

Load with:
```python
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
```

## Testing

- Command line: `python your-server.py`
- MCP Inspector: `npx @modelcontextprotocol/inspector python your-server.py`
- Integration: Configure in AI assistant

## Error Handling

Wrap tool calls in try/except, return errors as TextContent.

## Troubleshooting

- Server won't start? Check Python 3.10+, install dependencies
- AI can't connect? Verify absolute path
- Tools not working? Check tool name, input schema

## Resources

- [MCP Python SDK](https://github.com/anthropics/mcp-python)
- [MCP Specification](https://github.com/anthropics/mcp)
- [Example Servers](https://github.com/anthropics/mcp-servers)
