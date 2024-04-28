# PART 1
def part_1():

    # intialise our total value for wrapping paper needed
    total = 0

    # open file with context manager
    with open("input.txt", 'r') as file:
        # read each line of file
        # need to remove new line character
        lines = file.read().split("\n")

        # iterate through file ( after spliting new line character )
        for values in lines:
            # remove the 'x' character
            value = values.split("x")
            # create variable for length, width and height
            # convert string values into integer values for calculation
            l = int(value[0])
            w = int(value[1])
            h = int(value[2])

            # calculate the total surface area
            tsa = (2 * l * w) +  (2 * l * h) + (2 * w * h)

            # calculate the smallest area of the sides
            # area1 = l*w
            # area2 = l*h
            # area3 = w*h

            # if area1 < area2 and area1 < area2:
            #     smallest_area = area1
            # elif area2 < area1 and area2 < area3:
            #     smallest_area = area2
            # elif area3 < area1 and area3 < area2:
            #     smallest_area = area3

            smallest_area = min([l * w, l * h, w* h])

            # increament total each time with the addition
            total += tsa + smallest_area

    # output the total value of wrapping paper needed
    print()
    print(f"Total Amount of Wrapping Paper Need = {total}")
    print()

    # make sure file is closed
    print()
    print(f"Is File 'input.txt' CLosed? {file.closed}")
    print()

# PART 2
def part_2():

    # initalise our total value for ribbon needed
    total = 0

    # open the file with context manager
    with open("test.txt", 'r') as file:

        # read each line of file to remove new line character
        lines = file.read().split("\n")

        # iterate through file
        for values in lines:
            # remove the 'x' character
            value = values.split("x")
            # our variables of type integer for length, width and height
            l = int(value[0])
            w = int(value[1])
            h = int(value[2])

            perim = 2 * min([(l + w), (l + h), (w + h)])
            # calculations
            perimeter1 = (2 * l) + (2 * w)
            perimeter2 = (2 * l) + (2 * h)
            perimeter3 = (2 * w) + (2 * h)

            # find the smallest perimeter
            # CASE perimeter1 smallest
            if perimeter1 < perimeter2 and perimeter1 < perimeter3:
                smallest_perimeter = perimeter1
            # CASE perimeter2 smallest
            elif perimeter2 < perimeter1 and perimeter2 < perimeter3:
                smallest_perimeter = perimeter2
            # CASE perimeter3 smallest
            elif perimeter3 < perimeter1 and perimeter3 < perimeter2:
                smallest_perimeter = perimeter3

            # calculate the volume of present
            volume = l * w * h

            total = perim + volume

    # output the total value of ribbon needed
    print()
    print(f"Total Amount of Ribbon Need = {total}")
    print()

    # make sure file is closed
    print()
    print(f"Is File 'test.txt' CLosed? {file.closed}")
    print()






def day2_2():
    total = 0
    for line in open('test.txt'):
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        ribbon = 2 * min(l+w, w+h, h+l)
        bow = l*w*h
        total += ribbon + bow
    print(total)
    print(bow)

# calling functions
part_1()