class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    # !r will put '' in the variable like: 'variable'
    def __str__(self):
        return f'Device {self.name!r} via {self.connected_by!r} connected [{self.connected!r}]'

    def disconnect(self):
        self.connected = False

    def connect(self):
        self.connected = True


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f'{super().__str__()} capacity [{self.capacity}] capacity now [{self.remaining_pages}]'

    def printer_print(self, pages):
        if not self.connected:
            print('Your device is not connected to print some page')
            return
        self.remaining_pages -= int(pages)


device = Device('keyboard', 'usb')
device.disconnect()
print(device)

print('-----------')

printerDevice = Printer(name='headset', connected_by='usb', capacity=100)
print(printerDevice)
printerDevice.printer_print(4)
print(printerDevice)
printerDevice.disconnect()
print(printerDevice)
printerDevice.printer_print(2)
