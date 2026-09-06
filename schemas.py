"""Pydantic schemas for Manhattan Active WMS Connector."""
from __future__ import annotations
from typing import Any, Optional, List, Dict
from pydantic import BaseModel, Field

class NoParams(BaseModel):
    """Empty parameters model."""
    pass

class ConnectParams(BaseModel):
    label: str = Field(default="", description="Friendly connection label, e.g. Primary Manhattan Active WMS.")
    api_key: str = Field(description="Logistics API Key / Access Token")
    base_url: str = Field(default="https://api.manh.com/wms/v1", description="Manhattan Active WMS API base URL.")

class ConnectionIdParams(BaseModel):
    connection_id: str = Field(default="", description="Connection identifier (empty uses active connection).")

class ConnectionRecord(BaseModel):
    id: str
    label: str
    masked_key: str
    base_url: str
    is_active: bool

class ConnectionList(BaseModel):
    connections: list[ConnectionRecord]
    total: int

class DeleteResult(BaseModel):
    success: bool
    message: str

class ShipmentRecord(BaseModel):
    id: str
    name: Optional[str] = None
    status: Optional[str] = None
    created_at: Optional[str] = None
    raw: Dict[str, Any] = Field(default_factory=dict)

class ShipmentList(BaseModel):
    shipments: list[ShipmentRecord]
    total: int

class ListShipmentParams(BaseModel):
    connection_id: str = Field(default="", description="Optional connection ID.")
    limit: int = Field(default=20, ge=1, le=100, description="Max records to return.")

class GetShipmentParams(BaseModel):
    connection_id: str = Field(default="", description="Optional connection ID.")
    shipment_id: str = Field(description="Manhattan Active WMS Shipment ID.")

class AuditHealthReport(BaseModel):
    healthy: bool
    total_shipments: int
    details: Dict[str, Any] = Field(default_factory=dict)
    summary: str
