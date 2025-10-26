from fastmcp import FastMCP

# Create an MCP server instance
mcp = FastMCP("SerpMCP")

@mcp.tool
def hello_world(name: str = "World") -> str:
    """A simple hello world tool that greets the provided name.
    
    Args:
        name: The name to greet (defaults to "World")
        
    Returns:
        A friendly greeting message
    """
    return f"Hello, {name}! This is SerpMCP speaking."

@mcp.tool 
def calculate_sum(a: int, b: int) -> int:
    """Add two integers together.
    
    Args:
        a: First integer to add
        b: Second integer to add
        
    Returns:
        The sum of the two integers
    """
    return a + b

def main():
    """Main entry point for the SerpMCP server."""
    # Run the MCP server with stdio transport (default)
    mcp.run()

if __name__ == "__main__":
    main()
