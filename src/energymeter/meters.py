"""Definitions of different types of meters"""

from abc import ABC, abstractmethod

# from dataclasses import KW_ONLY
from dataclasses import dataclass
from datetime import datetime
from typing import Literal, Union

from . import db, modbus


@dataclass
class Meter(ABC):
    id: int
    """Unique numeric id used to store results in the database"""
    #    _: KW_ONLY
    name: str
    description: str = None
    db_table: Literal["Pulse", "Power", "CumulativePower"] = None
    """Sqlalchemy type that represents a table into which the measurements shall be saved. Leave None if you don't want to record this meter"""

    @abstractmethod
    def get_event(self, value=None) -> Union[db.Pulse, db.Power, db.CumulativePower]:
        """Get a measurement object to be written in the database for this meter"""
        ...


@dataclass
class GPIOMeter(Meter):
    gpio_port: int = None
    """Rasperry pi GPIO port"""
    imp_per_kwh: int = None
    """Number of pulses sent via S0 per kWh"""

    def get_event(self, value=None) -> Union[db.Pulse, db.Power, db.CumulativePower]:
        return getattr(db, self.db_table)(meter_id=self.id, time=datetime.utcnow())


@dataclass
class ModbusMeter(Meter):
    modbus_register_address: int = None
    modbus_register_type: Literal["U32", "S32", "U64"] = None
    ip_address: str = None
    unit = 3
    """Modbus Unit. For SMA devices the default is 3"""

    def get_register(self) -> modbus.Register:
        """Get the modbus register object for this meter"""
        return getattr(modbus, self.modbus_register_type)(
            self.modbus_register_address, name=self.name, description=self.description
        )

    def get_event(self, value=None) -> Union[db.Pulse, db.Power, db.CumulativePower]:
        return getattr(db, self.db_table)(meter_id=self.id, time=datetime.utcnow(), value=value)
