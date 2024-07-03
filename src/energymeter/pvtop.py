"""Command line monitoring tool for photovolatics"""

from importlib.resources import files

import modbus
import yaml

from .main import _connect_to_modbus


def main():
    with (files("energymeter") / "config.yml").open() as f:
        CONFIG = yaml.safe_load(f)

    modbus_connections = _connect_to_modbus(CONFIG["meters"])
    for meter_id, params in CONFIG["meters"].items():
        if "modbus" in params:
            modbus_client = modbus_connections[params["ip"]]
            register_type = getattr(modbus, params["modbus_type"])
            register = register_type(params["modbus"])
            value = modbus_client.read_modbus(register)
            print(f"{meter_id}\t{value}")


if __name__ == "__main__":
    main()
