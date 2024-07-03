"""Command line monitoring tool for photovolatics"""

from importlib.resources import files

import yaml

from . import modbus
from ._util import MODBUS_UNIT, _connect_to_modbus


def main():
    with (files("energymeter") / "config.yml").open() as f:
        CONFIG = yaml.safe_load(f)

    modbus_connections = _connect_to_modbus(CONFIG["meters"])
    print("Beschreibung\tWert")
    for meter_id, params in CONFIG["meters"].items():
        if "modbus" in params:
            modbus_client = modbus_connections[params["ip"]]
            register_type = getattr(modbus, params["modbus_type"])
            register = register_type(params["modbus"], name=meter_id, description=params["description"])
            value = modbus_client.read_modbus(register, unit=MODBUS_UNIT)
            print(f"{params['description']}\t{value}")


if __name__ == "__main__":
    main()
