import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import time

class NodeDefault(Node):
    def __init__(self):
        super().__init__('node_name_1')
        self.publisher_string = self.create_publisher(
            msg_type=String,
            topic='topic_name_1',
            qos_profile=10
        )
        self.msg_string = String()

        self.main()

    def func_pub(self, text):
        self.msg_string.data = text
        self.publisher_string.publish( self.msg_string )

    def main(self):
        num =0
        while True:
            self.func_pub(str(num))
            num += 1
            time.sleep(1)

def main():
    rclpy.init()
    node = NodeDefault()

    rclpy.spin( node )

    node.destroy_node()
    rclpy.shutdown()


if __name__=="__main__":
    main()