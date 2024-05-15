import time

def print_number_1():
    time.sleep(3) # Take this as an example of a program that takes long to execute.
    print(1)

def print_number_2():
    time.sleep(3)
    print(2)

def print_number_3():
    time.sleep(3)
    print(3)

start_time = time.time() # Get the start time of the program.
print_number_1()
print_number_2()
print_number_3()
end_time = time.time() # Get the end time of the program.
total_time = end_time - start_time
print("Took " + str(total_time) + " seconds to execute.") # Calculate the time taken to execute the program.