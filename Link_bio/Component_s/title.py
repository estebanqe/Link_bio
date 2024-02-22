import reflex as rx
import Link_bio.estilo.estilo as style
from Link_bio.estilo.estilo import Size

def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        #size=Size.BIG.value,
        style=style.title_style
    )