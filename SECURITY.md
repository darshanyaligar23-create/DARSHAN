# Security Policy

## Scope

MCP Hardware Inspector is an early-stage local read-only hardware metadata server. It is not a vulnerability scanner or a security audit tool.

## Reporting

Please report suspected vulnerabilities privately to the repository owner through GitHub's security advisory feature. Include affected version, operating system, reproduction steps, and impact. Do not include secrets, private IPs, serial numbers, or other sensitive host data unless essential.

## Safe operation

Use stdio with trusted MCP clients. Do not expose this server over a network or run it with elevated privileges. Review hardware and interface data before sharing it with an external model.
