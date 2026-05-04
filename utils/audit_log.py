"""Append-only in-memory audit log for SQL preview and execution."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class AuditEntry:
    at_iso: str
    kind: str  # generated | executed | error
    statement: str


def now_iso() -> str:
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

