from .meters import Meter, ModbusMeter
from .modbus import Modbus


def _load_meters(meter_configs: list[dict], meter_type: type[Meter]) -> list[Meter]:
    """Convert configuration file into meter objects"""
    meters = []
    for name, config in meter_configs.items():
        config["name"] = name
        meters.append(meter_type(**config))
    return meters


def _connect_to_modbus(meters: list[ModbusMeter]):
    """Go through all configs and make create one modbus connection for each unique IP"""
    modbus_connections = {}
    for meter in meters:
        if meter.ip_address not in modbus_connections:
            modbus_connections[meter.ip_address] = Modbus(meter.ip_address)
    return modbus_connections
