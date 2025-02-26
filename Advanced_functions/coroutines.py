import asyncio

async def async_task():
    print('async task started')
    await asyncio.sleep(2)
    print("async task finished")


async def main():
    task = asyncio.create_task(async_task())
    await task 

asyncio.run(main())

import ayncio 


async def async_task():
    print("task")
    await asyncio.sleep(1)
    print("finish")

async def main():
    task = asyncio.create_task(async_task)
    await task
asyncio.run(main())