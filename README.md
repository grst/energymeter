# Monitoring energymeters and SMA devices using a Rasperry Pi Zero

I live in a house with four flats, each of which is owned by a different member of my family.
In 2024 we jointly invested in a 23kWp photovoltaics (PV) system with 22kWh battery storage. To optimally use the energy
across the entire house, we now only have one contract (and one electricity meter) with the grid operator. Behind
the main meter, the consumption of each flat is measured using an Eltako electricity meter (as shown below) which we
use to split the electricity cost.

With a PV system (and maybe in the future, dynamic tariffs), the cost per kWh is not fixed. It is basically
free when there's sun and expensive otherwise. Thus ideally, we could not only record _how much_ energy is consumed,
but also _when_. Like that we can learn more about our energy consumption, optimize it towards consuming more
self-generated energy, and split the cost more accurately.

Luckily, the Eltako meters can be read out via a S0-interface. This is a very simple interface that sends one electric pulse for each consumed Wh. 
Moreover, the SMA inverter and battery system can be queried using a Modbus interface via the local network. This project contains a Python
project I run on a Rasperry Pi zero to count the pulses received via S0 and to query the modbus interface in a fixed interval. The resulting
measurements are saved in a SQLite database that can be used for analyzing and visualzing the energy consumption and production. 

## Hardware setup

| Energy meter with S0 port | Rasperry Pi Zero |
| ------------- | ------------- |
| ![eltako meter](img/eltako_meter.jpg) | ![rasperry_pi](img/rasperry_pi.jpg) |

The S0 interface of the Eltako energy meters is connected to the GPIO ports of a Rasperry Pi zero. 
In principle every cable should do, but I use Ethernet cables for that because they are shielded and conveniently offer
twisted wire pairs. According to the S0 protocol, on pulse is sent by the energymeter every time a certain unit of energy is consumed.
This value depends on the meter, but in my case it's one pulse per Wh. Of each energy meter, the S0- port is connected to the GND of the raspberry pi. The S0+ port to any of
the GPIO ports. GPIO ports must be set to Pull-up. We can then detect a falling edge signal.

## Installation

You need to have Python 3.10 or newer installed on your system. If you don’t have Python installed, you can get it e.g. from [Mambaforge](https://github.com/conda-forge/miniforge#mambaforge).
Then, install the `energymeter` package from this git repo: 

```bash
git clone https://github.com/grst/energymeter.git
pip install -e ./energymeter
```

## Configuration

You need to configure your energymeters in `src/energymeter/config.yml`. It is distinguished between S0 (GPIO) and Modbus (TCP/IP) meters. Three types of measurements can be recorded that will be 
saved in different SQL Tables: 
 * Pulse (S0 pulse counter)
 * Power (current power in W)
 * CumulativePower (cumulative power, i.e. counter readout in Wh)

Example:

```yaml
meters:
  GPIO:
    Meter1:
      id: 1
      db_table: Pulse
      gpio_port: 21
      imp_per_kwh: 1000
  Modbus:
    Sunny_Tripower_curr_power:
      id: 2
      description: "Current PV Power (W)"
      db_table: CumulativePower
      modbus_register_address: 30775
      modbus_register_type: U32
      ip_address: 192.168.1.147
```

## How it works

-   `monitor.py` is a simple python script that waits for events being detected on any of the GPIO ports. On every event,
    an entry is written to the database.
-   `service.sh` is a wrapper script called by the systemd service
-   `energymonitor.service` is a systemd service file, that needs to be put into `/etc/systemd/system`.

To activate the service call

```
systemctl enable energymonitor.service
systemctl start energymonitor.service
```

It will be started automatically after a reboot.

Check the status with

```
systemctl status energymonitor.service
```
