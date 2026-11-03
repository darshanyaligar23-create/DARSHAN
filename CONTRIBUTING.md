# Contributing

Thanks for helping improve MCP Hardware Inspector.

1. Open an issue describing the OS, Python version, expected behavior, and sanitized output.
2. Keep changes read-only and avoid shelling out where a maintained library provides the data.
3. Add tests for new platform-specific behavior and handle missing permissions gracefully.
4. Run `pytest` and `ruff check .` before submitting a pull request.
5. Never include real device identifiers, credentials, or private host/network details in fixtures.
