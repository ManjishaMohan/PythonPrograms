employee={
    "A":"Amit",
    "B":"Babita",
    "C":"Charu",
    "D":"Dinesh",
    "M":"Manji"
}
print(employee.keys())
print(employee.values())
employee.update({"E":"Eram","T":"Tina"})
print(employee)
print(employee.items())
del employee["D"]
print(employee)