# SerpMCP - AI Agent Development Guide

## Project Overview
SerpMCP is a Model Context Protocol (MCP) server for SerpApi search integration. This is a Python package that provides search capabilities as an MCP server.

## Architecture
- **Package Structure**: Standard `src/` layout with `serpmcp` as the root module
- **Entry Point**: CLI command `serpmcp` points to `serpmcp.main:main`
- **Build System**: Uses `uv_build` backend (uv's native build system)
- **Python Version**: 3.10-3.13 (project targets 3.13 in development)

## Development Workflow

### Essential Commands
```bash
# Build the package
uv build

# Run the CLI tool
uv run serpmcp

# Install for development
uv pip install -e .

# Install dependencies
uv sync
```

### Project Structure
```
src/serpmcp/
├── __init__.py    # Currently empty - package initialization
└── main.py        # CLI entry point and main logic
```

## Key Conventions

### Build System
- Uses `uv_build` instead of setuptools - this is uv's modern, fast build backend
- Configuration in `pyproject.toml` follows PEP 621 standards
- `uv.lock` is included for reproducible builds

### CLI Pattern
- Entry point follows `module.submodule:function` pattern
- Main function should be named `main()` following Python conventions
- CLI command name matches package name: `serpmcp`

### Package Metadata
- MIT license with license files pattern `LICEN[CS]E*`
- Pre-release versioning: `0.1.0a1` (alpha release)
- Keywords emphasize MCP, SerpApi, server, search capabilities

## FastMCP Framework Knowledge

### Server Architecture
- **FastMCP Instance**: Create server with `mcp = FastMCP("ServerName")`
- **Transport**: Default is stdio, supports HTTP/SSE for web deployments
- **Entry Point**: Use `mcp.run()` in main function for CLI execution

### Tool Definition Patterns
```python
@mcp.tool
def tool_name(param: type, default: value = default) -> return_type:
    """Tool description following MCP standards.
    
    Args:
        param: Parameter description
        
    Returns:
        Return value description
    """
    return result
```

### Key Tool Design Principles
- **Type Hints**: Required for automatic schema generation
- **Docstrings**: Used for tool descriptions and parameter docs
- **Default Values**: Supported and recommended for optional parameters
- **Return Types**: Can be str, int, dict, JSON-serializable objects

### Testing Strategies
- **In-Memory Testing**: Use `Client(mcp_instance)` for direct connection
- **No Process Overhead**: Avoids subprocess/stdio communication in tests
- **Client API**: `await client.call_tool("tool_name", {"param": value})`
- **Async Pattern**: All client operations are async

### Testing Best Practices
```python
async with Client(mcp_server) as client:
    # Test server connectivity
    ping_result = await client.ping()
    
    # List available tools
    tools = await client.list_tools()
    
    # Call specific tools
    result = await client.call_tool("tool_name", {"arg": "value"})
    assert result.content[0].text == expected
```

### MCP Protocol Concepts
- **Tools**: Functions that LLMs can call (like POST endpoints)
- **Resources**: Read-only data sources (like GET endpoints) 
- **Prompts**: Reusable message templates for LLM interactions
- **Context**: Access to MCP session capabilities via `ctx: Context`

### Development Workflow
- **Local Testing**: Use in-memory Client for unit tests
- **Integration Testing**: Test with actual MCP clients
- **Server Startup**: Verify `mcp.run()` starts without errors
- **Tool Validation**: Test all parameter combinations

## Important Notes
- Package is intended as an MCP server, not a standard CLI tool
- Built with FastMCP framework for rapid MCP development
- Future development should focus on SerpApi integration
- Consider async patterns for MCP server implementation