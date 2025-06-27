import asyncio

async def gerador():
    for i in range(5):
        await asyncio.sleep(1)
        yield f"Mensagem {i}"

async def main():
    async for msg in gerador():
        print(msg)

asyncio.run(main())