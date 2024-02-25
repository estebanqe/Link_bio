import reflex as rx
from Link_bio.estilo.color import Color

class FloatButton(rx.Component):
    library = "antd"
    tag = "FloatButton" 
    icon = rx.image(src="/AvatarC.jpeg")
    href = "https://creyente.vercel.app/"
    target = "_blank"
    badge = {"dot":True,"color":Color.PRIMARY.value}
    
float_button=FloatButton.create