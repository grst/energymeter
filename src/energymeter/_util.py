from .modbus import Modbus

MODBUS_UNIT = 3


def _connect_to_modbus(configs: dict):
    """Go through all configs and make create one modbus connection for each unique IP"""
    modbus_connections = {}
    for params in configs.values():
        if "modbus" in params:
            ip = params["ip"]
            if ip not in modbus_connections:
                modbus_connections[ip] = Modbus(ip)
    return modbus_connections
