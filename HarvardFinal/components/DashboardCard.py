import reflex as rx
from typing import Optional, Callable


def DashboardCard(
    title: str,
    subtitle: str,
    description: str,
    icon: str,
    bg_color: str,
    rotation: str = "rotate-1",
    on_click: Optional[Callable] = None
) -> rx.Component:
    
    card_props = {
        "class_name": f"text-black {bg_color} border-4 border-black p-4 sm:p-6 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] transform {rotation} hover:scale-105 transition-transform cursor-pointer"
    }
    
    if on_click is not None:
        card_props["on_click"] = on_click
    
    return rx.box(
        rx.box(
            rx.box(
                rx.icon(icon, size=32),
                class_name="bg-white border-2 border-black p-2"
            ),
            rx.box(
                rx.text(title, class_name="text-black text-3xl font-black"),
                rx.text(subtitle, class_name="text-black text-sm font-bold text-gray-600"),
                class_name="text-right"
            ),
            class_name="flex items-center justify-between mb-4"
        ),
        rx.heading(description, class_name="text-black text-lg font-bold"),
        **card_props
    )