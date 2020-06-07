from collections import deque
queue = deque([])
#for adding items in queue
queue.append(2)
queue.append(6)
queue.append(4)
queue.append(3)
print(queue)
#for removing items   FIFO
queue.popleft()
print(queue)
#for adding items in first
queue.appendleft(4)
print(queue)

#to check whether the stack is empty or not
if not queue:
    print()

