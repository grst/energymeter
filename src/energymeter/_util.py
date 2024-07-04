from .meters import Meter, ModbusMeter
from .modbus import Modbus


def _load_meters(meter_configs: list[dict], meter_type: type[Meter], with_db_table: bool = False) -> list[Meter]:
    """
    Convert configuration file into meter objects.

    If with_db_table is True, only meters that have a db_table argument that is not None
    will be returned.
    """
    meters = []
    for name, config in meter_configs.items():
        config["name"] = name
        meter = meter_type(**config)
        if not with_db_table or meter.db_table is not None:
            meters.append(meter)
    return meters


def _connect_to_modbus(meters: list[ModbusMeter]):
    """Go through all configs and make create one modbus connection for each unique IP"""
    modbus_connections = {}
    for meter in meters:
        if meter.ip_address not in modbus_connections:
            modbus_connections[meter.ip_address] = Modbus(meter.ip_address)
    return modbus_connections
