import os
from ament_index_python.packages import get_package_share_directory

import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():
    ld = launch.LaunchDescription()

    # config = os.path.join(
    #     get_package_share_directory('pi_control'),
    #     'params.yaml'
    # )

    pi_control_node = launch_ros.actions.Node(
        package='pi_control',
        node_executable='pi_control',
        output='screen',
        node_name='pi_control',
        # respawn=True,
        # respawn_delay=1.0,
        # parameters=[config]
    )

    ld.add_action(pi_control_node)
    return ld