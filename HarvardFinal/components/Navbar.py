import reflex as rx
from .Button import Button


class NavbarState(rx.State):
    is_mobile_menu_open: bool = False
    
    def toggle_mobile_menu(self):
        self.is_mobile_menu_open = not self.is_mobile_menu_open
    
    def close_mobile_menu(self):
        self.is_mobile_menu_open = False


def MobileMenuButton() -> rx.Component:
    return rx.button(
        rx.cond(
            NavbarState.is_mobile_menu_open,
            rx.icon("x", size=24, color="black"),
            rx.icon("menu", size=24, color="black")
        ),
        on_click=NavbarState.toggle_mobile_menu,
        class_name="sm:hidden bg-purple-400 border-2 border-black p-4 py-6 hover:bg-purple-500 transition-colors shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transform hover:-translate-y-1"
    )


def MobileMenu() -> rx.Component:
    return rx.cond(
        NavbarState.is_mobile_menu_open,
        rx.box(
            rx.box(
                Button(
                    text="New Task",
                    icon="plus",
                    color="blue",
                    size="mobile", 
                    full_width=True,
                    on_click=NavbarState.close_mobile_menu
                ),
                Button(
                    text="New Note",
                    icon="book_open",
                    color="green",
                    size="mobile", 
                    full_width=True,  
                    on_click=NavbarState.close_mobile_menu
                ),
                class_name="max-w-7xl mx-auto px-4 py-6"
            ),
            class_name="sm:hidden bg-white border-b-4 border-black shadow-[0px_8px_0px_0px_rgba(0,0,0,1)]"
        )
    )



def Navbar() -> rx.Component:
    return rx.box(
        rx.box(
            # Logo section
            rx.box(
                rx.box(
                    rx.icon("square_check", size=32, color="black"),
                    class_name="bg-red-400 border-4 border-black p-2 sm:p-3 transform -rotate-3 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]"
                ),
                rx.box(
                    rx.heading(
                        "Harvard TODO & Notes",
                        class_name="text-black text-xl sm:text-2xl font-black tracking-tight"
                    ),
                    rx.text(
                        "Simple & Productive",
                        class_name="text-black text-xs sm:text-sm font-bold text-gray-600"
                    ),
                    class_name="text-center sm:text-left"
                ),
                class_name="flex items-center space-x-3"
            ),
            
            # Desktop Navigation buttons (hidden on mobile)
            rx.box(
                Button(
                    text="New Task",
                    icon="plus",
                    color="blue",
                    mobile_text="Task"
                ),
                Button(
                    text="New Note", 
                    icon="book_open",
                    color="green",
                    mobile_text="Note"
                ),
                class_name="hidden sm:flex items-center space-x-2"
            ),
            MobileMenuButton(),
            class_name="flex justify-between items-center max-w-7xl mx-auto px-4 py-4"
        ),
        MobileMenu(),
        class_name="bg-white border-b-4 border-black sticky top-0 z-50 w-full"
    )