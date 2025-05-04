import flet as ft
import pyrebase
import flet
from flet import *
import datetime
import smtplib
from email.mime.text import MIMEText
from functools import partial
from pygments.cmdline import main_inner
from pygments.lexer import default
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



# Instalar firebase pip install pyrebase4
config = {
    "apiKey": "AIzaSyBUipaFuHqb9lewOkHtVBzRIAKZWInFtYY",
    "authDomain": "loginflet-7b2ce.firebaseapp.com",
    "projectId": "loginflet-7b2ce",
    "storageBucket": "loginflet-7b2ce.firebasestorage.app",
    "messagingSenderId": "195689109726",
    "appId": "1:195689109726:web:8ca22ccb29a2ae16d90a4f",
    "measurementId": "G-5XB4L59X9Y",
    "databaseURL": "",
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()


def main(page: ft.Page):
    # Función para un correcto width del container
    if page.width < 500:
        container_width = page.width
    elif 500 <= page.width < 700:
        container_width = page.width * 0.7
    else:
        container_width = page.width * 0.5

    # Función Login
    def login_user(e):
        email = tb1.value
        password = tb2.value
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            page.go("/main")
        except Exception as error:
            t.value = "No se ha podido Loguear correctamente"
        page.update()

    # Función registro
    def register_user(e):
        email = tb1.value
        password = tb2.value
        try:
            user = auth.create_user_with_email_and_password(email, password)
            tb1.value=""
            tb2.value=""
            t.value="Usuario registrado correctamente.Introduzca mail y contraseña."
            page.go("/")
        except Exception as error:
            t.value = "No se ha podido registrar correctamente"
        page.update()

    # Componentes de Login
    tetLogin=ft.Text("Iniciar sesión", size=30,color='Blue')
    buttonRegister = ft.ElevatedButton(text="No estoy registrado", width=page.width * 0.3, color=ft.Colors.BLACK,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),side=ft.BorderSide(color=ft.Colors.BLACK, width=1)),on_click=lambda e: page.go("/register"))
    blogin = ft.ElevatedButton(text="Loguearse", on_click=login_user, width=page.width * 0.3, color=ft.Colors.BLACK,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),side=ft.BorderSide(color=ft.Colors.BLACK, width=1)), )

    # Componentes de Registro
    tet = ft.Text("Regsitrarse", size=30, color='Blue')
    t = ft.Text()
    b = ft.ElevatedButton(text="Registrar", on_click=register_user,width=page.width*0.3,color=ft.Colors.BLACK,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0), side=ft.BorderSide(color=ft.Colors.BLACK, width=1)),)
    buttonLogin = ft.ElevatedButton(text="Ya estoy registrado", width=page.width * 0.3, color=ft.Colors.BLACK,style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=0),side=ft.BorderSide(color=ft.Colors.BLACK, width=1)),on_click=lambda e: page.go("/"))

    ##Componentes comunes Login y registro
    tb1 = ft.TextField(label="Mail", width=page.width * 0.3)
    tb2 = ft.TextField(label="Password ", password=True, can_reveal_password=True, width=page.width * 0.3)
    img = ft.Image(src=f"Bitcoin.png",width=50,height=50,fit=ft.ImageFit.CONTAIN,)

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                "/",
                [
                    ft.Container(
                        height=page.height,
                        width=page.width,
                        margin=ft.margin.only(top=page.height * 0.15),
                        alignment=ft.alignment.center,
                        content=ft.Column(controls=[
                            ft.Container(
                                width=container_width,
                                height=page.height * 0.6,
                                border_radius=60,
                                content=ft.Column(controls=[
                                    ft.Container(
                                        width=None,
                                        height=None,
                                        content=img,
                                        margin=ft.margin.only(top=page.width * 0.02, left=page.height * 0.02)
                                    ),
                                    ft.Container(
                                        content=tetLogin,
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Container(
                                        margin=ft.margin.only(top=page.height * 0.03),
                                        content=ft.Column([tb1, tb2]),
                                        alignment=ft.alignment.center
                                    ),
                                    ft.Container(
                                        margin=ft.margin.only(top=15),
                                        content=ft.Column([blogin]),
                                        alignment=ft.alignment.center
                                    ), 
                                    ft.Container(
                                        margin=ft.margin.only(top=5),
                                        content=ft.Column([buttonRegister, t]),
                                        alignment=ft.alignment.center
                                    ),
                                ],
                                ),
                                bgcolor=ft.Colors.GREY_200,
                                border=ft.border.all(0.5, ft.Colors.BLACK)
                            ),
                        ],
                        ),
                    )
                ],
            )
        )
        page.update()

        if page.route == "/register":
            page.views.append(
                ft.View(
                    "/register",
                    [
                        ft.Container(
                            height=page.height,
                            width=page.width,
                            margin=ft.margin.only(top=page.height * 0.15),
                            alignment=ft.alignment.center,
                            content=ft.Column(controls=[
                                ft.Container(
                                    width=container_width,
                                    height=page.height * 0.6,
                                    border_radius=60,
                                    content=ft.Column(controls=[
                                        ft.Container(
                                            width=None,
                                            height=None,
                                            content=img,
                                            margin=ft.margin.only(top=page.width * 0.02, left=page.height * 0.02)
                                        ),
                                        ft.Container(
                                            content=tet,
                                            alignment=ft.alignment.center
                                        ),
                                        ft.Container(
                                            margin=ft.margin.only(top=page.height * 0.03),
                                            content=ft.Column([tb1, tb2]),
                                             alignment=ft.alignment.center
                                         ),
                                         ft.Container(
                                             margin=ft.margin.only(top=15),
                                             content=ft.Column([b, ]),
                                             alignment=ft.alignment.center
                                         ),
                                         ft.Container(
                                             margin=ft.margin.only(top=5),
                                             content=ft.Column([buttonLogin, t]),
                                             alignment=ft.alignment.center
                                         ),
                                     ],
                                     ),
                                     bgcolor=ft.Colors.GREY_200,
                                     border=ft.border.all(0.5, ft.Colors.BLACK)
                                ),
                            ],
                            ),
                        )
                    ],

                )

            )
            page.update()
        carrito = {}
        if page.route == "/main":
            #Estos serán los productos añadidos
            productos = [
                {"nombre": "raton", "precio": 25, "stock": 255},
                {"nombre": "teclado", "precio": 45, "stock": 259},
                {"nombre": "casco", "precio": 30, "stock": 150},
                {"nombre": "pc", "precio": 550, "stock": 143},
                {"nombre": "mesa", "precio": 80, "stock": 220},
                {"nombre": "silla", "precio": 60, "stock":135},
                {"nombre": "reposapies", "precio": 20, "stock": 63},
                {"nombre": "microfono", "precio": 40, "stock": 139},
                {"nombre": "impresora", "precio": 100, "stock": 145},
                {"nombre": "pack-boligrafo", "precio": 5, "stock": 1110},
                {"nombre": "folios", "precio": 10, "stock": 500},
                {"nombre": "portatil", "precio": 750, "stock": 50}
            ]
            #Donde se mostrará el carrito
            cart_column = ft.Column()
            #Función para mostrar un carrito de la compra
            def mostrar_carro():
                carroCompra = []
                total = 0
                for nombre,datos in carrito.items():
                    #Se multiplica el precio por la cantidad pedida , se suma y nos indica el total.
                    subtotal = datos["precio"] *  datos["cantidad"]
                    total += subtotal
                    carroCompra.append(
                        ft.Row(
                            controls=[
                                ft.Text(f"{datos['nombre'].capitalize()}: {datos['cantidad']} x {datos['precio']}€ = {subtotal}€"),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    icon_color="blue400",
                                    icon_size=20,
                                    on_click=lambda e: quitar_producto(e, nombre),
                                ),
                            ],
                        )
                    )

                if not carroCompra:
                    carroCompra.append(ft.Text("El carro de la compra está vacío."))
                carroCompra.append(ft.Text(f"Total: {total}€", weight="bold"))
                cart_column.controls = carroCompra
                page.update()

            def quitar_producto(e, producto_nombre):
                if producto_nombre in carrito:
                    if carrito[producto_nombre]["cantidad"] > 1:
                        carrito[producto_nombre]["cantidad"] -= 1
                    else:
                        del carrito[producto_nombre]
                mostrar_carro()

            def crear_producto(producto):
                name = producto["nombre"]
                precio = producto["precio"]
                stock = producto["stock"]
                image_path = f"{name}.png"
# Configuración de cantidad con el valor predeterminado de 1.
                cantidad_input = ft.TextField(
                    label="Cantidad",
                    width=100,
                    value="1",
                )

                #En esta función agregamos productos al carrito
                def agregar_producto(e, producto_name=name, producto_precio=precio, producto_stock=stock):
                    cantidad = cantidad_input.value
                    if cantidad.isdigit() and int(cantidad) > 0:
                        cantidad = int(cantidad)
                        if producto_name in carrito:
                            nueva_cantidad = carrito[producto_name]["cantidad"] + cantidad
                            if nueva_cantidad > producto_stock:
                                print("Supera el stock disponible.")
                                return
                            carrito[producto_name]["cantidad"] = nueva_cantidad
                        else:
                            if cantidad > producto_stock:
                                print("No hay suficientes unidades disponibles.")
                                return
                            carrito[producto_name] = {
                                "precio": producto_precio,
                                "cantidad": cantidad,
                                "nombre" : name,
                            }
                        mostrar_carro()
                    else:
                        print("Cantidad inválida")


                return ft.Container(
                    width=420,
                    height=450,
                    bgcolor=ft.Colors.GREY_200,
                    border_radius=10,
                    border=ft.border.all(1, ft.Colors.GREY_600),
                    padding=20,
                    content=ft.Column(
                        controls=[
                            ft.Container(
                                alignment=ft.alignment.center,
                                content=ft.Image(src=image_path, width=230, height=210, fit=ft.ImageFit.COVER)
                            ),
                            ft.Text(name.capitalize(), size=16, weight="bold"),
                            ft.Text(f"Precio: {precio}€"),
                            ft.Text(f"Unidades disponibles: {stock}"),
                            cantidad_input,
                            ft.ElevatedButton("Agregar al carrito", on_click=agregar_producto)
                        ],
                        spacing=10
                    )
                )
            def generar_odt():
                fecha_hora_actual = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
                # Crear el nombre del archivo con la fecha y hora actual
                nombre_archivo = f"Pedido-Oficina-Telde-{fecha_hora_actual}.odt"
                with open(nombre_archivo, "w") as file:
                    file.write("Oficina de Telde: Calle el callejón del castillo \n")
                    file.write("Detalles del Pedido:\n\n")
                    total = 0
                    for nombre, datos in carrito.items():
                        subtotal = datos["precio"] * datos["cantidad"]
                        total += subtotal
                        file.write(
                            f"{datos['nombre'].capitalize()}: {datos['cantidad']} x {datos['precio']}€ = {subtotal}€\n")
                    file.write(f"\nTotal:{total}€")
                return nombre_archivo


            def enviar_pedido():
                archivo = generar_odt()
                enviar_email(
                    destinatario="azael.carballo@gmail.com",
                    asunto="Pedido finalizado - Oficina Telde",
                    cuerpo="Adjunto encontrarás el pedido generado desde la app.",
                    archivo_adjunto=archivo
                )
                carrito.clear()
                mostrar_carro()
                print("Pedido finalizado y enviado")


            def enviar_email(destinatario, asunto, cuerpo, archivo_adjunto):
                msg = MIMEText(cuerpo)
                msg["Subject"] = asunto
                msg["From"] = "djrop.net@gmail.com"
                msg["To"] = destinatario
                mensaje = MIMEMultipart()
                mensaje["From"] = msg["From"]
                mensaje["To"] = msg["To"]
                mensaje["Subject"] = msg["Subject"]
                mensaje.attach(MIMEText(cuerpo, "plain"))

                with open(archivo_adjunto, "rb") as adjunto:
                    parte = MIMEBase("application", "octet-stream")
                    parte.set_payload(adjunto.read())
                    encoders.encode_base64(parte)
                    parte.add_header("Content-Disposition", f"attachment; filename={archivo_adjunto}")
                    mensaje.attach(parte)

                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login("djrop.net@gmail.com", "znea agis zppj qfzj")
                    smtp.send_message(mensaje)


        #Aquí creo la lista de productos
            lista_productos = [crear_producto(p) for p in productos]
            rows = []
            products_per_row = 4
#Tenemos un bucle que va desde 0 hasta el tamaño de la lista de productos de 4 en 4.
            for i in range(0, len(lista_productos), products_per_row):
#Coge un cacho de la lista de productos en este caso cogerá de 4 en 4 como hemos dicho anteriormente.
                row_products = lista_productos[i:i + products_per_row]
                row = ft.Row(
                    controls=row_products,
                    spacing=40
                )
                rows.append(ft.Container(content=row, margin=ft.margin.only(bottom=30)))

            page.views.append(
                ft.View(
                    "/main",
                    controls=[
                        ft.AppBar(title=ft.Text("Almacén"), bgcolor=ft.Colors.BLUE),
                        ft.Container(
                            expand=True,
                            padding=10,
                            content=ft.Column(
                                controls=[
                                    ft.ListView(
                                        controls=rows,
                                        expand=True,
                                        padding=10
                                    ),
                                    ft.Divider(),
                                    ft.Text("Carrito ", size=18, weight="bold"),
                                    cart_column,
                                    ft.ElevatedButton(
                                        "Finalizar pedido",
                                        on_click=lambda e: (
                                            enviar_pedido()
                                        )
                                    )
                                ]
                            )
                        )
                    ]
                )
            )
            page.update()

    ##Configuración del router
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(main, view=ft.AppView.WEB_BROWSER)





