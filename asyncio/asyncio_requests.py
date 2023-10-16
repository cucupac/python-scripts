import aiohttp
import asyncio
import time


async def send_requests(task_id):
    url = "https://www.google.com"
    success_count = 0
    total_requests = 100

    async with aiohttp.ClientSession() as session:
        for _ in range(total_requests):
            async with session.get(url) as response:
                if response.status == 200:
                    success_count += 1
                else:
                    print(
                        f"Task {task_id} failed request with status: {response.status}"
                    )

    success_percentage = (success_count / total_requests) * 100
    print(f"Task {task_id} Success rate: {success_percentage}%")
    return task_id


async def main():
    tasks = [asyncio.create_task(send_requests(i)) for i in range(10)]
    returned_task_ids = await asyncio.gather(*tasks)
    print("returned_task_ids:", returned_task_ids)


# Python 3.7+
if __name__ == "__main__":
    start_time = time.time()
    asyncio.run(main())
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time of execution: {total_time} seconds")


########## RESULTS ##########
# Task 4 Success rate: 100.0%
# Task 8 Success rate: 100.0%
# Task 9 Success rate: 100.0%
# Task 7 Success rate: 100.0%
# Task 1 Success rate: 100.0%
# Task 0 Success rate: 100.0%
# Task 2 Success rate: 100.0%
# Task 6 Success rate: 100.0%
# Task 5 Success rate: 100.0%
# Task 3 Success rate: 100.0%
# Total time of execution: 13.668063402175903 seconds
########## RESULTS ##########
