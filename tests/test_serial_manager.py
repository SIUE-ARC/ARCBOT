from unittest import TestCase
import serial

from libarcbot.serialmanager.serialmanager import SerialManager


class TestSerialManager(TestCase):
    """docstring for TestSerialManager."""
    __serial = None
    __serial_manager = None

    def test_send_command(self):
        # given a command
        command = "This is my command"
        # and a serial manager
        serial_manager = SerialManager.get_instance(True)
        # and the serial managers connection
        serial_connection = serial_manager.get_serial_connection()
        # send the command
        result = serial_manager.send_command(command)
        # get the number of bytes waiting
        waiting = serial_connection.in_waiting
        # waiting must be greater than 0
        self.assertEqual(waiting, 0)
        # check if the lengths are the same
        self.assertEqual(len(result), len(command))
        # the result should be equal to the command
        self.assertEqual(command.encode('ascii'), result)

    def test_send_command_with_callback(self):
        # given a command
        command = "This is my command"
        # and an incorrect command
        incorrect = "This is not right"
        # and a serial manager
        serial_manager = SerialManager.get_instance(True)
        # and a callback function

        def callback_check_function(result): return self.assertEqual(
            command.encode('ascii'), result)
        # and another callback for completeness

        def callback_check_function_2(result): return self.assertNotEqual(
            incorrect.encode('ascii'), result)
        # send the command and call the callback
        result = serial_manager.send_command(command, callback_check_function)
        # send the command and call the second callback
        result = serial_manager.send_command(
            command, callback_check_function_2)
