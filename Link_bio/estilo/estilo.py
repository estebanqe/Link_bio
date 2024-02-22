import reflex as rx
from enum import Enum
from.color import Color as Color
from.color import text_color as text_color
from.fonts import Font,FontWeight

#Constants
MAX_WIGTH ="700px"

#Sizes
STYLESHEETS =[
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
    
]


class EmSize(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"


class Size(Enum):
    ZERO = "0"
    UNO="0.5"
    SMALL = "1"  # 8px
    DEFAULT = "2"  # 16px/1em
    MEDIUM = "3"  # 32px
    BIG = "8"  # 48px

#Styles


BASE_STYLE= {
    "font_family":Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color":Color.BACKGROUND.value,               #relleno de toda la pagina
    rx.heading: {
        "color":text_color.BLANCO.value,
        "font_family":Font.TITLE.value,
        "font_weight": FontWeight.MEDIUM.value,
    },
    rx.button: {
        "width" : "100%",
        "height" : "100%",
        "padding":EmSize.SMALL.value,
        "border_radius": EmSize.DEFAULT.value,
        "color":text_color.BLANCO.value,                #color de letra de los botones
        "background_color":Color.CONTENT.value,           #color del relleno de los botones
        "white_space":"normal",                     #cuando se haga pequeño este en 2 lineas
        "text_align":"start",
        "_hover":{                                   #hover es cuando se ilumina cunado lo señalamos con el mouse
            "background_color":Color.SECONDARY.value
        }
    },
    rx.link :{
        "text_decoration":"none",
        "_hover":{}
    }
}

navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size=EmSize.LARGE.value
)

title_style = dict(
    width="100%",                                #que ocupe el 100 porciento de los pixeles en donde se encuentre
    size=Size.DEFAULT.value,
    padding_top=EmSize.LARGE.value               #  el espacio encima del segmento
)

button_title_style = dict(
    font_family=Font.TITLE.value,
    font_weight= FontWeight.MEDIUM.value,
    font_size=EmSize.DEFAULT.value,
    color=text_color.colorletraboton.value
)

button_body_style = dict(
    font_size=EmSize.MEDIUM.value,
    font_weight= FontWeight.LIGHT.value,
    color=text_color.colorletraboton.value
)