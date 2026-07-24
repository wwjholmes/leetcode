from collections import deque

queue = deque(['name','age','DOB'])

queue.append("append_from_right") # Append from right
queue.pop() # Pop from right

queue.appendleft("fromLeft") # Append from left
queue.popleft() # Pop from left

element = 'age'
begin_index = 0
end_index = 3
index = 1

print(queue)
print(queue.index(element,begin_index,end_index)) # Returns first index of element b/w the 2 indices.
print(queue.insert(index,element))
print(queue)

print(queue.remove(element)) # removes first occurrance

print(queue.count(element)) # obvious
print(queue.reverse()) # reverses order of queue elements
print(queue)