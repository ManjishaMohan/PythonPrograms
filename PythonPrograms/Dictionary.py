symbol_to_name={
    "H": "hydrogen",
    "He":"helium",
    "Li":"lithium",
     "C": "carbon",
     "O": "oxygen",
    "N": "nitrogen"
}
#operations
print(symbol_to_name.keys())
print(symbol_to_name.values())

symbol_to_name.update({ "P":"phosphorous","S":"sulphur"})
print(symbol_to_name)
print(symbol_to_name.items())

del symbol_to_name["C"]
print(symbol_to_name)
