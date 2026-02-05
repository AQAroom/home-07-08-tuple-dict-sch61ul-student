v1_major = int(input())
v1_minor = int(input())
v1_patch = int(input())
v2_major = int(input())
v2_minor = int(input())
v2_patch = int(input())

version1 = (v1_major, v1_minor, v1_patch)
version2 = (v2_major, v2_minor, v2_patch)

if version1 > version2:
    print(1)
elif version2 > version1:
    print(2)
else:
    print(0)