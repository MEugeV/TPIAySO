import os
import redis

# Conexión a Redis
conexion_redis = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True,
)

def agregar_item(usuario: str, coleccion: str, item: str):
    key = f"favoritos:{usuario}:{coleccion}"
    conexion_redis.rpush(key, item)
    print("Ítem agregado")

def listar_items(usuario: str, coleccion: str):
    key = f"favoritos:{usuario}:{coleccion}"
    items = conexion_redis.lrange(key, 0, -1)
    if not items:
        print("Coleccion vacía")
        return
    print(f"{coleccion.title()} de {usuario.title()}:")
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")

def eliminar_item(usuario: str, coleccion: str, item: str):
    key = f"favoritos:{usuario}:{coleccion}"
    item_eliminado = conexion_redis.lrem(key, 0, item)
    if item_eliminado:
        print("Ítem eliminado")
    else:
        print("Ítem no encontrado")

def main():
    print("\n*** Coleccion de Favoritos ***")
    while True:
        accion = input("\n[a] agregar | [c] consultar | [e] eliminar | [s] salir > ").strip().lower()

        if accion not in {"a", "c", "e", "s"}:
            print("Opción no válida")
            continue

        if accion == "s":
            print("Aplicación cerrada")
            break

        usuario = input("Usuario: ").strip().lower()
        coleccion = input("Colección (plural): peliculas, canciones, libros… : ").strip().lower()

        if accion == "a":
            item = input("Ítem a agregar: ").strip()
            agregar_item(usuario, coleccion, item)

        elif accion == "c":
            listar_items(usuario, coleccion)

        elif accion == "e":
            item = input("Ítem a eliminar: ").strip()
            eliminar_item(usuario, coleccion, item)

try:
    main()
except redis.exceptions.ConnectionError:
    print("Error en conexión a redis")