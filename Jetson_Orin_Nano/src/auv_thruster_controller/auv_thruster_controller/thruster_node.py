import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class ThrusterController(Node):

    def __init__(self):
        super().__init__('thruster_controller')

        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_callback,
            10
        )

    def cmd_callback(self, msg):
        forward = msg.linear.x
        yaw = msg.angular.z

        self.get_logger().info(
            f"Forward: {forward}  Yaw: {yaw}"
        )


def main(args=None):
    rclpy.init(args=args)

    node = ThrusterController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
