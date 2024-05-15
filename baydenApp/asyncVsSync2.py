import time
import asyncio

async def print_number_1():
    await asyncio.sleep(3) # Take this as an example of a program that takes long to execute.
    print(1)

async def print_number_2():
    await asyncio.sleep(3)
    print(2)

async def print_number_3():
    await asyncio.sleep(3)
    print(3)

async def main():
    await asyncio.gather(print_number_1(), print_number_2(), print_number_3())

start_time = time.time() # Get the start time of the program.
asyncio.run(main()) # Run the program.
end_time = time.time() # Get the end time of the program.
total_time = end_time - start_time
print("Took " + str(total_time) + " seconds to execute.") # Calculate the time taken to execute the program.