# You parked your car in a parking lot and want to compute the total cost of the ticket. The billing rules are as follows:

        # - The entrance fee of the car parking lot is 2;
        # - The first full or partial hour costs 3;
        # - Each successive full or partial hour (after the first) costs 4.
# You entered the car parking lot at time E and left at time L. Time as String "HH:MM". ("HH" between 00-23, "MM" between 00-59)


# Function that, given strings E and L specifying points in time in the format "HH:MM", 
# returns the total cost of the parking bill from your entry at time E to your exit at time L. 
# You can assume that E describes a time before L on the same day.

def solution(E,L):
    h = int(L[0:2]) - int(E[0:2])
    m = int(L[3:5]) - int(E[3:5])

    if m > 0:
        h = h+1

    if h == 0:
        return 2
    elif h == 1:
        return 2+3
    elif h > 1:
        return 2+3+(h-1)*4

E = "10:43" 
L = "15:42" 
solution(E,L)


