import reflex as rx
from Link_bio.estilo.estilo import Size, EmSize
from Link_bio.estilo.color import Color as Color
from Link_bio.estilo.color import TextColor 

def info_text(title:str, body:str) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text(
            title,
            as_="span",
            font_weight="bold",
            color=Color.PRIMARY.value
        ),
        f"  {body}",
        font_size=EmSize.MEDIUM.value,
        color=TextColor.BODY.value
        )
    )