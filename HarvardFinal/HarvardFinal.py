import reflex as rx
from rxconfig import config

def index() -> rx.Component:
    return rx.box(
        rx.heading(
            "Welcome to HarvardFinal",
            class_name="text-white font-bold",
        ),
        class_name="bg-stone-900 h-screen w-screen flex items-center justify-center",
    )

app = rx.App()
app.add_page(index)
