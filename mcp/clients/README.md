# MCP Client Configurations

Connect AI assistants to MCP servers.

## Claude Desktop

**Location:** `~/Library/Application Support/Claude/claude_desktop_config.json`

**Basic:**
```json
{
  "mcpServers": {
    "pm-copilot": {
      "command": "python",
      "args": ["/absolute/path/to/mcp/servers/example-server.py"]
    }
  }
}
```

**Multiple servers:**
```json
{
  "mcpServers": {
    "pm-copilot": { "command": "python", "args": ["/path/to/example-server.py"] },
    "jira": {
      "command": "python",
      "args": ["/path/to/jira-server.py"],
      "env": { "JIRA_URL": "https://your-domain.atlassian.net" }
    }
  }
}
```

**Virtual environment:** Use `/path/to/venv/bin/python` as command

## Cursor

See `cursor-config-example.json`

## Testing

1. Verify absolute paths
2. Test manually: `python mcp/servers/example-server.py`
3. Restart AI assistant
4. Ask: "What MCP tools do you have access to?"

## Troubleshooting

- Config not loading? Check JSON syntax, absolute paths
- Server not starting? Check Python 3.10+, install dependencies
- Can't access tools? Restart AI assistant, check logs

## Security

Use `.env` for credentials, not config files.

See: `claude-config-example.json`, `cursor-config-example.json`
