def registrar_solicitud():
    codigo = input("Código del estudiante: ")
    nombre = input("Nombre del estudiante: ")
    tipo = input("Tipo de consulta: ")
    descripcion = input("Descripción: ")

    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "descripcion": descripcion
    }

    return solicitud


solicitud = registrar_solicitud()

print("\n--- SOLICITUD REGISTRADA ---")
print("Código:", solicitud["codigo"])
print("Nombre:", solicitud["nombre"])
print("Tipo:", solicitud["tipo"])
print("Descripción:", solicitud["descripcion"])