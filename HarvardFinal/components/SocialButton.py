import reflex as rx


def SocialButton(icon: str, bg_color: str, href: str = "#") -> rx.Component:
    return rx.link(
        rx.button(
            rx.icon(icon, size=20, color="white"),
            class_name=f"{bg_color} text-white p-3 border-2 border-white hover:opacity-90 transition-colors shadow-[2px_2px_0px_0px_rgba(255,255,255,1)] hover:shadow-[4px_4px_0px_0px_rgba(255,255,255,1)] transform hover:-translate-y-1"
        ),
        href=href,
        target="_blank"
    )