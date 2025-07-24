import reflex as rx
from .DashboardCard import DashboardCard


def Dashboard() -> rx.Component:
    return rx.box(
        rx.box(
            rx.box(
                rx.box(
                    rx.heading("Welcome Back!", class_name="text-xl font-bold"),
                    class_name="text-black inline-block bg-white border-4 border-black px-6 py-3 mb-4 transform rotate-1 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]"
                ),
                rx.heading(
                    "Stay Organized & Productive",
                    class_name="text-black text-3xl sm:text-4xl md:text-5xl font-black tracking-tight mb-2"
                ),
                rx.text(
                    "Manage your tasks and notes in one place",
                    class_name="text-black text-base sm:text-lg font-bold text-gray-600"
                ),
                class_name="text-center mb-8"
            ),
            rx.box(
                DashboardCard(
                    title="Tasks",
                    subtitle="Organize", 
                    description="Manage Tasks",
                    icon="target",
                    bg_color="bg-blue-300",
                    rotation="rotate-2"
                ),
                DashboardCard(
                    title="Notes",
                    subtitle="Capture",
                    description="Take Notes", 
                    icon="book_open",
                    bg_color="bg-pink-300",
                    rotation="-rotate-1"
                ),
                DashboardCard(
                    title="Done",
                    subtitle="Complete",
                    description="Get Things Done",
                    icon="square_check",
                    bg_color="bg-green-300",
                    rotation="rotate-1"
                ),
                DashboardCard(
                    title="Focus",
                    subtitle="Stay on track",
                    description="Stay Focused",
                    icon="clock",
                    bg_color="bg-yellow-300", 
                    rotation="-rotate-2"
                ),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6"
            ),
            class_name="max-w-7xl mx-auto px-4 py-4 sm:py-8"
        ),
        class_name="w-full"
    )