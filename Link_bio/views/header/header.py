import reflex as rx
from Link_bio.Component_s.link_icon import link_icon
from Link_bio.Component_s.info_text import info_text
from Link_bio.estilo.estilo import Size, EmSize
from Link_bio.estilo.color import text_color as text_color
from Link_bio.estilo.color import Color as Color
import Link_bio.constants as const
import datetime

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="César Quiña",
                size=Size.BIG.value,
                src="AvatarC.jpeg",
                radius="full",
                color=Color.PRIMARY.value,
                bg=Color.PRIMARY.value,
                padding="2px",
                border="6px",
                border_color=Color.PRIMARY.value
            ),  
            rx.vstack(
                rx.heading(
                    "CREYENTE",
                    size=Size.BIG.value
                ),
                rx.text(
                    "César Quiña",
                    size=Size.MEDIUM.value,
                    margin_top=EmSize.ZERO.value,
                    color=text_color.AZULMARINO.value
            ),
            rx.hstack(
                link_icon(
                    "/icons/instagramAzul.svg",
                    const.INSTAGRAM,
                    "email@email.com"
                ),
                link_icon(
                    "/icons/facebookAzul.svg",
                    const.FACEBOOK,
                    "facebook"
                ),
                link_icon(
                    "/icons/book-azul.svg",
                    const.CATALOGO,
                    "catalogo"
                ),
                link_icon(
                    "/icons/whatsappAzul.svg",
                    const.WHATSAPP,
                    "whatssap"
                ),
                spacing=Size.BIG.value
            ),
            align_items="start",
        ),
        spacing=Size.BIG.value
    ),
        
    rx.hstack(
        info_text(
            "+4",
            "años de experiencia"
        ),
        rx.spacer(),                                    #crea un espacio ficticio entre texto
        info_text(
            "ateción",
            "al detalle"
        ),
        rx.spacer(), 
        info_text(
            "trabajo",
            "certificado"
        ),
        rx.spacer(),
        width="100%",
        spacing=Size.DEFAULT.value
    ),
        
        
        rx.text(
            f"""
            Bienvenido a nuestro sitio especializado en trabajos en madera y melamina. Desde muebles a medida hasta soluciones de almacenamiento, fusionamos la tradición con la innovación para crear piezas únicas que realzan cualquier espacio. ¡Explore nuestro portafolio y dé vida a sus proyectos con nosotros!""",
            font_size=EmSize.DEFAULT.value,
            color=text_color.BLANCO.value
        ),
        width="100%",
        spacing=Size.DEFAULT.value,                     #espacion entre las 2 secciones
        align_items="start"                         #alinear todo al inicio
        
        
    )