from fastapi import FastAPI
from modelos.cliente import Cliente, Clientecrear

app = FastAPI()

# Lista para guardar clientes
list_clients: list[Cliente] = []


# Ruta principal
@app.get("/")
def home():
    return {"message": "Servidor funcionando correctamente"}


# Obtener todos los clientes
@app.get("/clientes")
def listar_clientes():
    return {"clients": list_clients}


# Crear cliente
@app.post("/clientes", response_model=Cliente)
def create_clients(date_client: Clientecrear):

    # Crear cliente con ID automático
    cliente_val = Cliente(
        id=len(list_clients) + 1,
        name=date_client.name,
        age=date_client.age,
        description=date_client.description
    )

    # Guardar en la lista
    list_clients.append(cliente_val)

    return cliente_val


# Obtener cliente por ID
@app.get("/clientes/{id}")
def get_client(id: int):

    for client_item in list_clients:

        if client_item.id == id:
            return client_item

    return {"message": "client not found"}


# Eliminar cliente
@app.delete("/clientes/{id}", response_model=Cliente)
def delete_client(id: int):

    for client_item in list_clients:

        if client_item.id == id:

            list_clients.remove(client_item)

            return client_item

    return {"message": "client not found"}


# Actualizar cliente
@app.put("/clientes/{id}", response_model=Cliente)
def update_client(id: int, date_client: Clientecrear):

    for client_item in list_clients:

        if client_item.id == id:

            client_item.name = date_client.name
            client_item.age = date_client.age
            client_item.description = date_client.description

            return client_item

    return {"message": "client not found"}