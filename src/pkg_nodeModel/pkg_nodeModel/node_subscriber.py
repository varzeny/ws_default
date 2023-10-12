import rclpy
from rclpy.node import Node
import std_msgs.msg

class NodeDefault(Node):
    def __init__(self):
        super().__init__('node_name_2')
        self.subscriber_default = self.create_subscription(
            msg_type=std_msgs.msg.String,
            topic='topic_name_1',
            callback=self.callback_1,
            qos_profile=10
        )

    def callback_1(self, msg):
        self.get_logger().info( msg.data )


def main():
    rclpy.init()
    node = NodeDefault()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__=="__main__":
    main()