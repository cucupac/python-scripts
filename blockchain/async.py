import asyncio
from web3 import AsyncWeb3, AsyncHTTPProvider


w3 = AsyncWeb3(AsyncHTTPProvider("https://polygon.llamarpc.com"))


async def fetch_blocks(n):
    for result in asyncio.as_completed([w3.eth.get_block(num) for num in range(n)]):
        b = await result
        print(b.number)


async def fetch_transaction_receipt():
    test_transaction_hash = (
        "0x3d7cc97dc71df2a87fd3e63741328cbec9d6f628371258045e1b5defaf83b754"
    )
    receipt = await w3.eth.wait_for_transaction_receipt(
        transaction_hash=test_transaction_hash, timeout=120, poll_latency=0.1
    )
    print("Retrieved receipt:", receipt)


# asyncio.run(fetch_blocks(50))
asyncio.run(fetch_transaction_receipt())
