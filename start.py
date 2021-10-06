from machine import WashingMachine
from threading import Thread
import sys, time

class StartandStop:
    def __init__(self):
        self.time_started = False

    def start(self):
        print("Machine is starting...")
        print("Machine has started!")

        self.machine = WashingMachine()
        while True:
            self.stopChoice()
            # Input statement for the machine
            self.option_value = input("Enter your Washing machine option \n")
            self.machine.changeOption(self.option_value)
            self.machine.control_center()
            
        
    def stop(self):
        print("Machine is stopping...")
        del self.machine
        print("Machine has stopped!")
        sys.exit(0)
        
    def stopChoice(self):
        stop_choice = input("Do you want to stop the choice, yes or no \n")
        if stop_choice.lower() in ["y", "yes"]:
            self.stop()

controller = StartandStop()
controller.start()