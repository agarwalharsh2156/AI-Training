# synchronousity before asynchronousity

# import time
# # line 8 waits for execution untill line 7 is completely executed.
# # each line is only executed after the line above it is completely executed.
# def printfun():
#     print("HI")
#     print("Hello")
# # Total time taken 2+ secs.
# printfun()


import asyncio
# async def worker(name, n):
#     print(f"{name} started")
#     await asyncio.sleep(n)      # Simulate some work (e.g. network call, I/O)
#     print(f"{name} finished")

# async def main():
#     print("Starting...")
    
#     # Run both workers CONCURRENTLY
#     await asyncio.gather(
#         worker("A", 2),
#         worker("B", 6)
#     )
    
#     print("All done!")

# # Run the program
# asyncio.run(main())


# import asyncio

async def main():
    print("Start")
    
    task1 = asyncio.create_task(asyncio.sleep(5))
    task2 = asyncio.create_task(asyncio.sleep(10))
    
    #only waits for the maximum of all the asyncio.sleep times
    await asyncio.sleep(10)
    await task1
    await task2
    
    print("End")

asyncio.run(main())

    


