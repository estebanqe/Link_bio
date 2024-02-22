import reflex as rx
import Link_bio.estilo.estilo as style
from Link_bio.estilo.estilo import Size,EmSize

def Link_buttton(title: str, body: str, image: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
             rx.hstack(
                  rx.image(
                     src=image,
                     width=EmSize.LARGE.value,                           #ancho del icono
                     height=EmSize.LARGE.value,                      #alto del icono
                     margin=EmSize.MEDIUM.value,                              #margen del icono
                     alt=title,
                     #width="100%"
                ), 
                rx.vstack(
                        rx.text(title,style=style.button_title_style),
                        rx.text(body,style=style.button_body_style),
                        align_items="start",
                        spacing=Size.SMALL.value,                #espacio entre el titulo y descripcion del boton
                        padding_y=EmSize.SMALL.value,
                        padding_right=EmSize.SMALL.value
                ),
                width="100%"
                 
             )         
        ),
        href= url,
        is_external=True,
        width="100%"   
    )
