thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)

print(thislist)  # Output: ['apple', 'banana', 'cherry', 'kiwi', 'orange']

thislist.pop()

thislist.append('mango')

for i in range(3):
    print(thislist[i])

i=0
while i < len(thislist):
    print(thislist[i])
    i += 1

a_list = (x for x in thislist if 'a' in x)

print(list(a_list))  # Output: ['banana', 'mango']