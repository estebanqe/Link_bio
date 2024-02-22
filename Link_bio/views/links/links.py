import reflex as rx
from Link_bio.Component_s.link_button import Link_buttton
from Link_bio.Component_s.title import title
from Link_bio.estilo.estilo import Size as Size
import Link_bio.constants as const

def links() -> rx.Component:
    return rx.vstack(
        title("Redes Sociales"),
        Link_buttton(
            "Facebook",
            """Madera y Melamina: Donde la Creatividad Encuentra su Hogar.""",
            "icons/facebook.svg",
            const.FACEBOOK
            ),
        
        Link_buttton(
            "Instagram",
            """Diseño en Madera: Crea Tu Espacio Perfecto con Nosotros.""",
            "icons/instagram.svg",
            const.INSTAGRAM
            ),
        Link_buttton(
            "Youtube",
            """Estilo Personalizado, Calidad Artesanal: Nuestro Compromiso.""",
            "icons/youtube.svg",
            const.YOUTUBE
            ),
        Link_buttton(
            "Tik-Tok",
            """Tu Visión, Nuestra Creación: Experiencia en Madera y Melamina.""",
            "icons/linkedin.svg",
            const.LINKEDLINK
            ),
            
            
        title("Cátalogo"),
        Link_buttton(
            "Maderas Personalisadas",
            """Madera: Transformando Ideas en Realidad.""",
            "icons/madera1.svg",
            const.MADERA_PERSONALIZADA
            ),
        Link_buttton(
            "Tablas de Picar",
            """Tablas de Picar: Elegancia y Funcionalidad en Cada Corte.""",
            "icons/madera2.svg",
            const.TABLA_PICAR
            ),
        Link_buttton(
            "Muebles Personalizados",
            """Hecho para Ti: Muebles que Cuentan tu Historia.""",
            "icons/madera3.svg",
            const.MUEBLES_PERSONLAZADOS
            ),
        Link_buttton(
            "Amoblado de Áreas Específicas",
            """Amoblado a tu Medida, Espacios con Propósito.""",
            "icons/madera4.svg",
            const.AMOBLADO_AREA
            ),
        
        title("Contacto"),
        Link_buttton(
            "WhatsApp",
            "respuesta rápida y de preferencia",
            "icons/whatsapp.svg",
            const.WHATSAPP
            ),
        Link_buttton(
            "Email",
            const.EMAIL,
            "icons/email.svg",
            f"mailto:{const.EMAIL}"
            ),
            
            
        width="100%",
        spacing=Size.DEFAULT.value,
    )   