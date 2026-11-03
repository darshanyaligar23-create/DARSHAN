"""Portable, read-only host metadata helpers."""
from __future__ import annotations
import platform
import socket
import psutil


def cpu_info() -> dict:
    """Return basic CPU metadata without executing external commands."""
    return {
        "processor": platform.processor() or None,
        "architecture": platform.machine() or None,
        "logical_cpu_count": psutil.cpu_count(logical=True),
        "physical_cpu_count": psutil.cpu_count(logical=False),
    }


def memory_info() -> dict:
    """Return system memory capacity in bytes."""
    m = psutil.virtual_memory()
    return {"total_bytes": m.total, "available_bytes": m.available, "used_bytes": m.used, "percent_used": m.percent}


def disk_info() -> list[dict]:
    """Return mounted filesystem capacity metadata; device paths may be sensitive."""
    rows = []
    for p in psutil.disk_partitions(all=False):
        try:
            u = psutil.disk_usage(p.mountpoint)
        except (PermissionError, OSError):
            continue
        rows.append({"mountpoint": p.mountpoint, "filesystem": p.fstype, "total_bytes": u.total, "used_bytes": u.used, "free_bytes": u.free})
    return rows


def network_interfaces() -> list[dict]:
    """Return local interface names and addresses; does not scan or contact networks."""
    rows = []
    for name, addrs in psutil.net_if_addrs().items():
        rows.append({"name": name, "addresses": [{"family": str(a.family), "address": a.address} for a in addrs if a.address]})
    return rows


def hardware_summary() -> dict:
    """Return a compact summary assembled from the other read-only tools."""
    return {"system": platform.system(), "release": platform.release(), "version": platform.version(), "hostname": socket.gethostname(), "cpu": cpu_info(), "memory": memory_info(), "disks": disk_info()}
