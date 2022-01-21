from pymodbus.client.sync import ModbusTcpClient as ModbusClient

client = ModbusClient('63.42.236.101', port=502)

client.connect()

#  Prostar address defaults to 0x1
rr = client.read_input_registers(0xE000, 1, unit=1)