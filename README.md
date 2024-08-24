# Project_G7
Aplicación del robot ABB IRB 1200 5kg 0.9m en el almacenamiento de componentes químicos antes de su uso en el proceso de producción.

Para ejecutar el avance:
1. cd ~/catkin_ws
2. catkin_make
3. source devel/setup.bash

### PARA EL GAZEBO

cd ~/catkin_ws/src/abb_pkgs/abb1200_master/src

roslaunch abb1200_gazebo irb1200_5_90_gazebo.launch

### PARA EL CODIGO DE PYTHON EJECUTAR LAS SIGUIENTES LINEAS

cd ~/catkin_ws/src/abb_pkgs/abb1200_master/src

rosrun abb1200_master jtc_node.py 1.0 -0.5 0.5 1.0 -1.0 0.5

rosrun abb1200_master jtc_node.py 0.02 0.60 -0.5 0 1.5 0

rosrun abb1200_master jtc_node.py 0.02 0.65 -0.5 0 1.5 0

rostopic pub /gripper/gripper_cmd/goal [Tab][Tab] #gripper agarra con position 0.2

rosrun abb1200_master jtc_node.py 0.02 0.50 -0.5 0 1.5 0

rosrun abb1200_master jtc_node.py 0.02 0.1 0.3 0 0 0

rosrun abb1200_master jtc_node.py 2.4 0.1 0.3 0 0 0

rosrun abb1200_master jtc_node.py 2.6 0.4 0.3 0 -0.8 0

rosrun abb1200_master jtc_node.py 2.8 0.4 0.4 0 -0.8 0

rostopic pub /gripper/gripper_cmd/goal [Tab][Tab] #gripper agarra con position 0.0

rosrun abb1200_master jtc_node.py 2.8 0.3 0.4 0 -0.8 0

rosrun abb1200_master jtc_node.py 0 0.3 0.4 0 -0.8 0

rosrun abb1200_master jtc_node.py 0.02 0.60 -0.5 0 1.5 0
