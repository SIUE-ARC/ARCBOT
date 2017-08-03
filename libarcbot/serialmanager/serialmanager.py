import serial
import glob
import time

class SerialManager(object):
    """SerialManager Interface"""
    __testing = False
    __instance = None
    __connection_string = None
    __serial_connection = None
    __baudrate = 9600
    __arduino_greeting = "ohai"
    __arduino_reponse = "kthxbai"

    def __init__(self, testing=False):
        super(SerialManager, self).__init__()
        self.__testing = testing
        self.__serial_connection = self.__open_serial_connection()

    def __del__(self):
        if self.__serial_connection and self.__serial_connection.isOpen():
            self.__serial_connection.close()
            del(self.__serial_connection)

    @classmethod
    def get_instance(cls, testing=False):
        if SerialManager.__instance is None:
            SerialManager.__instance = SerialManager(testing)
        return SerialManager.__instance

    def get_connection_string(self):
        return self.__connection_string

    def get_serial_connection(self):
        return self.__serial_connection

    def __open_serial_connection(self):
        try:
            if self.__testing:
                self.__connection_string = "loop://"
                return serial.serial_for_url(self.__connection_string, timeout=1)
            else:
                self.__connection_string = self.__find_arduino_port()
                return serial.Serial(port=self.__connection_string, baudrate=self.__baudrate)
        except serial.SerialException as e:
            raise

    def __find_arduino_port(self):
        # given a list of ports
        ports = glob.glob('/dev/tty[A-Za-z]*')
        arduino = ""
        # iterate over each port
        for port in ports:
            if arduino != "":
                pass
            # try connecting to it
            try:
                # establish the connection
                conn = serial.Serial(port,self.__baudrate)
                # waith until the UNO resets because of the serial connection
                time.sleep(4)
                # attempt to send the "Hello" command
                conn.write(self.__arduino_greeting.encode('ascii'))
                time.sleep(1)
                # get the number of bytes waiting in the input buffer
                waiting = conn.inWaiting()
                # get the response
                response = conn.read(waiting)
                # if the response is the same as the expected response (as a Byte array)
                if response == self.__arduino_reponse.encode('ascii'):
                    # then this is the correct port
                    arduino = port
                # close the connection
                conn.close()
            except Exception as e:
                pass
        return arduino

    def send_command(self, command, callback=None):
        # given  command
        command = command.encode('ascii')
        # send the command
        self.__serial_connection.write(command)
        # get the number of bytes waiting in the input buffer
        waiting = self.__serial_connection.in_waiting
        # get the result
        result = self.__serial_connection.read(waiting)
        # if the callback is valid
        if callback is not None and callable(callback):
            # call it, given the result
            callback(result)
        else:
            # otherwise return the result
            return result
