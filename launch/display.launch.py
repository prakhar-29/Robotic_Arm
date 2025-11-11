from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():
    pkg_path = get_package_share_directory('robotic_arm_latest')
    urdf_path = os.path.join(pkg_path, 'urdf', 'robotic_arm_latest.urdf')
    rviz_config_path = os.path.join(pkg_path, 'urdf.rviz')
    print("URDF path:", urdf_path)


    return LaunchDescription([
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            parameters=[{'robot_description': open(urdf_path).read()}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_path],
            output='screen'
        )
    ])

