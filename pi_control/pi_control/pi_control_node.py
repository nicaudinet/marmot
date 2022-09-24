from rclpy.node import Node

class PiControl(Node):

    def __init__(self):
        super().__init__('pi_control')

        self.run_test()

    def run_test(self):
        print("lesgooo")