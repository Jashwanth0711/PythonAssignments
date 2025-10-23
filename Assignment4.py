# why list occupies two blocks of memory but tuple one block in python.
import sys
lst=[1,2,3]
tup=(1,2,3)
print("--Memory Size--")
print(f"List size in bytes:{sys.getsizeof(lst)}")
print(f"Tuple size in bytes:{sys.getsizeof(tup)}")
print("--Memory Address of list and tuple")
print(f"Address of list:{id(lst)}")
print(f"Adress of tuple:{id(tup)}")

#Hashable vs Unhashable
print("--Hashable vs Unhashable--")
print(hash(1))
print(hash("Hello"))
print(hash((1,2)))
print(hash((1,[2,3])))
print(hash([1,2]))