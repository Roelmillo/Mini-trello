from reactpy import component, html

@component
def TaskCard(task_name: str):
    return html.div({"class": "task"}, task_name)

@component
def Column(name: str, tasks: list[str]):
    return html.div(
        {"class": "column"},
        html.h3(name),
        [TaskCard(t) for t in tasks],
    )

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
