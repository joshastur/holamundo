from typing import Optional
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/listar")
def listar():
    f = open("demofile.txt", "r")
    return f.read()

@app.post("/alta/{nombre}/{telefono}")
def dar_alta(nombre: str, telefono: str):
    f = open("demofile.txt", "w")
    # {
    # "nombre": "pepe",
    # "telefono": "5551234"
    # }
    f.write("{\"nombre\":\"" + nombre + "\",\"telefono\":\"" + telefono + "\"}")
    f.close()
    return {"alta":"ok"}

# Borrar fichero contactos

@app.delete("/borrar_fichero")
def borrar():   
    with open("demofile.txt", 'r+') as f:
        f.truncate(0)

# from typing import Optional
# from fastapi import FastAPI
# import json

# app = FastAPI()

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Optional[str] = None):
#     return {"item_id": item_id, "q": q}

# @app.post("/contacto_nuevo/")
# async def create_item(nombre: str,telefono:str):
#     return guarda_datos(nombre=nombre,telefono=telefono)
     

# def guarda_datos(nombre,telefono):
#     f = open('contactos.txt', 'a')
#     with open('contactos.txt', 'a') as f:
#         # Procesamiento del fichero
#         data_set = {"nombre": nombre, "telefono": telefono}
#         json_dump = json.dumps(data_set)
#         f.write(json_dump)

#     f.close()
        
# @app.get("/listar_contactos/")
# def read():
    
#     f = open('contactos.txt', 'r')
#     with open('contactos.txt', 'r') as f:
#         json_object = json. loads(f.read())
        
#     return json_object