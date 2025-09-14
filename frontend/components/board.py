from reactpy import component, html

@component
def BoardCard(title: str, color: str, on_click):
    return html.div(
        {
            "class": "board-card",
            "style": {"backgroundColor": color},
            "onClick": lambda event: on_click(title),
        },
        html.h2(title),
    )

@component
def BoardList(on_select_board, search_query: str):
    boards = [
        {"title": "Proyecto 1", "color": "#3498db"},
        {"title": "Proyecto 2", "color": "#2ecc71"},
        {"title": "Proyecto 3", "color": "#e67e22"},
        {"title": "Proyecto 4", "color": "#9b59b6"},
    ]

    filtered_boards = [b for b in boards if search_query.lower() in b["title"].lower()]

    return html.div(
        {"class": "board-list"},
        [BoardCard(b["title"], b["color"], on_select_board) for b in filtered_boards],
        html.button({"class": "add-board"}, "+ Crear nuevo tablero"),
    )
