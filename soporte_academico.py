def validar_codigo(codigo):
    return codigo.strip() != "" and len(codigo) >= 6


def validar_tipo(tipo):
    tipos_validos = ["matrícula", "pagos", "constancia", "plataforma", "otro"]
    return tipo.lower() in tipos_validos


def registrar_solicitud():
    codigo = input("Código del estudiante: ")

    while not validar_codigo(codigo):
        print("El código debe tener al menos 6 caracteres y no puede estar vacío.")
        codigo = input("Código del estudiante: ")

    nombre = input("Nombre del estudiante: ")

    tipo = input("Tipo de consulta: ")

    while not validar_tipo(tipo):
        print("Tipo de consulta no válido.")
        print("Opciones: matrícula, pagos, constancia, plataforma, otro")
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