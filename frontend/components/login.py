from reactpy import component, html, use_state

@component
def Login(on_success, on_go_signup):
    username, set_username = use_state("")
    password, set_password = use_state("")
    error, set_error = use_state("")

    def handle_login(event):
        if username == "admin" and password == "1234":  # demo
            set_error("")
            on_success()
        else:
            set_error("❌ Usuario o contraseña incorrectos")

    return html.div(
        {"class": "auth-container"},
        html.h2("🔐 Iniciar sesión"),

        html.input({
            "type": "text",
            "placeholder": "Usuario",
            "value": username,
            "onChange": lambda e: set_username(e["target"]["value"]),
            "class": "auth-input",
        }),
        html.input({
            "type": "password",
            "placeholder": "Contraseña",
            "value": password,
            "onChange": lambda e: set_password(e["target"]["value"]),
            "class": "auth-input",
        }),

        html.button({"class": "auth-btn", "onClick": handle_login}, "Entrar"),

        html.p({"class": "auth-error"}, error) if error else None,

        html.p(
            {},
            "¿No tienes cuenta? ",
            html.a({"href": "#", "onClick": lambda e: on_go_signup()}, "Registrarse")
        ),
    )
