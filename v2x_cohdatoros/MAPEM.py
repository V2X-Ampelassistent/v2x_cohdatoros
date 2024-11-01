from v2x_cohdainterfaces.msg import *
from rclpy.node import Node

class MAPEMPublisher(Node):

    def __init__(self):
        super().__init__('MAPEM_Publisher')
        self.Publisher = self.create_publisher(MAPEM, 'Cohda_Signals/MAPEM', 10)

    def _json_to_msg(self, json_string):
        # TBD
        # Temporary:
        msg = MAPEM()
        msg.mapem = str(json_string)

        return msg
    
    def send(self, data):
        # Convert the JSON Data to msg
        msg = self._json_to_msg(data)
        # Publish the message
        self.Publisher.publish(msg)
        # Log
        self.get_logger().info("Published Mapem")