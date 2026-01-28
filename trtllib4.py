# ACTIVITY-1- DATA STRUCTURE-2 IN PY

my_tuple =()

print(my_tuple)

my_tuple =(1,2,3)

print(my_tuple)

my_tuple =(1,2,3, "hi")

print(my_tuple)

my_tuple =(1,2,3, "hi", 4.5)

print(my_tuple)

my_tuple =(1,2,3, "hi")

print(my_tuple)

print(my_tuple[0])

print(my_tuple[1])

print(my_tuple[2])

print(my_tuple[0:3])

# # Activity-2

my_set={1,2,3,3,3,4,4,5,6,7,7,8,9}

print("my_set", my_set)

my_set.add(10)

print("updated my_set", my_set)

set1=my_set

set2={10,1,2,3,14,15}

print("difference : ", set1.difference(set2))

# # activity-3
setun1={"green", "blue"}
setun2={"blue", "yellow"}
print("union", setun1.union(setun2))

# # # Activity-4
setx={"apple", "banana"}
sety={"banana", "orange"}
print("intersection", setx.intersection(sety))


# After Class Projectx
print(" Personal Details Storage Program\n")

# Step 1: Take personal details from the user
first_name = input("Enter your First Name: ")
last_name = input("Enter your Last Name: ")
age = int(input("Enter your Age: "))
height = float(input("Enter your Height (in cm): "))
weight = float(input("Enter your Weight (in kg): "))
fav_subject = input("Enter your Favourite Subject: ")

# Step 2: Store details in a tuple
personal_details = (
    first_name,
    last_name,
    age,
    height,
    weight,
    fav_subject
)

print("\n✅ Data stored successfully in a tuple!")
print("Tuple →", personal_details)

# Step 3: Convert tuple to list
details_list = list(personal_details)

print("\n🔄 Tuple converted into a list!")
print("List →", details_list)

print("\n🎉 Project completed successfully!")
