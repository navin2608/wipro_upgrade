details={"name":"navin","city":"karur","college":"sona"}
details1={"name":"sudhakar","city":"karur","college":"sona"}

print(len(details))
#print(cmp(details,details1))
print(str(details))
print(details)
newdict=details.copy()
print("newdict:  ",newdict)
print("dict.items()  ",details.items())
print("dict.keys()   ",details.keys())
details.setdefault("name",10)
print(details)
values=details.values()
print("dict.values  ",values)
for i in values:
    print(i)
