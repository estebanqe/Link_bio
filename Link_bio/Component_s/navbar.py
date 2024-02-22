import reflex as rx
import Link_bio.estilo.estilo as style
from Link_bio.estilo.estilo import Size,EmSize
from Link_bio.estilo.color import Color as Color


def navbar() -> rx.Component:
    return rx.hstack(            #encabezado
        rx.flex(
            rx.text("Crey",color=Color.PRIMARY.value),
            rx.text("ente",color=Color.SECONDARY.value),
            style=style.navbar_title_style
        ),
        position="sticky",
        bg=Color.CABEZERA.value,
        padding_x=EmSize.BIG.value,
        padding_y=EmSize.DEFAULT.value,
        z_index="999",                                  #para que siempre apareciera arriba
        top="0px"                                         #para que se mantenga la parte superior estatica
        
        )