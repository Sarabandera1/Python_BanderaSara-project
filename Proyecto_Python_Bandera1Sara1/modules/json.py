import json
data = {}
data["usuario"] = []
data["usuario"].append({
    "nombre": "pepito",
    "apellido": "perez"
        
})
data["usuario"].append({
    "nombre": "Daniela",
    "apellido": "Ariza"
        
})
data["usuario"].append({
        "nombre": "pepito",
        "apellido": "perez"
        
})
with open('data,json', 'w') as file: 
    json.dump (data, file, indent=4)