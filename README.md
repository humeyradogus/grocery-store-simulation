# Simulation of a Grocery Store with Discrete Event Simulation!



A small grocery store has only one checkout counter. Customers arrive at this checkout counter at random from 1 to 8 minutes apart. The service times vary from 1 to 6 minutes. In this program the system is analyzed. The distribution of inter-arrival times and service times are illustrated in the tables Figure 1and Figure 2. To calculate the distribution of time between arrivals and Service Time distribution 2 different function was created. It is assumed that the first customer arrives at the checkout counter at time t=0.!

<img width="161" alt="image" src="https://user-images.githubusercontent.com/75491382/212732627-9222cabb-3240-40b2-babe-5e948d95df52.png">

Figure 1: Distribution of time between arrivals


<img width="150" alt="image" src="https://user-images.githubusercontent.com/75491382/212732874-f424d177-2a5d-4dc9-906e-ae467210b729.png">

Figure 2: Service Time Distribution

After running this program, the user is prompted for the end time of the simulation. After the program receives the end time from the user as an input, the values of the first event are put in the future event list. Future event list added elements are sorted according to clock time. This sorting is done every time an element is added to the list. The sort_FEL() function defined at the top of the program is used to perform the sorting process. The working logic of this function is based on the Bubble Sort Algorithm.
After the first event is completed, two different comparisons are made to understand whether the next events are arrival events or departure events. Elements contained in FEL are kept in the format [['A', 12], ['D', 13], ['E', 18]]. The arrival or departure event of the event in this list is decided by using the lines if FEL[0][0] == "A" or elif FEL[0][0] == "D". If the event is arrival, the algorithm shown in Figure 3 is applied. If Event, Departure, the algorithm shown in Figure 4 is used.

<img width="179" alt="image" src="https://user-images.githubusercontent.com/75491382/212733048-817b6e27-6901-453c-9497-86a80191ecba.png">

Figure 3: Arrival Event

<img width="174" alt="image" src="https://user-images.githubusercontent.com/75491382/212733128-8b2186f9-9dc5-4779-8ade-520c9739d969.png">

Figure 4: Departure Event

*********************************************************************************************************************************

OUTPUT OF THE PROGRAM

