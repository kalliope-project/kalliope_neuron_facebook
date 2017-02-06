import unittest

from kalliope.core.NeuronModule import MissingParameterException
from kalliope.neurons.facebook_manager.facebook_manager import Facebook_manager


class TestSlack(unittest.TestCase):
    def setUp(self):
        self.action = "POST"
        self.token = "kalliokey"
        self.message = "kalliomessage"

    def testParameters(self):
        def run_test(parameters_to_test):
            with self.assertRaises(MissingParameterException):
                Facebook_manager(**parameters_to_test)

        # empty
        parameters = dict()
        run_test(parameters)

        # Missing action
        parameters = {
            "token": self.token,
            "message": self.message
        }
        run_test(parameters)

        # Missing token
        parameters = {
            "action": self.action,
            "message": self.message
        }
        run_test(parameters)


        # Missing message
        parameters = {
            "action": self.action,
            "token": self.token
        }
        run_test(parameters)
