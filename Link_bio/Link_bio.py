import reflex as rx
from Link_bio.Component_s.navbar import navbar
from Link_bio.Component_s.footer import footer
from Link_bio.views.header.header import header
from Link_bio.views.links.links import links
from Link_bio.views.Sponsors.sponsors import sponsors
import Link_bio.estilo.estilo as styles
from Link_bio.estilo.estilo import Size,EmSize

#class State(rx.State):
 #   pass


def index() -> rx.Component:
    return rx.box(
        
        #rx.theme_panel(default_open=True),
        navbar(),
            rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=styles.MAX_WIGTH,              # solo usar 600 px en nuestro contenido
                width="100%",                            #que ocupe el 100 porcient del lugar
                margin_y=EmSize.DEFAULT.value,                    #margen en las y
                padding=EmSize.DEFAULT.value
                )
        ), 
        footer()
    )

     

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Creyente | Te enseño los mejores modelos de madera y melamina",
    description="Hola me Llamo creyente y tengo lo mejor de madera y melamina a medida y totalmente personalisado",
    image="AvatarC.jpeg"
)    

