import rclpy
from rclpy.node import Node

class PiControl(Node):

    def __init__(self):
        super().__init__('pi_control')
        self.get_logger().info('lesgoo')
        self.run_test()

    def run_test(self):
        self.get_logger().info('lesgoo 3')