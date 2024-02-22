import reflex as rx
from Link_bio.estilo.estilo import Size, EmSize
from Link_bio.estilo.color import Color as Color
from Link_bio.estilo.color import text_color as text_color

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
            title,
            font_weight="bold",
            color=Color.PRIMARY.value
        ),
        f"  {body}",
        font_size=EmSize.MEDIUM.value,
        color=text_color.BLANCO.value
        )
    )