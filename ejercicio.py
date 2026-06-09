import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

CATEGORIAS = ["Videojuegos", "Libros", "Musica y video", "Herramientas", "Dinero", "Miscelaneo y varios"]
PREFIJOS   = {"Videojuegos": "VJ", "Libros": "LB", "Musica y video": "MV", "Herramientas": "HE", "Dinero": "DI", "Miscelaneo y varios": "MS"}
TIEMPOS_PRESTAMO = [5, 10, 15, 30]
contador_items   = [1]
usuarios     = []
items        = []
prestamos    = []
devoluciones = []
ventas       = []

def menu_principal():
    print("-" * 95)
    print(r' /$$$$$$$                                    /$$                      /$$$$$$   /$$$$$$  ')
    print(r'| $$__  $$                                  | $$                     /$$__  $$ /$$__  $$')
    print(r'| $$   \ $$ /$$$$$$    /$$$$$$    /$$$$$$$ /$$$$$$     /$$$$$$      | $$  \__/| $$  \ $$')
    print(r'| $$$$$$$/ /$$__  $$  /$$__  $$  /$$_____/ |_  $$_/    |____  $$    | $$ /$$$$| $$  | $$')
    print(r'| $$____/ | $$  \__/ | $$$$$$$$ |  $$$$$$   | $$        /$$$$$$$    | $$|_  $$| $$  | $$')
    print(r'| $$      | $$       | $$_____/  \____  $$  | $$ /$$   /$$__  $$    | $$  \ $$| $$  | $$')
    print(r'| $$      | $$       |  $$$$$$$ /$$$$$$$/   |  $$$$/  |  $$$$$$$    |  $$$$$$/|  $$$$$$/')
    print(r'|__/      |__/        \_______/|_______/     \___/    \_______/      \______/  \______/ ')
    print("")
    print("               Bienvenido a Prestago - Sistema de Prestamos".center(95))
    print("-" * 95)
    while True:
        print("\n===== PRESTAGO - MENU PRINCIPAL =====")
        print("  1. Registrar Usuario")
        print("  2. Registrar Item")
        print("  3. Registrar Prestamo")
        print("  4. Registrar Devolucion")
        print("  5. Generar Venta")
        print("  6. Consultar Estado General de Prestamos")
        print("  7. Administrador")
        print("  0. Salir")
        opcion = input("\n  Seleccione una opcion: ").strip()
        if opcion == "1":
            registrar_usuario(usuarios, TIEMPOS_PRESTAMO)
        elif opcion == "2":
            registrar_item(items, CATEGORIAS, PREFIJOS, contador_items)
        elif opcion == "3":
            registrar_prestamo(items, prestamos, usuarios)
        elif opcion == "4":
            registrar_devolucion(items, prestamos, usuarios, devoluciones)
        elif opcion == "5":
            generar_venta_manual(prestamos, usuarios, items, ventas)
        elif opcion == "6":
            consultar_estado_general(prestamos, usuarios)
        elif opcion == "7":
            menu_administrador(usuarios, prestamos, ventas)
        elif opcion == "0":
            print("\n  Hasta luego. Cerrando Prestago...")
            break
        else:
            print("  Opcion no valida. Intente de nuevo.")


def validar_nombre(nombre):
    if len(nombre) < 3:
        print("  Error: El nombre debe tener al menos 3 caracteres.")
        return False
    for caracter in nombre:
        if caracter.isdigit():
            print("  Error: El nombre no puede contener numeros.")
            return False
    return True

def validar_documento(documento):
    if not documento.isdigit():
        print("  Error: El documento solo puede contener numeros.")
        return False
    if len(documento) < 3 or len(documento) > 15:
        print("  Error: El documento debe tener entre 3 y 15 digitos.")
        return False
    return True

def validar_correo(correo):
    if "@" not in correo:
        print("  Error: El correo debe contener '@'.")
        return False
    if not correo.endswith(".com"):
        print("  Error: El correo debe terminar en '.com'.")
        return False
    return True

def validar_nombre_item(nombre):
    letras = 0
    for caracter in nombre:
        if caracter.isalpha():
            letras += 1
    if letras < 3:
        print("  Error: El nombre del item debe tener al menos 3 letras.")
        return False
    return True

def estado_difuso(valor):
    if valor >= 0 and valor <= 2:
        return "Muy malo"
    elif valor > 2 and valor <= 4:
        return "Malo"
    elif valor > 4 and valor <= 6:
        return "Regular"
    elif valor > 6 and valor <= 8:
        return "Bueno"
    elif valor > 8 and valor <= 10:
        return "Excelente"
    else:
        return None

def documento_ya_existe(documento, usuarios):
    for u in usuarios:
        if u["documento"] == documento:
            return True
    return False

def buscar_usuario_por_documento(documento, usuarios):
    for u in usuarios:
        if u["documento"] == documento:
            return u
    return None

def buscar_item_por_id(id_item, items):
    for item in items:
        if item["id"] == id_item:
            return item
    return None

def obtener_prestamos_activos(documento, prestamos):
    lista = []
    for p in prestamos:
        if p["documento_usuario"] == documento and p["activo"] == True:
            lista.append(p)
    return lista

def generar_id_item(categoria, PREFIJOS, contador_items):
    prefijo = PREFIJOS[categoria]
    numero = str(contador_items[0]).zfill(3)
    id_generado = prefijo + numero
    contador_items[0] += 1
    return id_generado

def calcular_dias_prestado(fecha_inicio):
    hoy = datetime.date.today()
    diferencia = hoy - fecha_inicio
    return diferencia.days

def registrar_usuario(usuarios, TIEMPOS_PRESTAMO):
    print("\n========== REGISTRAR USUARIO ==========")
    print("  (Escriba 0 en cualquier momento para volver al menu)")
    while True:
        nombre = input("\n  Ingrese el nombre: ").strip()
        if nombre == "0":
            return
        if validar_nombre(nombre):
            break
    while True:
        apellido = input("  Ingrese el apellido: ").strip()
        if apellido == "0":
            return
        if validar_nombre(apellido):
            break
    while True:
        documento = input("  Ingrese el documento: ").strip()
        if documento == "0":
            return
        if validar_documento(documento):
            if documento_ya_existe(documento, usuarios):
                print("  Error: Este documento ya esta registrado.")
            else:
                break
    while True:
        correo = input("  Ingrese el correo electronico: ").strip()
        if correo == "0":
            return
        if validar_correo(correo):
            break
    print("  Tiempos disponibles: 5, 10, 15, 30 dias")
    while True:
        tiempo = input("  Ingrese el tiempo de prestamo: ").strip()
        if tiempo == "0":
            return
        if tiempo.isdigit() and int(tiempo) in TIEMPOS_PRESTAMO:
            tiempo = int(tiempo)
            break
        else:
            print("  Error: Solo se permite 5, 10, 15 o 30 dias.")
    usuarios.append({"nombre": nombre, "apellido": apellido, "documento": documento, "correo": correo, "tiempo_prestamo": tiempo})
    print(f"\n  Usuario {nombre} {apellido} registrado exitosamente.")

def registrar_item(items, CATEGORIAS, PREFIJOS, contador_items):
    print("\n========== REGISTRAR ITEM ==========")
    print("  (Escriba 0 en cualquier momento para volver al menu)")
    while True:
        nombre = input("\n  Ingrese el nombre del item: ").strip()
        if nombre == "0":
            return
        if validar_nombre_item(nombre):
            break
    print("\n  Categorias disponibles:")
    for i in range(len(CATEGORIAS)):
        print("  " + str(i+1) + ". " + CATEGORIAS[i])
    while True:
        opcion = input("  Seleccione la categoria (numero): ").strip()
        if opcion == "0":
            return
        if opcion.isdigit() and 1 <= int(opcion) <= len(CATEGORIAS):
            categoria = CATEGORIAS[int(opcion) - 1]
            break
        else:
            print("  Error: Seleccione una opcion valida.")
    while True:
        precio = input("  Ingrese el precio de compra: $").strip()
        if precio == "0":
            return
        if precio.isdigit() and int(precio) > 0:
            precio = int(precio)
            break
        else:
            print("  Error: Ingrese un precio valido (numero entero positivo).")
    print("\n  Estado del item (0 = muy malo, 10 = excelente)")
    print("  (Para volver al menu escriba 'menu')")
    while True:
        valor = input("  Ingrese el valor del estado (0-10): ").strip()
        if valor == "menu":
            return
        if valor.isdigit() and 0 <= int(valor) <= 10:
            valor = int(valor)
            estado = estado_difuso(valor)
            break
        else:
            print("  Error: Ingrese un valor entre 0 y 10.")
    id_item = generar_id_item(categoria, PREFIJOS, contador_items)
    items.append({"id": id_item, "nombre": nombre, "categoria": categoria, "precio": precio, "estado_valor": valor, "estado": estado, "disponible": True})
    print(f"\n  Item registrado. ID: {id_item} | Nombre: {nombre} | Estado: {estado}")

def registrar_prestamo(items, prestamos, usuarios):
    print("\n========== REGISTRAR PRESTAMO ==========")
    print("  (Escriba 0 en cualquier momento para volver al menu)")
    if len(items) == 0:
        print("  No hay items registrados.")
        return
    disponibles = []
    for item in items:
        if item["disponible"] == True:
            disponibles.append(item)
    if len(disponibles) == 0:
        print("  No hay items disponibles para prestar.")
        return
    print("\n  " + "ID".ljust(8) + "Nombre".ljust(22) + "Categoria".ljust(22) + "Estado".ljust(12) + "Precio")
    print("  " + "-" * 70)
    for item in disponibles:
        print("  " + item["id"].ljust(8) + item["nombre"].ljust(22) + item["categoria"].ljust(22) + item["estado"].ljust(12) + "$" + str(item["precio"]))
    while True:
        id_item = input("\n  Ingrese el ID del item a prestar: ").strip().upper()
        if id_item == "0":
            return
        item_seleccionado = buscar_item_por_id(id_item, items)
        if item_seleccionado is None:
            print("  Error: ID no encontrado.")
        elif item_seleccionado["disponible"] == False:
            print("  Error: Este item no esta disponible.")
        else:
            break
    while True:
        documento = input("  Ingrese el documento del usuario: ").strip()
        if documento == "0":
            return
        usuario = buscar_usuario_por_documento(documento, usuarios)
        if usuario is None:
            print("  Error: El usuario no esta registrado.")
        else:
            break
    print("\n  Fecha de hoy: " + str(datetime.date.today()))
    print("  Puede ingresar una fecha pasada para simular prestamos vencidos.")
    while True:
        fecha_str = input("  Fecha de inicio (AAAA-MM-DD, Enter para hoy): ").strip()
        if fecha_str == "0":
            return
        if fecha_str == "":
            fecha_inicio = datetime.date.today()
            break
        partes = fecha_str.split("-")
        if len(partes) != 3:
            print("  Error: Use el formato AAAA-MM-DD.")
        elif not partes[0].isnumeric() or not partes[1].isnumeric() or not partes[2].isnumeric():
            print("  Error: La fecha solo puede contener numeros.")
        elif int(partes[1]) < 1 or int(partes[1]) > 12:
            print("  Error: El mes debe estar entre 1 y 12.")
        elif int(partes[2]) < 1 or int(partes[2]) > 31:
            print("  Error: El dia debe estar entre 1 y 31.")
        else:
            fecha_inicio = datetime.date(int(partes[0]), int(partes[1]), int(partes[2]))
            break
    fecha_limite = fecha_inicio + datetime.timedelta(days=usuario["tiempo_prestamo"])
    prestamos.append({
        "id_prestamo": "PR" + str(len(prestamos) + 1).zfill(3),
        "id_item": item_seleccionado["id"],
        "nombre_item": item_seleccionado["nombre"],
        "documento_usuario": usuario["documento"],
        "nombre_usuario": usuario["nombre"] + " " + usuario["apellido"],
        "fecha_inicio": fecha_inicio,
        "fecha_limite": fecha_limite,
        "dias_permitidos": usuario["tiempo_prestamo"],
        "activo": True,
        "vendido": False })
    item_seleccionado["disponible"] = False
    print("\n  Prestamo registrado exitosamente.")
    print(f"  Usuario: {usuario['nombre']} {usuario['apellido']}")
    print(f"  Item: {item_seleccionado['nombre']} (ID: {item_seleccionado['id']})")
    print(f"  Fecha inicio: {fecha_inicio} | Fecha limite: {fecha_limite}")

def registrar_devolucion(items, prestamos, usuarios, devoluciones):
    print("\n========== REGISTRAR DEVOLUCION ==========")
    print("  (Escriba 0 en cualquier momento para volver al menu)")
    while True:
        documento = input("\n  Ingrese el documento del usuario: ").strip()
        if documento == "0":
            return
        usuario = buscar_usuario_por_documento(documento, usuarios)
        if usuario is None:
            print("  Error: El usuario no esta registrado.")
        else:
            break
    prestamos_activos = obtener_prestamos_activos(documento, prestamos)
    if len(prestamos_activos) == 0:
        print(f"  {usuario['nombre']} {usuario['apellido']} no tiene prestamos activos.")
        print("  No se puede registrar la devolucion.")
        return
    prestamos_en_tiempo = []
    for p in prestamos_activos:
        if calcular_dias_prestado(p["fecha_inicio"]) <= 30:
            prestamos_en_tiempo.append(p)
    if len(prestamos_en_tiempo) == 0:
        print("  Todos los prestamos del usuario superan 30 dias.")
        print("  Dirijase a la opcion 5 - Generar Venta para procesarlos.")
        return
    print(f"\n  Prestamos de {usuario['nombre']} {usuario['apellido']}:")
    print("  " + "ID Prestamo".ljust(12) + "ID Item".ljust(10) + "Nombre Item".ljust(22) + "Fecha Inicio".ljust(14) + "Dias")
    print("  " + "-" * 65)
    for p in prestamos_en_tiempo:
        dias = calcular_dias_prestado(p["fecha_inicio"])
        print("  " + p["id_prestamo"].ljust(12) + p["id_item"].ljust(10) + p["nombre_item"].ljust(22) + str(p["fecha_inicio"]).ljust(14) + str(dias))
    while True:
        id_pres = input("\n  Ingrese el ID del prestamo a devolver: ").strip().upper()
        if id_pres == "0":
            return
        prestamo_devolver = None
        for p in prestamos_en_tiempo:
            if p["id_prestamo"] == id_pres:
                prestamo_devolver = p
                break
        if prestamo_devolver is None:
            print("  Error: ID no encontrado.")
        else:
            break
    fecha_devolucion = datetime.date.today()
    dias_prestado = calcular_dias_prestado(prestamo_devolver["fecha_inicio"])
    en_tiempo = fecha_devolucion <= prestamo_devolver["fecha_limite"]
    print(f"\n  Fecha inicio: {prestamo_devolver['fecha_inicio']}")
    print(f"  Fecha devolucion: {fecha_devolucion}")
    print(f"  Dias prestado: {dias_prestado} dias")
    prestamo_devolver["activo"] = False
    for item in items:
        if item["id"] == prestamo_devolver["id_item"]:
            item["disponible"] = True
            break
    devoluciones.append({
        "id_prestamo": prestamo_devolver["id_prestamo"],
        "id_item": prestamo_devolver["id_item"],
        "nombre_item": prestamo_devolver["nombre_item"],
        "documento_usuario": documento,
        "nombre_usuario": usuario["nombre"] + " " + usuario["apellido"],
        "fecha_inicio": prestamo_devolver["fecha_inicio"],
        "fecha_devolucion": fecha_devolucion,
        "dias_prestado": dias_prestado,
        "en_tiempo": en_tiempo })
    if en_tiempo:
        # Generar certificado en TXT
        nombre_txt = f"{usuario['nombre']}_{usuario['apellido']}_{fecha_devolucion}_{prestamo_devolver['id_item']}_certificado.txt"
        contenido_cert  = "=" * 50 + "\n"
        contenido_cert += "     CERTIFICADO DE DEVOLUCION\n"
        contenido_cert += "            PRESTAGO\n"
        contenido_cert += "=" * 50 + "\n\n"
        contenido_cert += f"Usuario: {usuario['nombre']} {usuario['apellido']}\n"
        contenido_cert += f"Documento: {documento}\n"
        contenido_cert += f"Correo: {usuario['correo']}\n\n"
        contenido_cert += f"Item prestado: {prestamo_devolver['nombre_item']}\n"
        contenido_cert += f"ID del item: {prestamo_devolver['id_item']}\n"
        contenido_cert += f"ID del prestamo: {prestamo_devolver['id_prestamo']}\n\n"
        contenido_cert += f"Fecha de prestamo: {prestamo_devolver['fecha_inicio']}\n"
        contenido_cert += f"Fecha limite: {prestamo_devolver['fecha_limite']}\n"
        contenido_cert += f"Fecha de devolucion: {fecha_devolucion}\n"
        contenido_cert += f"Dias prestado: {dias_prestado}\n\n"
        contenido_cert += "Estado: DEVUELTO A TIEMPO - Gracias!\n"
        contenido_cert += "\n" + "=" * 50 + "\n"
        archivo = open(nombre_txt, "w", encoding="utf-8")
        archivo.write(contenido_cert)
        archivo.close()
        print(f"  Certificado TXT generado: {nombre_txt}")

        # Generar certificado en PDF
        nombre_pdf = f"{usuario['nombre']}_{usuario['apellido']}_{fecha_devolucion}_{prestamo_devolver['id_item']}_certificado.pdf"
        pdf = canvas.Canvas(nombre_pdf, pagesize=letter)
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(130, 750, "CERTIFICADO DE DEVOLUCION - PRESTAGO")
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(50, 710, "DATOS DEL USUARIO:")
        pdf.setFont("Helvetica", 11)
        pdf.drawString(50, 693, f"Usuario: {usuario['nombre']} {usuario['apellido']}")
        pdf.drawString(50, 678, f"Documento: {documento}")
        pdf.drawString(50, 663, f"Correo: {usuario['correo']}")
        pdf.line(50, 653, 550, 653)
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(50, 635, "DETALLE DEL PRESTAMO:")
        pdf.setFont("Helvetica", 11)
        pdf.drawString(50, 618, f"Item prestado: {prestamo_devolver['nombre_item']}")
        pdf.drawString(50, 603, f"ID del item: {prestamo_devolver['id_item']}")
        pdf.drawString(50, 588, f"ID del prestamo: {prestamo_devolver['id_prestamo']}")
        pdf.line(50, 578, 550, 578)
        pdf.setFont("Helvetica-Bold", 11)
        pdf.drawString(50, 560, "FECHAS:")
        pdf.setFont("Helvetica", 11)
        pdf.drawString(50, 543, f"Fecha de prestamo: {prestamo_devolver['fecha_inicio']}")
        pdf.drawString(50, 528, f"Fecha limite: {prestamo_devolver['fecha_limite']}")
        pdf.drawString(50, 513, f"Fecha de devolucion: {fecha_devolucion}")
        pdf.drawString(50, 498, f"Dias prestado: {dias_prestado}")
        pdf.line(50, 488, 550, 488)
        pdf.setFont("Helvetica-Bold", 12)
        pdf.setFillColorRGB(0, 0.6, 0)
        pdf.drawString(50, 465, "Estado: DEVUELTO A TIEMPO - Gracias!")
        pdf.save()
        print("\n  Devuelto a tiempo. Gracias!")
        print("  Certificado PDF generado: " + nombre_pdf)
    else:
        print("\n  Devolucion tardia. No se genera certificado.")

def generar_venta(usuario, prestamo, dias_prestado, items, ventas):
    precio_item = 0
    for item in items:
        if item["id"] == prestamo["id_item"]:
            precio_item = item["precio"]
            break
    impuesto = 0.23
    subtotal = precio_item
    valor_impuesto = subtotal * impuesto
    total = subtotal + valor_impuesto
    ventas.append({
        "id_venta": "VT" + str(len(ventas) + 1).zfill(3),
        "id_prestamo": prestamo["id_prestamo"],
        "id_item": prestamo["id_item"],
        "nombre_item": prestamo["nombre_item"],
        "documento_usuario": usuario["documento"],
        "nombre_usuario": usuario["nombre"] + " " + usuario["apellido"],
        "dias_prestado": dias_prestado,
        "subtotal": subtotal,
        "impuesto": valor_impuesto,
        "total": total,
        "fecha_venta": datetime.date.today() })
    # Generar factura en TXT
    nombre_txt_fact = f"{usuario['nombre']}_{usuario['apellido']}_{prestamo['id_item']}_factura.txt"
    contenido_fact  = "=" * 50 + "\n"
    contenido_fact += "         FACTURA DE VENTA\n"
    contenido_fact += "            PRESTAGO\n"
    contenido_fact += "=" * 50 + "\n\n"
    contenido_fact += "MOTIVACION DE LA VENTA:\n"
    contenido_fact += f"El item '{prestamo['nombre_item']}' fue prestado por {dias_prestado} dias,\n"
    contenido_fact += "superando el limite maximo de 30 dias permitidos.\n"
    contenido_fact += "Por esta razon el item debe ser vendido al prestador.\n\n"
    contenido_fact += "-" * 50 + "\n"
    contenido_fact += "DATOS DEL COMPRADOR:\n"
    contenido_fact += f"Nombre: {usuario['nombre']} {usuario['apellido']}\n"
    contenido_fact += f"Documento: {usuario['documento']}\n"
    contenido_fact += f"Correo: {usuario['correo']}\n\n"
    contenido_fact += "-" * 50 + "\n"
    contenido_fact += "DETALLE DEL ITEM:\n"
    contenido_fact += f"Item: {prestamo['nombre_item']}\n"
    contenido_fact += f"ID: {prestamo['id_item']}\n"
    contenido_fact += f"Dias prestado: {dias_prestado}\n\n"
    contenido_fact += "-" * 50 + "\n"
    contenido_fact += "RESUMEN DE COBRO:\n"
    contenido_fact += f"Subtotal:       ${subtotal:.2f}\n"
    contenido_fact += f"Impuesto (23%): ${valor_impuesto:.2f}\n"
    contenido_fact += f"TOTAL A PAGAR:  ${total:.2f}\n"
    contenido_fact += "-" * 50 + "\n"
    contenido_fact += f"Fecha de venta: {datetime.date.today()}\n"
    contenido_fact += "=" * 50 + "\n"
    archivo = open(nombre_txt_fact, "w", encoding="utf-8")
    archivo.write(contenido_fact)
    archivo.close()
    print(f"  Factura TXT generada: {nombre_txt_fact}")

    # Generar factura en PDF
    nombre_pdf = f"{usuario['nombre']}_{usuario['apellido']}_{prestamo['id_item']}_factura.pdf"
    pdf = canvas.Canvas(nombre_pdf, pagesize=letter)
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(180, 750, "FACTURA DE VENTA - PRESTAGO")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(50, 710, "MOTIVACION DE LA VENTA:")
    pdf.drawString(50, 693, f"El item '{prestamo['nombre_item']}' fue prestado por {dias_prestado} dias,")
    pdf.drawString(50, 678, "superando el limite maximo de 30 dias permitidos.")
    pdf.drawString(50, 663, "Por esta razon el item debe ser vendido al prestador.")
    pdf.line(50, 653, 550, 653)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(50, 635, "DATOS DEL COMPRADOR:")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(50, 618, f"Nombre: {usuario['nombre']} {usuario['apellido']}")
    pdf.drawString(50, 603, f"Documento: {usuario['documento']}")
    pdf.drawString(50, 588, f"Correo: {usuario['correo']}")
    pdf.line(50, 578, 550, 578)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(50, 560, "DETALLE DEL ITEM:")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(50, 543, f"Item: {prestamo['nombre_item']}")
    pdf.drawString(50, 528, f"ID: {prestamo['id_item']}")
    pdf.drawString(50, 513, f"Dias prestado: {dias_prestado}")
    pdf.line(50, 503, 550, 503)
    pdf.setFont("Helvetica-Bold", 11)
    pdf.drawString(50, 485, "RESUMEN DE COBRO:")
    pdf.setFont("Helvetica", 11)
    pdf.drawString(50, 468, f"Subtotal:           ${subtotal:.2f}")
    pdf.drawString(50, 453, f"Impuesto (23%):     ${valor_impuesto:.2f}")
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, 435, f"TOTAL A PAGAR:      ${total:.2f}")
    pdf.setFont("Helvetica", 10)
    pdf.drawString(50, 410, f"Fecha de venta: {datetime.date.today()}")
    pdf.save()
    prestamo["activo"]  = False
    prestamo["vendido"] = True
    for item in items:
        if item["id"] == prestamo["id_item"]:
            item["disponible"] = False
            break
    print(f"\n  Factura PDF generada: {nombre_pdf}")
    print(f"  Subtotal:     ${subtotal:.2f}")
    print(f"  Impuesto 23%: ${valor_impuesto:.2f}")
    print(f"  Total:        ${total:.2f}")

def generar_venta_manual(prestamos, usuarios, items, ventas):
    print("\n========== GENERAR VENTA ==========")
    print("  (Escriba 0 para volver al menu)")
    vencidos = []
    for p in prestamos:
        if p["activo"] == True:
            if calcular_dias_prestado(p["fecha_inicio"]) > 30:
                vencidos.append(p)
    if len(vencidos) == 0:
        print("  No hay prestamos activos con mas de 30 dias.")
        return
    print("\n  " + "ID Prestamo".ljust(12) + "Usuario".ljust(25) + "Item".ljust(22) + "Dias")
    print("  " + "-" * 65)
    for p in vencidos:
        dias = calcular_dias_prestado(p["fecha_inicio"])
        print("  " + p["id_prestamo"].ljust(12) + p["nombre_usuario"].ljust(25) + p["nombre_item"].ljust(22) + str(dias))
    while True:
        id_pres = input("\n  Ingrese el ID del prestamo para generar venta: ").strip().upper()
        if id_pres == "0":
            return
        prestamo_seleccionado = None
        for p in vencidos:
            if p["id_prestamo"] == id_pres:
                prestamo_seleccionado = p
                break
        if prestamo_seleccionado is None:
            print("  Error: ID no encontrado.")
        else:
            break
    usuario = buscar_usuario_por_documento(prestamo_seleccionado["documento_usuario"], usuarios)
    dias = calcular_dias_prestado(prestamo_seleccionado["fecha_inicio"])
    generar_venta(usuario, prestamo_seleccionado, dias, items, ventas)

def consultar_estado_general(prestamos, usuarios):
    print("\n========== CONSULTAR ESTADO GENERAL DE PRESTAMOS ==========")
    if len(prestamos) == 0:
        print("  No hay prestamos registrados.")
        return
    activos = []
    devueltos = []
    vendidos = []
    for p in prestamos:
        if p["activo"] == True:
            activos.append(p)
        elif p["vendido"] == True:
            vendidos.append(p)
        else:
            devueltos.append(p)
    encabezado = "  " + "ID".ljust(10) + "Usuario".ljust(25) + "Item".ljust(20) + "Fecha Inicio".ljust(14) + "Dias".ljust(6) + "Estado"
    separador = "  " + "-" * 85
    lista_activos = []
    for p in activos:
        dias = calcular_dias_prestado(p["fecha_inicio"])
        lista_activos.append({"prestamo": p, "dias": dias})
    for i in range(len(lista_activos)):
        for j in range(len(lista_activos) - 1 - i):
            if lista_activos[j]["dias"] > lista_activos[j+1]["dias"]:
                temp = lista_activos[j]
                lista_activos[j]   = lista_activos[j+1]
                lista_activos[j+1] = temp
    print("\n  --- ITEMS ACTUALMENTE PRESTADOS ---")
    if len(lista_activos) == 0:
        print("  No hay items prestados actualmente.")
    else:
        print(encabezado)
        print(separador)
        for entrada in lista_activos:
            p = entrada["prestamo"]
            dias = entrada["dias"]
            if dias > 30:
                estado = "VENTA PENDIENTE"
            elif dias > 20:
                estado = "SOLICITUD ENVIADA"
            elif datetime.date.today() > p["fecha_limite"]:
                estado = "VENCIDO"
            else:
                estado = "En tiempo"
            print("  " + p["id_prestamo"].ljust(10) + p["nombre_usuario"].ljust(25) + p["nombre_item"].ljust(20) + str(p["fecha_inicio"]).ljust(14) + str(dias).ljust(6) + estado)
            if dias > 20 and dias <= 30:
                usuario = buscar_usuario_por_documento(p["documento_usuario"], usuarios)
                nombre_txt = usuario["nombre"] + "_" + usuario["apellido"] + "_" + p["id_item"] + "_solicitud.txt"
                contenido = "=" * 50 + "\n"
                contenido += "   SOLICITUD DE DEVOLUCION - PRESTAGO\n"
                contenido += "=" * 50 + "\n\n"
                contenido += "Estimado/a " + usuario["nombre"] + " " + usuario["apellido"] + ",\n\n"
                contenido += "El item '" + p["nombre_item"] + "' lleva " + str(dias) + " dias prestado.\n"
                contenido += "Le solicitamos gestionar su devolucion antes de los 30 dias.\n\n"
                contenido += "Item: " + p["nombre_item"] + " | ID: " + p["id_item"] + "\n"
                contenido += "Fecha inicio: " + str(p["fecha_inicio"]) + " | Fecha limite: " + str(p["fecha_limite"]) + "\n"
                contenido += "\nAVISO: Pasados 30 dias el item sera vendido a su nombre.\n"
                contenido += "=" * 50 + "\n"
                archivo = open(nombre_txt, "w", encoding="utf-8")
                archivo.write(contenido)
                archivo.close()
                print("  >> Solicitud generada: " + nombre_txt)
    # Ordenar devueltos por dias con burbuja
    lista_devueltos = []
    for p in devueltos:
        dias = calcular_dias_prestado(p["fecha_inicio"])
        lista_devueltos.append({"prestamo": p, "dias": dias})
    for i in range(len(lista_devueltos)):
        for j in range(len(lista_devueltos) - 1 - i):
            if lista_devueltos[j]["dias"] > lista_devueltos[j+1]["dias"]:
                temp = lista_devueltos[j]
                lista_devueltos[j]   = lista_devueltos[j+1]
                lista_devueltos[j+1] = temp

    # Ordenar vendidos por dias con burbuja
    lista_vendidos = []
    for p in vendidos:
        dias = calcular_dias_prestado(p["fecha_inicio"])
        lista_vendidos.append({"prestamo": p, "dias": dias})
    for i in range(len(lista_vendidos)):
        for j in range(len(lista_vendidos) - 1 - i):
            if lista_vendidos[j]["dias"] > lista_vendidos[j+1]["dias"]:
                temp = lista_vendidos[j]
                lista_vendidos[j]  = lista_vendidos[j+1]
                lista_vendidos[j+1]= temp

    print("\n  --- ITEMS DEVUELTOS ---")
    if len(lista_devueltos) == 0:
        print("  No hay items devueltos todavia.")
    else:
        print(encabezado)
        print(separador)
        for entrada in lista_devueltos:
            p = entrada["prestamo"]
            dias = entrada["dias"]
            print("  " + p["id_prestamo"].ljust(10) + p["nombre_usuario"].ljust(25) + p["nombre_item"].ljust(20) + str(p["fecha_inicio"]).ljust(14) + str(dias).ljust(6) + "Devuelto")

    print("\n  --- ITEMS VENDIDOS ---")
    if len(lista_vendidos) == 0:
        print("  No hay items vendidos todavia.")
    else:
        print(encabezado)
        print(separador)
        for entrada in lista_vendidos:
            p = entrada["prestamo"]
            dias = entrada["dias"]
            print("  " + p["id_prestamo"].ljust(10) + p["nombre_usuario"].ljust(25) + p["nombre_item"].ljust(20) + str(p["fecha_inicio"]).ljust(14) + str(dias).ljust(6) + "Vendido")
    print("\n  === ESTADISTICAS GENERALES ===")
    print(f"  Total activos     : {len(activos)}")
    print(f"  Total devueltos   : {len(devueltos)}")
    print(f"  Total vendidos    : {len(vendidos)}")
    print(f"  Total historico   : {len(prestamos)}")
    nombre_archivo = "estado_general_" + str(datetime.date.today()) + ".txt"
    contenido = "ESTADO GENERAL DE PRESTAMOS - PRESTAGO\n"
    contenido     += "Fecha de consulta: " + str(datetime.date.today()) + "\n"
    contenido     += "=" * 60 + "\n\n"
    contenido     += "--- ACTIVOS ---\n"
    for entrada in lista_activos:
        p = entrada["prestamo"]
        dias = entrada["dias"]
        if dias > 30:
            estado_txt = "VENTA PENDIENTE"
        elif dias > 20:
            estado_txt = "SOLICITUD ENVIADA"
        elif datetime.date.today() > p["fecha_limite"]:
            estado_txt = "VENCIDO"
        else:
            estado_txt = "En tiempo"
        contenido += f"ID: {p['id_prestamo']} | Item: {p['nombre_item']} | Usuario: {p['nombre_usuario']} | Dias: {dias} | Estado: {estado_txt}\n"
    contenido += "\n--- DEVUELTOS ---\n"
    for entrada in lista_devueltos:
        p = entrada["prestamo"]
        dias = entrada["dias"]
        contenido += f"ID: {p['id_prestamo']} | Item: {p['nombre_item']} | Usuario: {p['nombre_usuario']} | Dias: {dias}\n"
    contenido += "\n--- VENDIDOS ---\n"
    for entrada in lista_vendidos:
        p = entrada["prestamo"]
        dias = entrada["dias"]
        contenido += f"ID: {p['id_prestamo']} | Item: {p['nombre_item']} | Usuario: {p['nombre_usuario']} | Dias: {dias}\n"
    contenido += "\n=== ESTADISTICAS ===\n"
    contenido += f"Total activos  : {len(activos)}\n"
    contenido += f"Total devueltos: {len(devueltos)}\n"
    contenido += f"Total vendidos : {len(vendidos)}\n"
    contenido += f"Total historico: {len(prestamos)}\n"
    archivo = open(nombre_archivo, "w", encoding="utf-8")
    archivo.write(contenido)
    archivo.close()
    print("\n  Informacion guardada en: " + nombre_archivo)

def menu_administrador(usuarios, prestamos, ventas):
    print("\n========== ACCESO ADMINISTRADOR ==========")
    usuario_admin = input("  Usuario (0 para volver): ").strip()
    if usuario_admin == "0":
        return
    contrasena_admin = input("  Contrasena: ").strip()
    if contrasena_admin == "0":
        return
    ADMINS = {"admin": "1234", "gestor": "abcd"}
    if usuario_admin not in ADMINS or ADMINS[usuario_admin] != contrasena_admin:
        print("  Error: Usuario o contrasena incorrectos.")
        return
    while True:
        print("\n===== PRESTAGO - MENU ADMINISTRADOR =====")
        print("  1. Total de prestamos registrados")
        print("  2. Total de items devueltos")
        print("  3. Total de ventas realizadas")
        print("  4. Total pago realizado")
        print("  5. Lista de usuarios")
        print("  6. Usuario con mayor y menor cantidad de prestamos")
        print("  0. Volver al menu principal")
        opcion = input("\n  Seleccione una opcion: ").strip()
        if opcion == "1":
            print(f"\n  Total de prestamos registrados: {len(prestamos)}")
        elif opcion == "2":
            total = 0
            for p in prestamos:
                if p["activo"] == False and p["vendido"] != True:
                    total += 1
            print(f"\n  Total de items devueltos: {total}")
        elif opcion == "3":
            print(f"\n  Total de ventas realizadas: {len(ventas)}")
        elif opcion == "4":
            total_pagado = 0
            for v in ventas:
                total_pagado += v["total"]
            print(f"\n  Total pago realizado: ${total_pagado:.2f}")
        elif opcion == "5":
            if len(usuarios) == 0:
                print("  No hay usuarios registrados.")
            else:
                print("\n  " + "Nombre".ljust(20) + "Apellido".ljust(20) + "Documento".ljust(16) + "Correo")
                print("  " + "-" * 70)
                for u in usuarios:
                    print("  " + u["nombre"].ljust(20) + u["apellido"].ljust(20) + u["documento"].ljust(16) + u["correo"])
        elif opcion == "6":
            if len(usuarios) == 0:
                print("  No hay usuarios registrados.")
            else:
                conteo = {}
                for u in usuarios:
                    conteo[u["documento"]] = 0
                for p in prestamos:
                    doc = p["documento_usuario"]
                    if doc in conteo:
                        conteo[doc] += 1
                max_p = -1
                min_p = 999999
                doc_max = None
                doc_min = None
                for doc in conteo:
                    if conteo[doc] > max_p:
                        max_p = conteo[doc]
                        doc_max = doc
                    if conteo[doc] < min_p:
                        min_p = conteo[doc]
                        doc_min = doc
                u_max = buscar_usuario_por_documento(doc_max, usuarios)
                u_min = buscar_usuario_por_documento(doc_min, usuarios)
                print(f"\n  Mayor: {u_max['nombre']} {u_max['apellido']} ({max_p} prestamos)")
                print(f"  Menor: {u_min['nombre']} {u_min['apellido']} ({min_p} prestamos)")
        elif opcion == "0":
            break
        else:
            print("  Opcion no valida.")

menu_principal()