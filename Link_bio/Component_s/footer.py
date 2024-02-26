import reflex as rx
import datetime
import Link_bio.constants as const
from Link_bio.estilo.estilo import Size,EmSize
from Link_bio.estilo.color import TextColor
from Link_bio.estilo.color import Color as Color



def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/logo_c.png",
            height=EmSize.VERY_BIG.value,     #alto del logo
            width=EmSize.VERY_BIG.value,      #ancho del logo
            #padding_x=EmSize.SMALL.value,
            alt="logotipo de no se que\"eme\"entre llaves",  #esto es para personas ividentes
            margin_top=EmSize.BIG.value,
        ),
        rx.link(
            rx.box(
                #rx.hstack(
                f"fecha {datetime.date.today()}",
                    rx.text(
                        "trabajo con excelencia   ",
                         as_="span",
                        color=Color.PRIMARY.value
                    ),
                #),
                padding_top=EmSize.DEFAULT.value   
            ),
            href=const.CATALOGO,
            is_external=True,
            font_size=EmSize.MEDIUM.value,
        ),
            rx.text(
                "Innovación en Madera: Inspirando Espacios, Creando Historias para tu hogar.",
                font_size=EmSize.MEDIUM.value,
                margin_top=EmSize.ZERO.value       #quita el espacio entre los textos que los distancia en el eje Y
            ),
       
        align="center",
        margin_bottom=EmSize.BIG.value,
        padding_botttom=EmSize.VERY_BIG.value,
        padding_x=EmSize.BIG.value,
        spacing=Size.ZERO.value,
        color=TextColor.FOOTER.value,
        
    )