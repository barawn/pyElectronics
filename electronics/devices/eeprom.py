# programming class using pyElectronics
# for Si5341. Probably works with other clock modules too.
# I use pyElectronics because it's easy to create gateway stuff
# for various different devices so the same code works in multiple
# places and I am violently sick of constantly writing programming
# code for these damn clocks

from electronics.device import I2CDevice
from csv import DictReader
from time import sleep

class EEPROM(I2CDevice):
    def __init__(self, bus, address=0x50):
        super().__init__(bus, address)

    def read(self, addr, nb=1):
        d = bytes([addr])
        self.i2c_write(d)
        return self.i2c_read(nb)

    def write(self, addr, data, verbose=False):
        idx = 0
        pageData = data[8*idx:8*(idx+1)]
        while len(pageData) > 0:
            thisAddr = addr + idx*8            
            toWrite = bytes([thisAddr]) + bytes(pageData)
            if verbose:
                print(idx, ":", pageData.hex(), "-", toWrite.hex())
            self.i2c_write(toWrite)
            idx = idx + 1
            pageData = data[8*idx:8*(idx+1)]
