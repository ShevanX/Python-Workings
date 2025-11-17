
Capitals = {"USA":"DC",
            "India":"New Delhi",
            "Canada":"Toronto",
            "Sri Lanka":"Colombo",
            "France":"Paris",
            "England":"London"}

#print(help(Capitals))

print(Capitals.get("India"))

Capitals.update({"Japan":"Tokyo"})

Capitals.pop("India")

# for i in Capitals.keys():
#     print(i)
#
# for i in Capitals.values():
#     print(i)

for x,y in Capitals.items():
    print(f"{x}:{y}")

