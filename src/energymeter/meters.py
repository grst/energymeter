"""Definitions of different types of meters"""

from dataclasses import KW_ONLY, dataclass
from typing import Literal

from . import modbus


@dataclass
class Meter:
    id: int
    """Unique numeric id used to store results in the database"""
    _: KW_ONLY
    name: str
    description: str = None
    db_table: Literal["Pulse", "Power", "CumulativePower"] = None
    """Sqlalchemy type that represents a table into which the measurements shall be saved. Leave None if you don't want to record this meter"""


@dataclass
class GPIOMeter(Meter):
    gpio_port: int
    """Rasperry pi GPIO port"""
    imp_per_kwh: int
    """Number of pulses sent via S0 per kWh"""


@dataclass
class ModbusMeter(Meter):
    modbus_register_address: int
    modbus_register_type: Literal["U32", "S32", "U64"]
    ip_address: str
    unit = 3
    """Modbus Unit. For SMA devices the default is 3"""

    def get_register_type(self) -> type:
        """Get the register type as type object"""
        return getattr(modbus, self.modbus_register_type)
