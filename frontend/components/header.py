from reactpy import component, html

@component
def Header(search_query, set_search_query):
    """Header con título y buscador"""
    return html.header(
        {"class": "app-header"},
        html.h1("🚀 Mini-Dino"),
        html.input(
            {
                "type": "text",
                "placeholder": "🔍 Buscar tablero...",
                "value": search_query,
                "onChange": lambda e: set_search_query(e["target"]["value"]),
                "class": "search-input",
            }
        ),
    )
