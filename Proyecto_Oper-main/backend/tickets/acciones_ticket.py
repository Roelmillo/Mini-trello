from tickets import ticket as t

class Acciones:
    def crear(self, usuario):
        titulo = input("Introduce el título de tu ticket: ")
        descripcion = input("Mete el contenido de tu ticket: ")
        ticket = t.Ticket(usuario[0], titulo, descripcion)
        if ticket.insert_ticket():
            print(f"Ticket guardado: {titulo}")
        else:
            print("No se ha guardado el ticket.")

    def mostrar(self, usuario):
        tickets = t.Ticket.mostrar_tickets()
        for ticket in tickets:
            print(f"Título: {ticket.titulo}, Contenido: {ticket.descripcion}")

    def borrar(self, usuario):
        titulo = input("Introduce el título del ticket a eliminar: ")
        t.Ticket.borrar(titulo)
        print("Ticket eliminado exitosamente.")