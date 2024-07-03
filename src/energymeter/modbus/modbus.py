import time
from threading import Lock, Thread

from pymodbus.client.sync import ModbusTcpClient
from Register import Register


class Modbus:
    def __init__(self, *, unit: int, address: str, port: int, interval):
        self.thread = Thread(target=self._polling_thread)
        self.register_lock = Lock()
        self.registers: list[int] = []
        self.available_registers: dict[int, Register] = {}
        self.unit = unit
        self.client = ModbusTcpClient(address, port=port, timeout=10)
        self.polling_groups = []
        self.daemon = args.daemon
        self.interval = args.interval

        self.gui = None
        self.logger = None

    def __del__(self):
        self.client.close()

    def connect(self):
        self.client.connect()

    def poll_register(self, register_id: int):
        if register_id not in self.registers:
            if register_id not in self.available_registers:
                print(f"Register with the id {register_id} does not exist")
            else:
                register = self.available_registers[register_id]
                self.registers.append(register_id)  # war register_id

    def add_register(self, register: Register):
        self.available_registers[register.id] = register

    def start(self):
        self._group_register()

        self.connect()

        if self.daemon:
            self.thread.daemon = True
            self.thread.start()
            if self.gui:
                self.gui.run()
            else:
                while True:
                    time.sleep(self.interval)
        else:
            return self._poll()

    def list_available_registers(self):
        for index, register in self.available_registers.items():
            print(register)

    def _poll(self):
        result = {}
        for group in self.polling_groups:
            start_id = group[0].id
            length = self._length_of_group(group)
            first_register = group[0]

            response = self.client.read_holding_registers(start_id, length, unit=self.unit)

            if response:
                for index in range(len(group)):
                    register = group[index]
                    start_index = sum(register.length for register in group[0:index])

                    chunk = response.registers[start_index : start_index + register.length]
                    register.set_registers(chunk)
                    value = register.get_value()

                    if register.is_null():
                        value = "NAN"

                    result[register] = value
                    print(f"Register {register} has value {value}")
        if self.gui:
            self.gui.update(result)
        else:
            if self.logger:
                self.logger.log(result)
        return result

    def _length_of_group(self, group):
        return sum(reg.length for reg in group)

    def _polling_thread(self):
        while True:
            with self.register_lock:
                self._poll()
                time.sleep(self.interval)

    def _group_register(self):
        if len(self.registers) == 0:
            return

        self.registers.sort()

        polling_groups = [[]]

        next_id = self.registers[0]
        for id in self.registers:
            register = self.available_registers[id]

            if register == None:
                continue

            if next_id != id:
                polling_groups.append([])

            current_group = polling_groups[len(polling_groups) - 1]
            current_group.append(register)
            next_id = register.id + register.length

        self.polling_groups = polling_groups
