import reflex as rx
import Link_bio.constants as const
from Link_bio.Component_s.title import title
from Link_bio.Component_s.link_sponsor import Link_sponsor
from Link_bio.estilo.estilo import Size as Size


def sponsors() -> rx.Component:
    return rx.vstack(
        title("Creyente & Hijos"),
       
          rx.hstack(
               Link_sponsor(
                    "carpinteria.jpg",
                    const.CARPINTERIA, 
                    "simbolo de carpinteria"        
               ),
               Link_sponsor(
                    "logo_c.png",
                    const.CARPINTERIA, 
                    "simbolo de carpinteria"        
               ),
           spacing=Size.BIG.value,
           #columns=[1,2],
          ),
       
        width="100%",
        align_items="start",
        spacing=Size.MEDIUM.value
    )