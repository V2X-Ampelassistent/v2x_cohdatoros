from v2x_cohdainterfaces.msg import *
from rclpy.node import Node

class SPATEMPublisher(Node):

    def __init__(self):
        super().__init__('SPATEM_Publisher')
        self.Publisher = self.create_publisher(SPAT, 'Cohda_Signals/SPAT', 10)

    def _json_to_msg(self, json_string):
        """Mainly Generated by ChatGPT"""
        data = json_string['spat']

        # Create a SPAT-Message
        spat_msg = SPAT()

        # time Stamp and Name
        spat_msg.timestamp = data.get('timeStamp', '')
        spat_msg.name = data.get('name', '')

        # Intersections
        for intersection_data in data.get('intersections', []):
            intersection_msg = Intersection()

            # Name and ID
            intersection_msg.name = intersection_data.get('name', '')
            intersection_id = IntersectionID()
            intersection_id.region = intersection_data.get('id', {}).get('region', 0)
            intersection_id.id = intersection_data.get('id', {}).get('id', 0)
            intersection_msg.id = intersection_id

            # optional sections
            intersection_msg.revision = intersection_data.get('revision', 0)
            states = intersection_data.get('status', [])[0]
            for state in states:
                intersection_msg.status.append(int(state))
            intersection_msg.moy = intersection_data.get('moy', 0)
            intersection_msg.timestamp = intersection_data.get('timeStamp', '')

            # enabled Lanes
            intersection_msg.enabled_lanes = intersection_data.get('enabledLanes', [])

            # Compute Signalstates
            for state_data in intersection_data.get('states', []):
                state_msg = SignalState()
                state_msg.movement_name = state_data.get('movementName', '')
                state_msg.signal_group = state_data.get('signalGroup', 0)

                # State Time Speed
                for sts_data in state_data.get('state-time-speed', []):
                    sts_msg = StateTimeSpeed()
                    sts_msg.event_state = sts_data.get('eventState', 0)

                    # Timing
                    timing_data = sts_data.get('timing', {})
                    timing_msg = Timing()
                    timing_msg.start_time = timing_data.get('startTime', 0)
                    timing_msg.min_end_time = timing_data.get('minEndTime', 0)
                    timing_msg.max_end_time = timing_data.get('maxEndTime', 0)
                    timing_msg.likely_time = timing_data.get('likelyTime', 0)
                    timing_msg.confidence = timing_data.get('confidence', 0)
                    timing_msg.next_time = timing_data.get('nextTime', 0)
                    sts_msg.timing = timing_msg

                    # Velocity Data
                    for speed_data in sts_data.get('speeds', []):
                        speed_msg = Speed()
                        speed_msg.type = speed_data.get('type', 0)
                        speed_msg.speed = speed_data.get('speed', 0)
                        speed_msg.confidence = speed_data.get('confidence', 0)
                        speed_msg.distance = speed_data.get('distance', 0)
                        speed_msg.classification = speed_data.get('classification', 0)
                        sts_msg.speeds.append(speed_msg)

                    # regional extensions, if available
                    for regional_data in sts_data.get('regional', []):
                        regional_msg = Regional()
                        regional_msg.region_id = regional_data.get('regionId', 0)
                        regional_msg.reg_ext_value = regional_data.get('regExtValue', '')
                        sts_msg.regional.append(regional_msg)

                    state_msg.state_time_speed.append(sts_msg)

                # maneuver assist
                for maneuver_data in state_data.get('maneuverAssistList', []):
                    maneuver_msg = ManeuverAssist()
                    maneuver_msg.connection_id = maneuver_data.get('connectionID', 0)
                    maneuver_msg.queue_length = maneuver_data.get('queueLength', 0)
                    maneuver_msg.available_storage_length = maneuver_data.get('availableStorageLength', 0)
                    maneuver_msg.wait_on_stop = maneuver_data.get('waitOnStop', False)
                    maneuver_msg.ped_bicycle_detect = maneuver_data.get('pedBicycleDetect', False)
                    state_msg.maneuver_assist_list.append(maneuver_msg)

                intersection_msg.states.append(state_msg)

            # regional Extensions for Intersection
            for regional_data in intersection_data.get('regional', []):
                regional_msg = Regional()
                regional_msg.region_id = regional_data.get('regionId', 0)
                regional_msg.reg_ext_value = regional_data.get('regExtValue', '')
                intersection_msg.regional.append(regional_msg)

            spat_msg.intersections.append(intersection_msg)

        # Regional Extensions for SPAT
        for regional_data in data.get('regional', []):
            regional_msg = Regional()
            regional_msg.region_id = regional_data.get('regionId', 0)
            regional_msg.reg_ext_value = regional_data.get('regExtValue', '')
            spat_msg.regional.append(regional_msg)

        return spat_msg
    
    def send(self, data):
        # Convert the JSON Data to msg
        msg = self._json_to_msg(data)
        # Publish the message
        self.Publisher.publish(msg)
        # Log
        self.get_logger().info("Published Spatem")