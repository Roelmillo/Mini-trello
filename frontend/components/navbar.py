from reactpy import component, html

@component
def Navbar():
    return html.header(
        {"class": "navbar"},
        # Izquierda: logo + menús
        html.div(
            {"class": "navbar-left"},
            html.span({"class": "logo"}, "🦖 Mini-Dino"),
            html.nav(
                {"class": "nav-links"},
                html.a({"href": "#", "class": "nav-item"}, "Workspaces"),
                html.a({"href": "#", "class": "nav-item"}, "Recientes"),
                html.a({"href": "#", "class": "nav-item"}, "Favoritos"),
            ),
        ),
        # Centro: búsqueda
        html.div(
            {"class": "navbar-center"},
            html.input({
                "type": "text",
                "class": "search-input",
                "placeholder": "Buscar proyectos o tableros..."
            }),
        ),
        # Derecha: acciones + perfil
        html.div(
            {"class": "navbar-right"},
            html.button({"class": "create-btn"}, "Crear"),
            html.span({"class": "icon"}, "🔔"),
            html.div({"class": "avatar"}, "👤"),
        ),
    )
