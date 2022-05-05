''' This is SSTF Disk Schedulig algorithm implemented in python
By Yogesh Rana '''

def sstf(head, requests):
    # copy of requests list
    temp_requests = requests
    # Copy of head
    temp_position = head
    # Initialize head movements to 0
    head_movement = 0

    while temp_requests:
        #find the closest request to the current cylinder
        closest = abs(temp_position - temp_requests[0])
        closestIndex = 0
        print(f"Moving Header from {temp_position} to",end=" ")
        for x in range(1, len(temp_requests)):
            if abs(temp_position - temp_requests[x]) < closest:
                closest = abs(temp_position - temp_requests[x])
                closestIndex = x
        head_movement += abs(temp_position - temp_requests[closestIndex])
        # Assign new head i.e. temp_position
        temp_position = temp_requests[closestIndex]
        print(temp_position)
        print(f"\thead movement for now: {head_movement}")
        # Remove that request i.e. head (temp_position) from
        # the copy of the list of request
        temp_requests.remove(temp_position)
    return head_movement

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
    #sequence = [176,79,34,60,92,11,41,114]
    # Call the SSTF function
    sstf_head_movement = sstf(head, request_sequence)
    print(f"The total number of head movements for SSTF is : {sstf_head_movement}")