import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempt", attempts + 1, "wait time", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1



# | Attempt | Printed Output         | Sleep Time | Next wait_time |
# | ------- | ---------------------- | ---------- | -------------- |
# | 1       | Attempt 1 wait time 1  | 1 sec      | 2              |
# | 2       | Attempt 2 wait time 2  | 2 sec      | 4              |
# | 3       | Attempt 3 wait time 4  | 4 sec      | 8              |
# | 4       | Attempt 4 wait time 8  | 8 sec      | 16             |
# | 5       | Attempt 5 wait time 16 | 16 sec     | 32             |
