import reflex as rx
from rxconfig import config

from HarvardFinal.components.Navbar import Navbar
from HarvardFinal.components.Dashboard import Dashboard


def index() -> rx.Component:
    return rx.box(
        Navbar(),
        Dashboard(),
        class_name="bg-yellow-50 min-h-screen w-full"
    )

app = rx.App()
app.add_page(
    index,
    route="/",
    title="Harvard TODO & Notes - Dashboard",
    description="A productivity app combining task management and note-taking with neobrutalist design",
)