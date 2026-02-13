"""the diffrential equation of the pendulum postion is theta'' + (g/l) * sin(theta) = 0 which we get by 
eqauting force of gravity and the force of tension in the string and we put acceleration = theta'' wrt to time 
(tension)mgsin(theta) = m * l * theta''(force of gravity) => theta'' + (g/l) * sin(theta) = 0 
for very small angles we can use the approximation sin(theta) ~ theta and we get the equation of simple harmonic motion
so we got the second order linear homogenous diffrential equation theta'' + (g/l) * theta = 0 {can be solved pluging e^lambda.t}
"""

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_ivp 

time = np.linspace(0, 10, 1000) # time from 0 to 10 seconds with 1000 points 
g = 9.81 # acceleration due to gravity 
l = 1.0 # length of the pendulum 
theta0 = 0.1 # initial angle in radians 
# for small angles we can use the approximation sin(theta) ~ theta
omega = np.sqrt(g/l) # angular frequency 

"""we will use solveivp which uses range kutta technique to solve the diffrential equations but solve_ivp is designed to solve
 equations in the form dy/dt = f(t, y) so we have decompose the second order equation into a system of first order equations """

def pendulum(t, y):
    theta, omega = y 
    dtheta_dt = omega 
    domega_dt = - (g/l) * np.sin(theta) 
    return [dtheta_dt, domega_dt]
"""instead of directly solving the second order equation we have defined a function that returns the derivatives of theta and omega
 with respect to time and we will use this function to solve the system of equations using solve_ivp"""
initial_conditions = [theta0, 0.0] # initial angle and initial angular velocity 

solution = solve_ivp(pendulum, [0, 10], initial_conditions, t_eval=time) # solve the system of equations
theta = solution.y[0] # extract the angle from the solution
plt.plot(time, theta) # plot the angle as a function of time
plt.title('Pendulum Position Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.grid()
plt.show()
