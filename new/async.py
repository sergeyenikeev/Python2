import asyncio

async def world():
    await asyncio.sleep(2)
    print("World")

async def hello():
    await asyncio.sleep(1)
    print("Hello")
    # await world()

async def main():
    # await world()
    await asyncio.gather(world(), hello())
    # await asyncio.gather(world())
    # await asyncio.gather(hello())


if __name__ == "__main__":
    asyncio.run(main())
    # asyncio.run(hello())
    # await asyncio.gather(world(), hello())