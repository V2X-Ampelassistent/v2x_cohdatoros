from v2x_cohdainterfaces.msg import *
from rclpy.node import Node
from .JSONtoSPATEM import *

class SPATEMPublisher(Node):

    def __init__(self):
        super().__init__('SPATEM_Publisher')
        self.Publisher = self.create_publisher(Spatem, 'Cohda_Signals/SPATEM', 10)

    def send(self, data):
        # Convert the JSON Data to msg
        msg = JSONtoSPATEM(data)
        # Publish the message
        self.Publisher.publish(msg)
        # Log
        self.get_logger().info("Published Spatem")