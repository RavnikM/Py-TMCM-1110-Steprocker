import serial
import struct
from threading import Lock

class Steprocker():
    def __init__(self,port):
        self.lock = Lock()
        self.serial = serial.Serial(port=port,
                            baudrate=9600,
                            bytesize=serial.EIGHTBITS,
                            parity=serial.PARITY_NONE,
                            stopbits=serial.STOPBITS_ONE,
                            timeout=None) # behavior of read(x) -> wait forever / until requested number of bytes are received


    def __del__(self):
        if self.serial.isOpen():
            self.serial.close()


    def rs232_checksum(self,the_bytes):
        value = b'%02X' % (sum(the_bytes) & 0xFF)
        return struct.pack(">B", int(value,16))


    def get_maximum_positioning_speed(self):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x06 - Instruction number (6 = GAP(Get axis parameter))
        # x04 - Type (4 = Maximum positioning speed)
        # x00 - Motor / Bank
        # x00 - Value byte3  (not used)
        # x00 - Value byte2  (not used)
        # x00 - Value byte1  (not used)
        # x00 - Value byte0  (not used)
        try:
            self.lock.acquire()
            packet = b'\x01\x06\x04\x00\x00\x00\x00\x00'
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            return struct.unpack('>i', reply[4:8])[0]
        finally:
            self.lock.release()


    def set_maximum_positioning_speed(self, value):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x05 - Instruction number (5 = SAP(Set axis parameter))
        # x04 - Type (4 = Maximum positioning speed)
        # x00 - Motor / Bank
        # Variabilni del
        # Value byte3
        # Value byte2
        # Value byte1
        # Value byte0
        try:
            self.lock.acquire()
            fixed_part = b'\x01\x05\x04\x00'
            uvalue_bytes = struct.pack(">i", value)
            packet = fixed_part + uvalue_bytes
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            if reply[2] == 100:
                return True
            else:
                return False
        finally:
            self.lock.release()


    def get_maximum_acceleration(self):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x06 - Instruction number (6 = GAP(Get axis parameter))
        # x05 - Type (5 = Maximum acceleration)
        # x00 - Motor / Bank
        # x00 - Value byte3  (not used)
        # x00 - Value byte2  (not used)
        # x00 - Value byte1  (not used)
        # x00 - Value byte0  (not used)
        try:
            self.lock.acquire()
            packet = b'\x01\x06\x05\x00\x00\x00\x00\x00'
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            return struct.unpack('>i', reply[4:8])[0]
        finally:
            self.lock.release()


    def set_maximum_acceleration(self, value):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x05 - Instruction number (5 = SAP(Set axis parameter))
        # x05 - Type (5 = Maximum acceleration)
        # x00 - Motor / Bank
        # Variabilni del
        # Value byte3
        # Value byte2
        # Value byte1
        # Value byte0
        try:
            self.lock.acquire()
            fixed_part = b'\x01\x05\x05\x00'
            uvalue_bytes = struct.pack(">i", value)
            packet = fixed_part + uvalue_bytes
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            if reply[2] == 100:
                return True
            else:
                return False
        finally:
            self.lock.release()


    def get_actual_position(self):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x06 - Instruction number (6 = GAP(Get axis parameter))
        # x01 - Type (1 = Actual position)
        # x00 - Motor / Bank
        # x00 - Value byte3  (not used)
        # x00 - Value byte2  (not used)
        # x00 - Value byte1  (not used)
        # x00 - Value byte0  (not used)
        try:
            self.lock.acquire()
            packet = b'\x01\x06\x01\x00\x00\x00\x00\x00'
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            return struct.unpack('>i', reply[4:8])[0]
        finally:
            self.lock.release()


    def set_actual_position(self, value):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x05 - Instruction number (5 = SAP(Set axis parameter))
        # x01 - Type (1 = Actual position)
        # x00 - Motor / Bank
        # Variabilni del
        # Value byte3
        # Value byte2
        # Value byte1
        # Value byte0
        try:
            self.lock.acquire()
            fixed_part = b'\x01\x05\x01\x00'
            uvalue_bytes = struct.pack(">i", value)
            packet = fixed_part + uvalue_bytes
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            if reply[2] == 100:
                return True
            else:
                return False
        finally:
            self.lock.release()


    def get_target_position(self):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x06 - Instruction number (6 = GAP(Get axis parameter))
        # x00 - Type (1 = Target position)
        # x00 - Motor / Bank
        # Variabilni del
        # x00 - Value byte3 (not used)
        # x00 - Value byte2 (not used)
        # x00 - Value byte1 (not used)
        # x00 - Value byte0 (not used)
        try:
            self.lock.acquire()
            packet = b'\x01\x06\x00\x00\x00\x00\x00\x00'
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            return struct.unpack('>i', reply[4:8])[0]
        finally:
            self.lock.release()


    def set_target_position(self, value):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x05 - Instruction number (5 = SAP(Set axis parameter))
        # x00 - Type (0 = Target position)
        # x00 - Motor / Bank
        # Variabilni del
        # Value byte3
        # Value byte2
        # Value byte1
        # Value byte0
        try:
            self.lock.acquire()
            fixed_part = b'\x01\x05\x00\x00'
            uvalue_bytes = struct.pack(">i", value)
            packet = fixed_part + uvalue_bytes
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            if reply[2] == 100:
                return True
            else:
                return False
        finally:
            self.lock.release()


    def get_run_current(self):
        # Fiksni del
        # x01 - Target address 1 = board number
        # x06 - Instruction number 5 = GAP(Get axis parameter)
        # x06 - Type 6 = run currnet
        # x00 - Motor / Bank
        # Variabilni del
        # x00 - Value byte3 (not used)
        # x00 - Value byte2 (not used)
        # x00 - Value byte1 (not used)
        # x00 - Value byte0 (not used)
        try:
            self.lock.acquire()
            packet = b'\x01\x06\x06\x00\x00\x00\x00\x00'
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            return reply[7]
        finally:
            self.lock.release()


    def set_run_current(self, value):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x05 - Instruction number (5 = SAP(Set axis parameter))
        # x06 - Type (6 = run currnet)
        # x00 - Motor / Bank
        # Variabilni del
        # x00 - Value byte3 - not used
        # x00 - Value byte2 - not used
        # x00 - Value byte1 - not used
        # Value byte0 - parameter value 0..255
        try:
            self.lock.acquire()
            fixed_part = b'\x01\x05\x06\x00\x00\x00\x00'
            uvalue_bytes = struct.pack("B", value)
            packet = fixed_part + uvalue_bytes
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            if reply[2] == 100:
                return True
            else:
                return False
        finally:
            self.lock.release()


    def get_standby_current(self):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x06 - Instruction number (6 = GAP(Get axis parameter))
        # x07 - Type (7 = standby currnet)
        # x00 - Motor / Bank
        # Variabilni del
        # x00 - Value byte3 - not used
        # x00 - Value byte2 - not used
        # x00 - Value byte1 - not used
        # x00 - Value byte0 - not used
        try:
            self.lock.acquire()
            packet = b'\x01\x06\x07\x00\x00\x00\x00\x00'
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            return reply[7]
        finally:
            self.lock.release()


    def set_standby_current(self, value):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x05 - Instruction number (5 = SAP(Set axis parameter))
        # x07 - Type (7 = standby currnet)
        # x00 - Motor / Bank
        # Variabilni del
        # x00 - Value byte3 - not used
        # x00 - Value byte2 - not used
        # x00 - Value byte1 - not used
        # Value - Value byte0 - parameter value 0..255
        try:
            self.lock.acquire()
            fixed_part = b'\x01\x05\x07\x00\x00\x00\x00'
            uvalue_bytes = struct.pack("B", value)
            packet = fixed_part + uvalue_bytes
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            if reply[2] == 100:
                return True
            else:
                return False
        finally:
            self.lock.release()


    def get_micro_steps(self, return_str=False):
        # microsteps0..8
        # Microstep resolutions per full step:
        # 0 fullstep
        # 1 halfstep
        # 2 4 microsteps
        # 3 8 microsteps
        # 4 16 microsteps
        # 5 32 microsteps
        # 6 64 microsteps
        # 7 128 microsteps
        # 8 256 microsteps

        # Fiksni del
        # x01 - Target address (1 = board number)
        # x06 - Instruction number (6 = GAP(Get axis parameter))
        # x8C - Type (140 = get microsteps)
        # x00 - Motor / Bank
        # Variabilni del
        # x00 - Value byte3 - not used
        # x00 - Value byte2 - not used
        # x00 - Value byte1 - not used
        # x00 - Value byte0 - not used
        try:
            self.lock.acquire()
            packet = b'\x01\x06\x8C\x00\x00\x00\x00\x00'
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)

            if reply[7] == 0:
                if not return_str:
                    return 1
                else:
                    return 'full-steps'
            elif reply[7] == 1:
                if not return_str:
                    return 2
                else:
                    return 'half-steps'
            elif reply[7] == 2:
                if not return_str:
                    return 4
                else:
                    return '4-microsteps'
            elif reply[7] == 3:
                if not return_str:
                    return 8
                else:
                    return '8-microsteps'
            elif reply[7] == 4:
                if not return_str:
                    return 16
                else:
                    return '16-microsteps'
            elif reply[7] == 5:
                if not return_str:
                    return 32
                else:
                    return '32-microsteps'
            elif reply[7] == 6:
                if not return_str:
                    return 64
                else:
                    return '64-microsteps'
            elif reply[7] == 7:
                if not return_str:
                    return 128
                else:
                    return '128-microsteps'
            elif reply[7] == 8:
                if not return_str:
                    return 256
                else:
                    return '256-microsteps'
        finally:
            self.lock.release()


    def set_micro_steps(self, value):
        # microsteps 0..8
        # Microstep resolutions per full step:
        # 0 - fullstep
        # 1 - halfstep
        # 2 - 4 microsteps
        # 3 - 8 microsteps
        # 4 - 16 microsteps
        # 5 - 32 microsteps
        # 6 - 64 microsteps
        # 7 - 128 microsteps
        # 8 - 256 microsteps

        if value == 1:
            true_value = 0
        elif value == 2:
            true_value = 1
        elif value == 4:
            true_value = 2
        elif value == 8:
            true_value = 3
        elif value == 16:
            true_value = 4
        elif value == 32:
            true_value = 5
        elif value == 64:
            true_value = 6
        elif value == 128:
            true_value = 7
        elif value == 256:
            true_value = 8

        # Fiksni del
        # x01 - Target address 1 = board number
        # x05 - Instruction number (5 = SAP(Set axis parameter))
        # x8C - Type 140 = set microsteps
        # x00 - Motor / Bank
        # Variabilni del
        # x00 - Value byte3 - not used
        # x00 - Value byte2 - not used
        # x00 - Value byte1 - not used
        # Value - Value byte0 - parameter value 0..8
        try:
            self.lock.acquire()
            fixed_part = b'\x01\x05\x8C\x00\x00\x00\x00'
            uvalue_bytes = struct.pack("B", true_value)
            packet = fixed_part + uvalue_bytes
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            if reply[2] == 100:
                return True
            else:
                return False
        finally:
            self.lock.release()


    def get_target_position_reached(self):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x06 - Instruction number (6 = GAP(Get axis parameter))
        # x08 - Type (8 = Target position reached flag)
        # x00 - Motor / Bank
        # Variabilni del
        # x00 - Value byte3 - not used
        # x00 - Value byte2 - not used
        # x00 - Value byte1 - not used
        # x00 - Value byte0 - not used
        try:
            self.lock.acquire()
            packet = b'\x01\x06\x08\x00\x00\x00\x00\x00'
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            if reply[7] == 1:
                return True
            elif reply[7] == 0:
                return False
        finally:
            self.lock.release()


    def motor_stop(self):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x03 - Instruction number (3 = MST(Motor Stop))
        # x00 - Type (0 - not used)
        # x00 - Motor / Bank
        # Variabilni del
        # x00 - Value byte3 - not used
        # x00 - Value byte2 - not used
        # x00 - Value byte1 - not used
        # x00 - Value byte0 - not used
        try:
            self.lock.acquire()
            packet = b'\x01\x03\x00\x00\x00\x00\x00\x00'
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            if reply[2] == 100:
                return True
            else:
                return False
        finally:
            self.lock.release()


    def movetopos_abs(self,microsteps, calculate_to_fullsteps=False):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x04 - Instruction number (4 = MVP(Move to Position))
        # x00 - Type (0 = ABSolute)
        # x00 - Motor / Bank
        # Variabilni del
        # Value byte3
        # Value byte2
        # Value byte1
        # Value byte0
        try:
            if calculate_to_fullsteps:
                microsteps = microsteps * self.get_micro_steps()

            self.lock.acquire()
            fixed_part = b'\x01\x04\x00\x00'
            usteps_bytes = struct.pack(">i", microsteps)
            packet = fixed_part + usteps_bytes
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            if reply[2] == 100:
                return True
            else:
                return False
        finally:
            self.lock.release()


    def movetopos_rel(self,microsteps, calculate_to_fullsteps=False):
        # Fiksni del
        # x01 - Target address (1 = board number)
        # x04 - Instruction number (4 = MVP(Move to Position))
        # x01 - Type (1 = Relative)
        # x00 - Motor / Bank
        # Variabilni del
        # Value byte3
        # Value byte2
        # Value byte1
        # Value byte0
        try:
            if calculate_to_fullsteps:
                microsteps = microsteps * self.get_micro_steps()
            self.lock.acquire()
            fixed_part = b'\x01\x04\x01\x00'
            usteps_bytes = struct.pack(">i", microsteps)
            packet = fixed_part + usteps_bytes
            packet = packet + self.rs232_checksum(packet)
            self.serial.write(packet)
            reply = self.serial.read(9)
            if reply[2] == 100:
                return True
            else:
                return False
        finally:
            self.lock.release()