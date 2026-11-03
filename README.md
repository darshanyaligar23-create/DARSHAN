# MCP Hardware Inspector

A local-first, read-only Model Context Protocol (MCP) server for inspecting host hardware and system facts. It exposes a small, explicit set of tools for CPU, memory, disks, platform, and network-interface metadata.

> **Status:** early scaffold. Hardware coverage varies by operating system; values may be unavailable. This project does not claim to detect every device or provide a security audit.

## Safety and privacy

- Read-only inspection; no shell execution, writes, firmware changes, or device control.
- No network calls or telemetry from the server.
- Network tools report interface metadata only; they do not scan hosts or networks.
- Treat tool output as potentially sensitive before sharing it with an AI service.
- Run with least privilege. Do not expose the MCP server to untrusted clients.

## Quick start

Requires Python 3.11+.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -e .
python -m mcp_hardware_inspector
```

The server uses stdio transport. Configure your MCP client to launch the command `python -m mcp_hardware_inspector` from this repository's environment.

## Tools

- `hardware_summary`: platform, CPU, memory, and disk overview.
- `cpu_info`: logical CPU count and available processor metadata.
- `memory_info`: total/available memory when supported.
- `disk_info`: mounted filesystem capacity metadata.
- `network_interfaces`: interface names and addresses (can reveal local network details).

## Development

```bash
pip install -e ".[dev]"
pytest
```

Contributions welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md). Licensed under MIT; see [LICENSE](LICENSE).

## Roadmap

Cross-platform tests, richer hardware sensors, packaging, and release automation are planned. Please open an issue with OS/version and sanitized diagnostic output when reporting gaps.
