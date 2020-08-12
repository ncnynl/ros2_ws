import rclpy
import rclpy.node
from rclpy.exceptions import ParameterNotDeclaredException
from rcl_interfaces.msg import ParameterType
import rcl_interfaces.msg as ParameterMsgs

class MinimalParam(rclpy.node.Node):
    def __init__(self):
        super().__init__('minimal_param_node')
        timer_period = 2 
        self.timer = self.create_timer(timer_period, self.timer_callback)
        my_parameter_descriptor = ParameterMsgs.ParameterDescriptor(
                type=ParameterType.PARAMETER_STRING,description='This parameter is mine!')
        self.declare_parameter("my_parameter", "default value for my_parameter", 
                my_parameter_descriptor)

    def timer_callback(self):
        my_param = self.get_parameter("my_parameter").get_parameter_value().string_value
        self.get_logger().info('Hello %s!' % my_param)
        my_new_param = rclpy.parameter.Parameter(
                "my_parameter",
                rclpy.Parameter.Type.STRING,
                "world"
        )
        all_new_parameters = [my_new_param]
        self.set_parameters(all_new_parameters)


def main():
    rclpy.init()
    node = MinimalParam()
    rclpy.spin(node)

if __name__ == '__main__':
    main()

