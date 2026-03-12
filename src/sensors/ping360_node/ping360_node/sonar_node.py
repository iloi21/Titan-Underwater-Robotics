import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random


class Ping360Node(Node):

    def __init__(self):
        super().__init__('ping360_node')

        self.publisher = self.create_publisher(Float32, '/sonar_distance', 10)

        self.timer = self.create_timer(1.0, self.publish_fake_scan)

    def publish_fake_scan(self):

        msg = Float32()
        msg.data = random.uniform(1.0, 5.0)

        self.publisher.publish(msg)

        self.get_logger().info(f"Sonar distance: {msg.data}")


def main(args=None):
    rclpy.init(args=args)
    node = Ping360Node()
    rclpy.spin(node)
    rclpy.shutdown()
