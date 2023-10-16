import requests
import time


def send_requests():
    url = "https://www.google.com"
    success_count = 0
    total_requests = 1000

    for _ in range(total_requests):
        response = requests.get(url)
        if response.status_code == 200:
            success_count += 1
        else:
            print(f"Failed request with status: {response.status_code}")

    success_percentage = (success_count / total_requests) * 100
    print(f"Success rate: {success_percentage}%")


if __name__ == "__main__":
    start_time = time.time()
    send_requests()
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time of execution: {total_time} seconds")


########## RESULTS ##########
# Success rate: 100.0%
# Total time of execution: 139.12748408317566 seconds
########## RESULTS ##########
