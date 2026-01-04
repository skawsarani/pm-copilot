# MCP Integration

This directory is for custom MCP (Model Context Protocol) servers you create to connect AI to external data sources.

---

## Quick Start

### 1. Learn from the Task Manager MCP

See `core/task-manager/` for a complete working example:

```bash
cd core/task-manager
cat server.py  # Review implementation
```

Full documentation: `core/README.md`

### 2. Build Your Own MCP Server

**Use the mcp-builder skill** to generate high-quality MCP servers:

```
/mcp-builder [service-name]
```

The skill will guide you through creating MCP servers for:
- Jira/Linear/Asana - Task management integration
- Google Analytics/Mixpanel - Metrics and analytics
- Slack - Team communication
- Confluence/Notion - Documentation
- GitHub/GitLab - Code and issues
- Figma - Design files

See `skills/mcp-builder/SKILL.md` for details.

### 3. Install and Configure

Once you've created your MCP server:

**Claude Desktop** - Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "your-server": {
      "command": "python3",
      "args": ["/absolute/path/to/pm-copilot/mcp/your-server.py"],
      "cwd": "/absolute/path/to/pm-copilot"
    }
  }
}
```

**Cursor** - Create `.cursor/mcp.json` in project root:
```json
{
  "mcpServers": {
    "your-server": {
      "command": "python3",
      "args": ["./mcp/your-server.py"]
    }
  }
}
```

Restart your MCP client to load the server.

---

## Security

**Never commit secrets!** Use `.env` files (gitignored):

```bash
# .env
API_KEY=your-key-here
```

```python
# your-server.py
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
```

---

## Resources

- **MCP-Builder Skill**: `skills/mcp-builder/` (use this to generate servers)
- **Task Manager Example**: `core/task-manager/` (working reference implementation)
- **MCP Specification**: https://github.com/anthropics/mcp
- **MCP Python SDK**: https://github.com/anthropics/mcp-python
