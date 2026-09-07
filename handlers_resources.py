"""Resource handlers for Manhattan Active WMS Connector."""
from __future__ import annotations
from typing import Any
from imperal_sdk import ActionResult
from app import chat
from schemas import (
    ListShipmentParams, GetShipmentParams,
    ShipmentRecord, ShipmentList, AuditHealthReport, ConnectionIdParams
)
from handlers_connection import resolve_client

@chat.function("list_shipments", "List shipments in Manhattan Active WMS.", action_type="read", chain_callable=True, event="manhattan-associates-wms-connector.list_shipments", effects=["read:shipments"], data_model=ShipmentList)
async def list_shipments(ctx, params: ListShipmentParams) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        raw_items = await client.list_shipments(limit=params.limit)
        items = []
        for r in raw_items:
            rid = str(r.get("id") or r.get("key") or r.get("uuid") or "unknown")
            rname = r.get("name") or r.get("title") or r.get("label") or rid
            items.append({"id": rid, "name": rname, "status": r.get("status"), "created_at": r.get("createdAt") or r.get("created_at"), "raw": r})
        return ActionResult.success({"shipments": items, "total": len(items)}, summary=f"Found {len(items)} shipments.")
    except Exception as e:
        return ActionResult.error(f"Error listing shipments: {e}")

@chat.function("get_shipment", "Get details of one Shipment in Manhattan Active WMS.", action_type="read", chain_callable=True, event="manhattan-associates-wms-connector.get_shipment", effects=["read:shipment"], data_model=ShipmentRecord)
async def get_shipment(ctx, params: GetShipmentParams) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        r = await client.get_shipment(params.shipment_id)
        rid = str(r.get("id") or params.shipment_id)
        rname = r.get("name") or r.get("title") or rid
        return ActionResult.success({"id": rid, "name": rname, "status": r.get("status"), "created_at": r.get("createdAt") or r.get("created_at"), "raw": r}, summary=f"Retrieved Shipment {rid}.")
    except Exception as e:
        return ActionResult.error(f"Error retrieving Shipment: {e}")

@chat.function("audit_shipment_health", "Audit health of Manhattan Active WMS shipments and connectivity.", action_type="read", chain_callable=True, event="manhattan-associates-wms-connector.audit_shipment_health", effects=["read:audit"], data_model=AuditHealthReport)
async def audit_shipment_health(ctx, params: ConnectionIdParams) -> ActionResult:
    client = await resolve_client(ctx, params.connection_id)
    try:
        items = await client.list_shipments(limit=50)
        return ActionResult.success({
            "healthy": True,
            "total_shipments": len(items),
            "details": {"sample_count": len(items)},
            "summary": f"Manhattan Active WMS healthy. Sampled {len(items)} shipments."
        }, summary=f"Manhattan Active WMS health check passed with {len(items)} shipments.")
    except Exception as e:
        return ActionResult.error(f"Error auditing Manhattan Active WMS health: {e}")
