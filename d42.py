contact={
     "Keerthana":"7795180558",
     "Nameera":"7411935337",
    "Neha":"7411535167",
    "Habiba":"7656321685"
}
contact["Arjun"]="7853124378"
contact["Sam"]="8342567876"
print("Safe Lookup Results:")
print("Sam:",contact.get("Sam","Cantact Not Found"))
print("Raj:",contact.get("Raj","Cantact Not Found"))
print("\nContact List")
for name,phone in contact.items():
  print(f"contact:{name}/phone:{phone}")