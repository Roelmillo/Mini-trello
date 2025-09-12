from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure

app = FastAPI()

# Servir carpeta estática
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


# ------------------------------
# COMPONENTES
# ------------------------------

# Tarjeta de tablero
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


# Lista de tableros
@component
def BoardList(on_select_board):
    boards = [
        {"title": "Proyecto 1", "color": "#3498db"},
        {"title": "Proyecto 2", "color": "#2ecc71"},
        {"title": "Proyecto 3", "color": "#e67e22"},
    ]

    return html.div(
        {"class": "board-list"},
        [BoardCard(b["title"], b["color"], on_select_board) for b in boards],
        html.button({"class": "add-board"}, "+ Crear nuevo tablero"),
    )


# Tarjeta de tarea
@component
def TaskCard(task_name: str):
    return html.div({"class": "task"}, task_name)


# Columna de Kanban
@component
def Column(name: str, tasks: list[str]):
    return html.div(
        {"class": "column"},
        html.h3(name),
        [TaskCard(t) for t in tasks],
    )


# Vista de un tablero Kanban
@component
def KanbanBoard(board_name: str, on_back):
    data = {
        "Pendiente": ["Configurar BD", "Definir modelo Usuario"],
        "En progreso": ["Diseñar tablero Kanban"],
        "Completado": ["Conectar ReactPy con backend"],
    }

    return html.div(
        {"class": "kanban"},
        html.button({"class": "back-btn", "onClick": lambda e: on_back()}, "← Volver"),
        html.h2(f"📋 {board_name}"),
        html.div(
            {"class": "board"},
            [Column(name, tasks) for name, tasks in data.items()],
        ),
    )


# ------------------------------
# APP PRINCIPAL
# ------------------------------
@component
def App():
    current_board, set_current_board = use_state(None)

    def handle_select_board(board_name):
        set_current_board(board_name)

    def handle_back():
        set_current_board(None)

    return html.div(
        {},
        html.link({"rel": "stylesheet", "href": "/static/style.css"}),
        html.h1("🚀 Proyecto Oper"),
        (
            BoardList(handle_select_board)
            if current_board is None
            else KanbanBoard(current_board, handle_back)
        ),
    )


configure(app, App)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
