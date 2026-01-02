# MCP Integration

Connect AI to external data sources.

## Directory Structure

```
mcp/
├── servers/    # Server implementations
├── clients/    # Client configs
```

## Quick Start

**Claude Desktop:** Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "pm-copilot": {
      "command": "python",
      "args": ["/path/to/mcp/servers/example-server.py"]
    }
  }
}
```

**Cursor:** See `clients/cursor-config-example.json`

## Use Cases

Jira/Linear/Asana, Google Analytics/Mixpanel, Slack, Confluence/Notion

## Creating Servers

See `servers/README.md` for details and `example-server.py` for template.

## Security

Use `.env` for credentials (gitignored). Never commit secrets.

```python
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")
```

## Resources

- [MCP Specification](https://github.com/anthropics/mcp)
- [MCP Python SDK](https://github.com/anthropics/mcp-python)
- [Claude MCP Docs](https://docs.anthropic.com/claude/docs/mcp)
