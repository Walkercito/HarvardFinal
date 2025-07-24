import reflex as rx
from typing import Optional, Callable


def Button(
    text: str,
    icon: str,
    color: str = "blue",
    size: str = "default",
    mobile_text: Optional[str] = None,
    full_width: bool = False,
    on_click: Optional[Callable] = None,
    **kwargs
) -> rx.Component:

    color_classes = {
        "blue": "bg-blue-400 hover:bg-blue-500",
        "green": "bg-green-400 hover:bg-green-500", 
        "red": "bg-red-400 hover:bg-red-500",
        "purple": "bg-purple-400 hover:bg-purple-500"
    }

    size_classes = {
        "sm": "text-xs px-2 py-3",
        "default": "text-sm sm:text-base px-3 sm:px-4 py-6",
        "lg": "text-base px-4 py-6",
        "mobile": "text-lg px-6 py-4" 
    }

    width_class = "w-full" if full_width else ""
    
    layout_class = "flex items-center justify-center" if full_width else ""
    
    base_classes = f"{color_classes.get(color, color_classes['blue'])} text-black border-2 border-black font-bold transition-colors {size_classes.get(size, size_classes['default'])} shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] transform hover:-translate-y-1 {width_class} {layout_class}".strip()

    button_props = {
        "class_name": base_classes,
        **kwargs
    }

    if on_click is not None:
        button_props["on_click"] = on_click
    
    mobile_display_text = mobile_text if mobile_text else (text[:4] if len(text) > 6 else text)
    if full_width:
        return rx.button(
            rx.icon(icon, size=20, class_name="mr-3"),
            text,
            **button_props
        )

    return rx.button(
        rx.icon(icon, size=16, class_name="h-3 w-3 sm:h-4 sm:w-4 mr-1 sm:mr-2"),
        rx.text(mobile_display_text, class_name="sm:hidden"),
        rx.text(text, class_name="hidden sm:inline"),
        **button_props
    )