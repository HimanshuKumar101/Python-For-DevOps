# set is the collection of the unordered items
# each element in the set must be unique and immutable

collection = { 1,2,3,3,3,4}

print(collection)

# collection = set() empty set

# print(type(collection))


collection.add(5)


collection.remove(3)
print(collection)


collection.update([6,7,8])

print(collection)

set1 = {1,2,3,4,5}
set2 = {2,6,34,62,6,5,3}

print(set1.union(set2))

print(set1.intersection(set2))