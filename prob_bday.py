import numpy as np 
import matplotlib.pyplot as plt 

number_of_people = np.linspace(1, 100, 100) # number of people from 1 to 100
probability = 1 - np.exp(-number_of_people**2 / (2 * 365)) # probability of at least two people sharing a birthday
plt.plot(number_of_people, probability) # plot the probability as a function of the number of people
plt.title('Probability of at least two people sharing a birthday')  
plt.grid(True)
plt.show() 