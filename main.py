import random
from prettytable import PrettyTable

#define the column names of the table in debug mode
outputTable = PrettyTable(['#', 'clock', 'LQ(t)', 'LS(t)',
                           'Future Event List', 'Comment', 'Service Util', 'MQ'])
#defining initial values
FEL = []
arrival_time_list = []
departure_time_list = []
end_time_list = []
number_of_event = 0
idle_time = 0
max_queue_length = 0
clock = 0
lqt = 0
lst = 1
service_non_idle = 0

end_time = int(input("Please enter end time of the simulation: "))
"""
FUNCTION TO GENERATE SERVICE TIME
"""
def generate_service_time():
    service_time = 0
    random_digit_assignment = random.randint(1, 100)

    if (random_digit_assignment) <= 10:
        service_time = 1
    elif (random_digit_assignment) >= 11 and (random_digit_assignment) <= 30:
        service_time = 2
    elif (random_digit_assignment) >= 31 and (random_digit_assignment) <= 60:
        service_time = 3
    elif (random_digit_assignment) >= 61 and (random_digit_assignment) <= 85:
        service_time = 4
    elif (random_digit_assignment) >= 86 and (random_digit_assignment) <= 95:
        service_time = 5
    elif (random_digit_assignment) >= 96 and (random_digit_assignment) <= 100:
        service_time = 6

    return service_time
"""
FUNCTION TO GENERATE ARRIVAL TIME
"""
def generate_arrival_time():
    random_digit_assignment = random.randint(1, 1000)
    if (random_digit_assignment) <= 125:
        arrival_time = 1
    elif (random_digit_assignment) >= 126 and (random_digit_assignment) <= 250:
        arrival_time = 2
    elif (random_digit_assignment) >= 251 and (random_digit_assignment) <= 375:
        arrival_time = 3
    elif (random_digit_assignment) >= 376 and (random_digit_assignment) <= 500:
        arrival_time = 4
    elif (random_digit_assignment) >= 501 and (random_digit_assignment) <= 625:
        arrival_time = 5
    elif (random_digit_assignment) >= 626 and (random_digit_assignment) <= 750:
        arrival_time = 6
    elif (random_digit_assignment) >= 751 and (random_digit_assignment) <= 875:
        arrival_time = 7
    elif (random_digit_assignment) >= 876 and (random_digit_assignment) <= 1000:
        arrival_time = 8

    return arrival_time
"""
The FEL variable has the nested list in the format [['E', 12], ['D', 13], ['A', 14]].
It is created a variable as “l” for using the python length function for a nested list
FEL. The first and second elements of the nested list were then retrieved using two 
for-loop iterators. Bubble sort is implemented.
"""
def sort_FEL(FEL):
    l = len(FEL)
    for i in range(0, l):
        for j in range(0, l - i - 1):
            if (FEL[j][1] > FEL[j + 1][1]):
                temp = FEL[j]
                FEL[j] = FEL[j + 1]
                FEL[j + 1] = temp
    return FEL


for i in range(end_time):
    # creation of initial events and placing on FEL.
    if number_of_event == 0:
        number_of_event += 1 # increment the number off event to print on the debug table

        arrival_time = generate_arrival_time() + clock # generate arrival time for the first event
        departure_time = generate_service_time() + clock # generate departure time for the first event

        departure_time_list = ["D", departure_time] # assign first event's departure time on FEL.
        arrival_time_list = ["A", arrival_time] # assign first event's departure time on FEL.
        end_time_list = ["E", end_time] # assign first event's departure time on FEL.

        FEL.insert(1, departure_time_list) # place first event's departure time on FEL.
        FEL.insert(2, arrival_time_list) # place first event's arrival time on FEL.
        FEL.insert(3, end_time_list) # place first event's end time on FEL.

        sort_FEL(FEL) # sort the future event list

    else:
        # calculate the idle time
        if (lst == 1):
            service_non_idle += FEL[0][1] - clock
        # calculate the max queue length
        if lqt >= max_queue_length:
            max_queue_length = lqt

        clock = FEL[0][1] # take the clock time

        if FEL[0][0] == "A": # IF EVENT IS ARRIVAL EVENT
            FEL.remove(FEL[0]) # remove the handled event from future event list

            if lst == 1: # Is LS(t) = 1?
                lqt += 1 # Increase LQ(t) by 1
                generate_arrival_time() # Generate interarrival time a*
                arrival_time = generate_arrival_time() + clock # schedule next arrival event at tiem t + a*

                arrival_time_list = ["A", arrival_time] # add the arrival time into the arrival time list
                FEL.insert(2, arrival_time_list) # insert arrival time list to 2nd index into FEL

                sort_FEL(FEL) # sort the future event list
            else: # LS(t) != 1
                lst = 1 # set LS(t) to 1
                generate_service_time() # Generate service time s*
                departure_time = generate_service_time() + clock # schedule new departure event at time t + s*

                departure_time_list = ["D", departure_time] # add the departure time into the departure time list
                FEL.insert(1, departure_time_list) # insert departure time list to 1st index into FEL

                generate_arrival_time()  # Generate interarrival time a*
                arrival_time = generate_arrival_time() + clock # schedule next arrival event at time t + a*

                arrival_time_list = ["A", arrival_time] # add the arrival time into the arrival time list
                FEL.insert(2, arrival_time_list) # insert arrival time list to 2nd index into FEL

                sort_FEL(FEL) # sort the future event list
            number_of_event += 1 # increment the number of event to print on the debug table

        elif FEL[0][0] == "D": # IF EVENT IS DEPARTURE EVENT
            FEL.remove(FEL[0]) # remove the handled event from future event list

            if lqt > 0: # Is LQ(t) > 0?
                lqt -= 1 # reduce LQ(t) by 1
                generate_service_time() # Generate service time s*
                departure_time = generate_service_time() + clock # schedule new departure event at time t + s*

                departure_time_list = ["D", departure_time] # add the departure time into the departure time list
                FEL.insert(1, departure_time_list) # insert departure time list to 1st index into FEL

                sort_FEL(FEL)  # sort the future event list
            else:
                lst = 0 # set LS(t) = 0
            number_of_event += 1 # increment the number of event to print on the debug table

        elif FEL[0][0] == "E": # IF EVENT IS END EVENT
            break

    # add the statistics to debug table
    outputTable.add_row([number_of_event, clock, lqt, lst, str(FEL), str(FEL[0]), service_non_idle, max_queue_length])


print("\nIf you want to select the debug mode, please enter 1. When debug mode is selected the simulation produces the system"
      "\nsnapshots for DES and then prints the results. If the debug mode is not selected, simulation only prints the results. "
      "\nIf you want to see only the results of simulation, please enter 2. ")

select_debug_mode = (int(input("Select 1 or 2: \n")))

if select_debug_mode == 1:
    print(outputTable)
    print()
    print("percentage of the time the checkout counter is idle: ",((clock - service_non_idle)/end_time)*100, "%")
    print("maximum queue length at the checkout counter: ", max_queue_length)

elif select_debug_mode == 2:
    print("percentage of the time the checkout counter is idle: ", ((clock - service_non_idle)/end_time)*100, "%")
    print("maximum queue length at the checkout counter: ", max_queue_length)
else:
    print("If you want to see the results, you can only select 1 or 2. Other inputs will not be accepted.")