cmake_minimum_required(VERSION 3.5)
project(robotic_arm_latest)

# Find required packages
find_package(ament_cmake REQUIRED)

# --- Explicitly install URDF files ---
install(
  FILES
    urdf/robotic_arm_latest.urdf
    urdf/robotic_arm_latest.csv
  DESTINATION share/${PROJECT_NAME}/urdf
)

# --- Install other resource directories ---
install(
  DIRECTORY
    meshes
    launch
    config
    textures
  DESTINATION share/${PROJECT_NAME}
)

# Export package
ament_package()

