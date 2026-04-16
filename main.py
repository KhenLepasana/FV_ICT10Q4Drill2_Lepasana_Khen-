from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

def sample_numpy(e):
    document.getElementById('output').innerHTML = " "

    tickets =  np.array(['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
    sold_tickets = np.array([4, 2, 3, 4, 7, 3, 1])
    sample_graph = plt.plot(tickets, sold_tickets)
    plt.show()

    plt.title("Tickets sold")
    plt.xlabel('Days')
    plt.ylabel('Number of Tickets')
    