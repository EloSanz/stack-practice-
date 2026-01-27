from core.http_client import syncClient, client
import time
import asyncio

# Sync comparison
start_sync = time.time()
n = 100
for _ in range(n):
    syncClient.get("https://jsonplaceholder.typicode.com/posts/1")
print(f"Sync execution time: {time.time() - start_sync:.4f}s")

# Async comparison
async def main():
    start_async = time.time()
    tasks = [client.get("https://jsonplaceholder.typicode.com/posts/1") for _ in range(n)]
    await asyncio.gather(*tasks)
    print(f"Async execution time: {time.time() - start_async:.4f}s")

if __name__ == "__main__":
    asyncio.run(main())



    