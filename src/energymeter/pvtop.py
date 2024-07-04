"""Command line monitoring tool for photovolatics"""

from importlib.resources import files

import yaml

from ._util import _connect_to_modbus, _load_meters
from .meters import ModbusMeter


def main():
    with (files("energymeter") / "config.yml").open() as f:
        CONFIG = yaml.safe_load(f)

    modbus_meters: list[ModbusMeter] = _load_meters(CONFIG["meters"]["Modbus"], ModbusMeter)
    modbus_connections = _connect_to_modbus(modbus_meters)
    print("Beschreibung\tWert")
    for meter in modbus_meters:
        modbus_client = modbus_connections[meter.ip_address]
        value = modbus_client.read_modbus(meter.get_register(), unit=meter.unit)
        print(f"{meter.description}\t{value}")


if __name__ == "__main__":
    main()
