import time

# Set timer length (in seconds)
timer_length = 60 

# Start timer
start_time = time.time()

# Loop until timer runs out
while time.time() - start_time < timer_length:
    remaining_time = timer_length - int(time.time() - start_time)
    print(f"Time remaining: {remaining_time}s", end="\r")

# Timer has finished
print("Time's up!")