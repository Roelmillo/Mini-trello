from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from reactpy import component, html, use_state
from reactpy.backend.fastapi import configure

# Importamos componentes
from .components import Login, Signup, BoardList, KanbanBoard, Navbar

# ------------------------------
# CONFIGURACIÓN APP
# ------------------------------
BASE_DIR = Path(__file__).resolve().parent
app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# ------------------------------
# APP PRINCIPAL
# ------------------------------
@component
def App():
    logged_in, set_logged_in = use_state(False)
    show_signup, set_show_signup = use_state(False)
    current_board, set_current_board = use_state(None)
    search_query, set_search_query = use_state("")

    def handle_select_board(board_name):
        set_current_board(board_name)

    def handle_back():
        set_current_board(None)

    return html.div(
        {"class": "app-container"},
        html.meta({"name": "viewport", "content": "width=device-width, initial-scale=1.0"}),
        html.link({"rel": "stylesheet", "href": "/static/style.css"}),

        Navbar(),  # 👈 Nueva barra superior (única)

        (
            Signup(lambda: set_show_signup(False))
            if show_signup
            else (
                Login(lambda: set_logged_in(True), lambda: set_show_signup(True))
                if not logged_in
                else html.div(
                    {},
                    BoardList(handle_select_board, search_query)
                    if current_board is None
                    else KanbanBoard(current_board, handle_back),
                )
            )
        )
    )


configure(app, App)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("frontend.app_front:app", host="0.0.0.0", port=8000, reload=True)
