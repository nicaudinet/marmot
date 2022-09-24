import rclpy

from pi_control.pi_control_node import PiControl

def main(args=None):
    rclpy.init(args=args)

    node = PiControl()

    rclpy.spin(node)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()