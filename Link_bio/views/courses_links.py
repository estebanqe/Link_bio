import reflex as rx
from Link_bio.routes import Route
from Link_bio.Component_s.link_button import Link_buttton
from Link_bio.Component_s.title import title
from Link_bio.estilo.estilo import Size as Size
import Link_bio.constants as const

def courses_links() -> rx.Component:
    return rx.vstack(
        title("Creyente"),
        Link_buttton(
            "pagina Creyente",
            "Nueva descripcion de la pagina Creyente ",
            "/AvatarC.jpeg",
            const.Creyente
        ),
        
        width="100%",
        spacing=Size.DEFAULT.value,
    )   