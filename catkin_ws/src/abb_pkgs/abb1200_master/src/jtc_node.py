#!/usr/bin/env python3

import rospy
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import sys

def perform_trajectory():
    rospy.init_node('abb_trajectory_publisher')  # Inicializar el nodo

    # Cambiar el nombre del topic para que coincida con el remapeo
    controller_name = '/joint_path_command'

    trajectory_publisher = rospy.Publisher(controller_name, JointTrajectory, queue_size=10)  # Definir el publicador

    argv = sys.argv[1:]  # Leer los argumentos de la línea de comandos

    # Verificar que se estén recibiendo 6 valores
    if len(argv) != 6:
        rospy.logerr("Número incorrecto de argumentos. Se requieren 6 valores para las posiciones de las articulaciones.")
        return

    abb_joints = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']  # Nombres de las articulaciones

    # Convertir los argumentos a posiciones en radianes
    goal_positions = [float(arg) for arg in argv]

    rospy.loginfo("Publicando en %s con las posiciones: %s", controller_name, goal_positions)
    rospy.sleep(1)  # Espera para asegurarse de que el nodo esté listo

    # Crear el mensaje de trayectoria
    trajectory_msg = JointTrajectory()
    trajectory_msg.joint_names = abb_joints
    trajectory_msg.points.append(JointTrajectoryPoint())
    trajectory_msg.points[0].positions = goal_positions
    trajectory_msg.points[0].velocities = [0.0 for _ in abb_joints]
    trajectory_msg.points[0].accelerations = [0.0 for _ in abb_joints]
    trajectory_msg.points[0].time_from_start = rospy.Duration(3)  # Tiempo para completar el movimiento

    rospy.sleep(1)  # Otra espera breve para asegurarse de que todo esté listo
    trajectory_publisher.publish(trajectory_msg)  # Publicar la trayectoria

    rospy.loginfo("Mensaje publicado correctamente.")

if __name__ == '__main__':
    perform_trajectory()
