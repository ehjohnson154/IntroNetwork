import threading
import time


ranges = [
    [10, 20],
    [1, 5],
    [70, 80],
    [27, 92],
    [0, 16]
]

#The actual thread running. Calculates adding up the range.
def runner(id, start, end, result):
    """ Thread running function. """
    print(f"Running: ID {id} | {range(start, end)}")
    total = sum(range(start,end+1))
    result[id] = total

    #return result

# Launch this many threads
THREAD_COUNT = len(ranges)

results = [0] * THREAD_COUNT
# We need to keep track of them so that we can join() them later. We'll
# put all the thread references into this array
threads = [ ]

# Launch all threads!!
for i in range(THREAD_COUNT):
    start = ranges[i][0]
    end = ranges[i][-1]
    # Give them a name
    id = i

    # Set up the thread object.
    t = threading.Thread(target=runner, args=(id, start, end, results))

    # The thread won't start executing until we call `start()`:
    t.start()

    # Keep track of this thread so we can join() it later.
    threads.append(t)

# Join all the threads back up to this, the main thread. The main thread
# will block on the join() call until the thread is complete. If the
# thread is already complete, the join() returns immediately.

for t in threads:
    t.join()

print(results)
print(sum(results))