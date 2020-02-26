a="geeksforgeeks"
rot=int(input("enter the no. of rotations\n"))
b1=a[rot:]
b2=a[:rot]
c1=a[-(rot):]
c2=a[:-2]
print("left rotation:    "+(b1+b2))
print("right rotation:   "+(c1+c2))
