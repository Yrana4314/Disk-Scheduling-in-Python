''' FCFS Disk Schedulig algorithm in Python
By Yogesh Rana
CISC3320'''

def fcfs(head, requests):
    # Initialize total head movement to 0
    head_movement = 0
    # Loop through list of requests
    for request in requests:
        # if request (i) is not head
        if request != head:
            # print the movement from head to request line
            print(f"Moving header from {head} to ",end="")
            #if head is greater than request
            if head >= request:
                # calculate the difference
                difference = head - request
                # Add the difference to cumulative head_movement
                head_movement += difference
                # Assign a new head as request
                head = request
            # if head is smaller than request
            if head <= request:
                difference = request - head
                head_movement += difference
                head = request
            print(request)
            print(f" head movement for now: {head_movement}")
    return head_movement

if __name__ == "__main__":
    # Total number of cylinders
    num_disk_cylinders = 5000
    # Get the initial header possition from user GIVEN 65
    head = int(input("Enter initial head position: "))
    # Check if the entered head position is with in range of numbers of cylinders
    while not head in range(num_disk_cylinders+1):
        head = int(input("Please enter head position between 0-4999: "))

    request_sequence = [4078, 153, 2819, 3294, 1433, 211, 1594, 2004, 2335,
    2007, 771, 1043, 3950, 2784, 1881, 2931, 3599, 1245, 4086, 520, 3901,
    2866, 947, 3794, 2353, 3970, 3948, 1815, 4621, 372, 2684, 3088, 827,
    3126, 2083, 584, 4420, 1294, 917, 2881, 3659, 2868, 100, 1581, 4581,
    1664, 1001, 1213, 3439, 4706, 4869]
    #sequence = [82,170,43,140,24,16,190]
    # Call the FCFS function
    fcfc_head_movement = fcfs(head, request_sequence)
    print(f"The total number of head movements is : {fcfc_head_movement}")



