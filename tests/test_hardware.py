from mcp_hardware_inspector import hardware


def test_cpu_info_shape():
    result = hardware.cpu_info()
    assert "logical_cpu_count" in result
    assert "architecture" in result


def test_memory_info_shape():
    result = hardware.memory_info()
    assert result["total_bytes"] >= 0
    assert result["available_bytes"] >= 0


def test_disk_info_is_list():
    assert isinstance(hardware.disk_info(), list)
