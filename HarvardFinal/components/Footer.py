import reflex as rx
from datetime import datetime

from ..components.SocialButton import SocialButton
from HarvardFinal.data import (
    GitHub,
    LinkedIn,
    Twitter,
    Email
)


def Footer() -> rx.Component:
    current_year = datetime.now().year
    
    return rx.box(
        rx.box(
            rx.box(
                rx.box(
                    rx.box(
                        rx.box(
                            rx.icon("square_check", size=32, color="black"),
                            class_name="bg-red-400 border-4 border-black p-2 sm:p-3 transform -rotate-3 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]"
                        ),
                        rx.box(
                            rx.heading("Harvard TODO & Notes", class_name="text-lg sm:text-xl font-black"),
                            rx.text("Simple Productivity", class_name="font-bold text-sm sm:text-base"),
                            class_name="ml-3"
                        ),
                        class_name="bg-white text-black border-4 border-white p-3 sm:p-4 inline-flex items-center transform rotate-2 shadow-[4px_4px_0px_0px_rgba(255,255,255,1)] mb-4"
                    ),
                    rx.text(
                        "A productivity app that combines task management and note-taking with a bold, neobrutalist design.",
                        class_name="text-sm font-medium max-w-md text-gray-300"
                    ),
                    class_name="text-center sm:text-left"
                ),
                rx.box(
                    rx.heading("Features", class_name="text-lg font-black mb-4 text-white"),
                    rx.box(
                        rx.text("• Task Management", class_name="text-gray-300 font-medium mb-2"),
                        rx.text("• Note Taking", class_name="text-gray-300 font-medium mb-2"),
                        rx.text("• Priority System", class_name="text-gray-300 font-medium mb-2"),
                        rx.text("• Local Storage", class_name="text-gray-300 font-medium"),
                        class_name="space-y-1"
                    ),
                    class_name="text-center sm:text-left"
                ),
    
                class_name="grid grid-cols-1 sm:grid-cols-2 gap-8 mb-8"
            ),

            rx.box(class_name="border-t-2 border-gray-600 mb-6"),
            rx.box(
                rx.box(
                    rx.text(
                        "Made with ",
                        rx.icon("heart", size=20, color="#ef4444", class_name="inline mx-1"),
                        " by Walkercito",
                        class_name="text-base sm:text-lg font-bold text-white"
                    ),
                    class_name="text-center sm:text-left"
                ),
                
                rx.box(
                    SocialButton("github", "bg-gray-800", GitHub),
                    SocialButton("twitter", "bg-blue-500", Twitter),
                    SocialButton("linkedin", "bg-blue-700", LinkedIn),
                    SocialButton("mail", "bg-red-500", Email),
                    class_name="flex justify-center sm:justify-end space-x-3"
                ),
                class_name="flex flex-col sm:flex-row justify-between items-center gap-4 mb-6"
            ),
        
            rx.text(
                f"© {current_year} Harvard TODO & Notes. Keep it simple, stay productive.",
                class_name="text-xs sm:text-sm font-medium text-center text-gray-400 border-t border-gray-600 pt-4"
            ),
            
            class_name="max-w-7xl mx-auto px-4 py-6 sm:py-8"
        ),
        
        class_name="bg-black text-white border-t-4 border-white w-full mt-8 sm:mt-12"
    )