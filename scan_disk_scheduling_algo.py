''' SCAN Disk Scheduling algorithm in Python
By Yogesh Rana
CISC3320'''
''' In this SCAN disk scheduling algorithm, first of all,
we go to the upper most part of the request list
including 1 less than disk size and go downwards i.e. less than head
'''
def scan(head,requests):
    # total number of cylinders
    num_of_cylinders = 5_000
    # total Head Movement
    head_movements = 0

    # initializing currHeadPos with head
    currHeadPos = head

    # list to store requests > head
    greater_than_head = []
    # greater_than_head goes to rightmost end of the disk i.e, sizeOfDisk - 1
    greater_than_head.append(num_of_cylinders -1)

    # list to store requests < head
    less_han_head = []

    # Divide the list of requests into greater_than_head list and
    # less_han_head list
    for request in requests:
        if request < head:
            less_han_head.append(request)
        else:
            greater_than_head.append(request)


    # Sort both list
    greater_than_head.sort()
    less_han_head.sort()

    # First it will process the requests that are in greater_than_head
    # And then it will process requests in less_han_head list.
    # Loop through greater than head list
    for i in range(len(greater_than_head)):
        # print Serving request message
        print(f"Now Serving request {greater_than_head[i]}")
        head_movements += abs(greater_than_head[i] - currHeadPos)
        print(f"\thead movements for now {head_movements}")
        # Assign new currHeadpos
        currHeadPos = greater_than_head[i]
    # Loop through less_than_head list in REVERSE order
    for i in range(len(less_han_head)-1, -1, -1):
        # print Serving request message
        print(f"Now Serving request {less_han_head[i]}")
        head_movements += abs(less_han_head[i] - currHeadPos)
        print(f"\thead movements for now {head_movements}")
        # Assign new currHeadpos
        currHeadPos = less_han_head[i]
    # return the head_movements
    return head_movements

if __name__ == "__main__":
    # Total number of cylinders
    num_disk_cylinders = 5000
    # Get the initial header possition from user (GIVEN 65)
    head = int(input("Enter initial head position: "))
    # Check if the entered head position is within range of numbers of cylinders
    while not head in range(num_disk_cylinders+1):
        head = int(input("Please enter head position between 0-4999: "))

    request_sequence = [4078, 153, 2819, 3294, 1433, 211, 1594, 2004, 2335,
    2007, 771, 1043, 3950, 2784, 1881, 2931, 3599, 1245, 4086, 520, 3901,
    2866, 947, 3794, 2353, 3970, 3948, 1815, 4621, 372, 2684, 3088, 827,
    3126, 2083, 584, 4420, 1294, 917, 2881, 3659, 2868, 100, 1581, 4581,
    1664, 1001, 1213, 3439, 4706, 4869]
    #sequence = [87,170,43,140,24,16,190]
    # Call the SCAN function
    scan_head_movement = scan(head, request_sequence)
    print(f"The total number of head movements for SCAN is : {scan_head_movement}")

