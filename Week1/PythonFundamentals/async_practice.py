import asyncio

async def main(delay):
    print("delay starting")
    await asyncio.sleep(delay)
    print("delay.")


print("Starting async execution")
asyncio.run(main(5))
print("End of async execution.")
