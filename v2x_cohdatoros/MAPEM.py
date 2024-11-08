from v2x_cohdainterfaces.msg import *
from rclpy.node import Node
from .JSONtoMAPEM import *

class MAPEMPublisher(Node):

    def __init__(self):
        super().__init__('MAPEM_Publisher')
        self.Publisher = self.create_publisher(Mapem, 'Cohda_Signals/MAPEM', 10)
    
    def send(self, data):
        # Convert the JSON Data to msg
        msg = JSONtoMAPEM(data)
        # Publish the message
        self.Publisher.publish(msg)
        # Log
        self.get_logger().info("Published Mapem")