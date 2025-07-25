import reflex as rx
from rxconfig import config

from HarvardFinal.components.Navbar import Navbar, NavbarState
from HarvardFinal.views.Dashboard import Dashboard
from HarvardFinal.components.TaskSection import TaskSection, TaskState
from HarvardFinal.components.NotesSection import NotesSection, NotesState
from HarvardFinal.components.Footer import Footer

def index() -> rx.Component:
    return rx.box(
        Navbar(),
        rx.box(
            Dashboard(),
            rx.box(
                TaskSection(),
                NotesSection(),
                class_name="grid grid-cols-1 lg:grid-cols-2 gap-6 lg:gap-8 mt-6 sm:mt-8 max-w-7xl mx-auto px-4"
            ),
            class_name="py-4 sm:py-8"
        ),
        
        Footer(),
        class_name="bg-yellow-50 min-h-screen w-full"
    )


app = rx.App()
app.add_page(
    index,
    route="/",
    title="Harvard TODO & Notes - Dashboard",
    description="A productivity app combining task management and note-taking with neobrutalist design",
)