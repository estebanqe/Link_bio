import reflex as rx
from Link_bio.estilo.estilo import Size, EmSize

def link_icon(image: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=image,
            width=EmSize.DEFAULT.value,
            height=EmSize.DEFAULT.value,
            alt=alt     
        ),
        href=url,
        is_external=True
    )