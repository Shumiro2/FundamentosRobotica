#!/usr/bin/env python
import rospy
from sensor_msgs.msg import JointState

if __name__ == "__main__":

    rospy.init_node("jointsNode")
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)

    # Nombres de las articulaciones
    jnames = ("head_pan", "right_j0", "right_j1", "right_j2",
              "right_j3", "right_j4", "right_j5", "right_j6")
    # Configuracion articular deseada (en radianes)
    jvalues = [0, 0, -0.78, 0, 1.57, 0, 0.78, 0]
    #          0, 3.2,   0, 0, 1.51, 0, -1.52, -2.92 .
    # Objeto (mensaje) de tipo JointState
    jstate = JointState()
    # Asignar valores al mensaje
    jstate.header.stamp = rospy.Time.now()
    jstate.name = jnames
    jstate.position = jvalues

    # Frecuencia del envio (en Hz)
    rate = rospy.Rate(10)
    x = 0
    y = -0.78
    z = 0
    w = 0
    # Bucle de ejecucion continua
    while not rospy.is_shutdown():

        # Tiempo actual (necesario como indicador para ROS)
        jstate.header.stamp = rospy.Time.now()

        if (x < 3.2):
            x = x+0.032

        elif (y < 0):
            y = y+0.0078

        elif (z > -1.52):
            z = z-0.023

        elif (w > -3):
            w = w-0.0292

        jvalues = [0, x, y, 0, 1.57, 0, z, w]
        jstate.position = jvalues

        # Publicar mensaje
        pub.publish(jstate)
        # Esperar hasta la siguiente iteracion
        rate.sleep()
