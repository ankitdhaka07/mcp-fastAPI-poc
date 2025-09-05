from fastapi import FastAPI
from .weather import mcp

# Create FastAPI app
app = FastAPI(
    title="FastAPI MCP",
    description="A demonstration of MCP integration with StreamableHttp",
    version="0.2.0",
)

# Add MCP routes (handles /.well-known/mcp/manifest.json + streamableHttp endpoints)
# Mount the FastMCP streamable HTTP app
# This will handle all MCP protocol endpoints under the root path
app.mount("/", mcp.streamable_http_app())
# Import routes at the end
from . import routes  # noqa
