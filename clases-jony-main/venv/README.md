Cristian Camilo Rojas Vesga ficha #3407184

1. cliente.py - Los modelos
Se usan dos clases con Pydantic. Clientecrear define los datos que el usuario envía (sin id), y Cliente hereda de ella y le agrega el id. Esto es buena práctica porque al crear un cliente el usuario no debe enviar el id, lo genera el sistema solo.
2. main.py - La API
Se importa FastAPI y los dos modelos. Se crea una lista list_clients en memoria que guarda los clientes mientras el servidor está corriendo.
Cada endpoint hace una cosa:

GET /clientes → devuelve toda la lista
POST /clientes → recibe datos, genera el id automático con len(list_clients) + 1 y guarda el cliente
GET /clientes/{id} → recorre la lista buscando el id
DELETE /clientes/{id} → lo encuentra y lo elimina con .remove()
PUT /clientes/{id} → lo encuentra y actualiza sus campos

3. Para correr el servidor
Se usa python -m uvicorn main:app --reload porque uvicorn es el servidor ASGI que corre aplicaciones FastAPI. El --reload hace que se reinicie automáticamente cuando cambias el código.
4. Para probar
Una vez corriendo, entras a http://127.0.0.1:8000/docs y FastAPI genera automáticamente una interfaz visual donde puedes probar todos los endpoints sin necesidad de Postman.