cmake_minimum_required(VERSION 3.0.2)

project(abb_irb1200_description)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs)

catkin_package()

if (CATKIN_ENABLE_TESTING)
  find_package(roslaunch REQUIRED)
endif()

install(DIRECTORY config launch meshes urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
