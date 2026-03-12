import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from geometry_msgs.msg import Twist

class AutonomyNode(Node):

    def __init__(self):
        super().__init__('autonomy_node')

        self.subscription = self.create_subscription(
            Float32,
            '/sonar_distance',
            self.sonar_callback,
            10)

        self.publisher = self.create_publisher(
            Twist,
            '/cmd_vel',
            10)

    def sonar_callback(self, msg):

        distance = msg.data
        twist = Twist()

        if distance < 2.0:
            twist.angular.z = 0.5
            twist.linear.x = 0.0
            self.get_logger().info("Obstacle detected → turning")

        else:
            twist.linear.x = 1.0
            twist.angular.z = 0.0
            self.get_logger().info("Path clear → moving forward")

        self.publisher.publish(twist)


def main(args=None):

    rclpy.init(args=args)

    node = AutonomyNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
