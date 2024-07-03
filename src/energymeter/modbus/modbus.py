from pymodbus.client.sync import ModbusTcpClient
from .register import Register
from threading import Lock


class Modbus:
    def __init__(self, ip, timeout=4):
        self.client = ModbusTcpClient(ip, timeout=timeout)
        self.lock = Lock()
        self.client.connect()

    def read_modbus(self, register: Register, unit: int):
        """Read a register via modbus. This function is thread-safe"""
        with self.lock:
            response = self.client.read_holding_registers(register.id, register.length, unit=unit)
            register.set_registers(response.registers)
            value = register.get_value()
            return value
