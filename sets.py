set1={"makeup","clothes","work","interest","helping","friends"}
set2={"change","lifestyle","development","self growth","friends"}
print(set1)
print(set2)
print(set1 & set2)
print(set1.union(set2))
set3={"rocks","rocks","rocks"}
print(set3)
list1=["giraffe","camel","lion","lion"]
set4=set(list1)
print(set4)
set4.add("deer")
print(set4)
set4.remove("camel")
print(set4)
print(set1.difference(set2))
print("camel"in set4)
print("lion"in set4)
