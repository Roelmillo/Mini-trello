from reactpy import component, html, use_state

@component
def Signup(on_go_login):
    username, set_username = use_state("")
    email, set_email = use_state("")
    password, set_password = use_state("")
    confirm, set_confirm = use_state("")
    error, set_error = use_state("")
    success, set_success = use_state("")

    def handle_signup(event):
        if not username or not email or not password or not confirm:
            set_error("⚠️ Todos los campos son obligatorios")
            set_success("")
        elif password != confirm:
            set_error("❌ Las contraseñas no coinciden")
            set_success("")
        else:
            set_error("")
            set_success("✅ Usuario registrado con éxito (simulado)")

    return html.div(
        {"class": "auth-container"},
        html.h2("📝 Registrarse"),

        html.input({
            "type": "text",
            "placeholder": "Usuario",
            "value": username,
            "onChange": lambda e: set_username(e["target"]["value"]),
            "class": "auth-input",
        }),
        html.input({
            "type": "email",
            "placeholder": "Email",
            "value": email,
            "onChange": lambda e: set_email(e["target"]["value"]),
            "class": "auth-input",
        }),
        html.input({
            "type": "password",
            "placeholder": "Contraseña",
            "value": password,
            "onChange": lambda e: set_password(e["target"]["value"]),
            "class": "auth-input",
        }),
        html.input({
            "type": "password",
            "placeholder": "Confirmar contraseña",
            "value": confirm,
            "onChange": lambda e: set_confirm(e["target"]["value"]),
            "class": "auth-input",
        }),

        html.button({"class": "auth-btn", "onClick": handle_signup}, "Crear cuenta"),

        html.p({"class": "auth-error"}, error) if error else None,
        html.p({"class": "auth-success"}, success) if success else None,

        html.p(
            {},
            "¿Ya tienes cuenta? ",
            html.a({"href": "#", "onClick": lambda e: on_go_login()}, "Iniciar sesión")
        ),
    )
