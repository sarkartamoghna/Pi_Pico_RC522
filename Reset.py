import machine
rst = machine.Pin(0, machine.Pin.OUT)
rst.value(1)  # Pull RST HIGH
