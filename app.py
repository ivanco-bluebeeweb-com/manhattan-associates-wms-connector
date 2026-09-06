"""Extension declaration, capabilities, health check for Manhattan Associates WMS Connector."""
from __future__ import annotations
import json
from imperal_sdk import ChatExtension, Extension

ext = Extension(
    "manhattan-associates-wms-connector",
    version="0.1.0",
    display_name="Manhattan Associates WMS",
    icon="icon.svg",
    capabilities=["manhattan_wms:manage"],
    description="Official Imperal connector for Manhattan Associates WMS (C30. Email Marketing & Newsletter). Manage operations securely."
)

chat = ChatExtension(ext)

@ext.health_check
async def health_check(ctx) -> dict:
    raw = await ctx.secrets.get("manhattan_wms_connections")
    try:
        count = len(json.loads(raw)) if raw else 0
    except Exception:
        count = 0
    return {
        "healthy": True,
        "detail": f"{count} Manhattan Associates WMS connection(s) configured." if count else "Not connected yet."
    }
