import reflex as rx
from typing import List, Dict, Any
from datetime import datetime
from .Button import Button
import random

class NotesState(rx.State):
    """Estado para manejar las notas."""
    notes: List[Dict[str, Any]] = []
    new_note_title: str = ""
    new_note_content: str = ""
    new_note_tags: str = ""
    is_creating: bool = False
    
    def toggle_creating(self):
        """Alternar formulario de creación."""
        self.is_creating = not self.is_creating
        if not self.is_creating:
            # Limpiar formulario al cancelar
            self.new_note_title = ""
            self.new_note_content = ""
            self.new_note_tags = ""
    
    def add_note(self):
        """Agregar nueva nota."""
        if self.new_note_title.strip() and self.new_note_content.strip():
            colors = ["bg-blue-200", "bg-pink-200", "bg-green-200", "bg-yellow-200", "bg-purple-200", "bg-orange-200"]
            
            note = {
                "id": len(self.notes) + 1,
                "title": self.new_note_title,
                "content": self.new_note_content,
                "tags": [tag.strip() for tag in self.new_note_tags.split(",") if tag.strip()] if self.new_note_tags else [],
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "color": random.choice(colors)
            }
            self.notes = [note] + self.notes  # Agregar al inicio
            # Limpiar formulario
            self.new_note_title = ""
            self.new_note_content = ""
            self.new_note_tags = ""
            self.is_creating = False
    
    def delete_note(self, note_id: int):
        """Eliminar nota."""
        self.notes = [note for note in self.notes if note["id"] != note_id]
    
    def open_notes_form(self):
        """Abrir formulario de notas (llamado desde navbar)."""
        self.is_creating = True
    
    @rx.var
    def has_notes(self) -> bool:
        """Verificar si tiene notas."""
        return len(self.notes) > 0

def CreateForm() -> rx.Component:
    """Formulario para crear nueva nota."""
    return rx.cond(
        NotesState.is_creating,
        rx.box(
            rx.vstack(
                rx.input(
                    placeholder="Note title...",
                    value=NotesState.new_note_title,
                    on_change=NotesState.set_new_note_title,
                    class_name="border-2 border-black font-medium focus:ring-2 focus:ring-green-400 w-full px-3 py-2"
                ),
                rx.text_area(
                    placeholder="Write your note here...",
                    value=NotesState.new_note_content,
                    on_change=NotesState.set_new_note_content,
                    class_name="border-2 border-black font-medium min-h-[100px] focus:ring-2 focus:ring-green-400 w-full px-3 py-2",
                    rows=4
                ),
                rx.input(
                    placeholder="Tags (comma separated)...",
                    value=NotesState.new_note_tags,
                    on_change=NotesState.set_new_note_tags,
                    class_name="border-2 border-black font-medium focus:ring-2 focus:ring-green-400 w-full px-3 py-2"
                ),
                rx.hstack(
                    Button(
                        text="Save Note",
                        icon="save",
                        color="green",
                        on_click=NotesState.add_note
                    ),
                    Button(
                        text="Cancel",
                        icon="x",
                        color="white",
                        on_click=NotesState.toggle_creating
                    ),
                    spacing="3"
                ),
                spacing="4"
            ),
            class_name="mb-6 bg-gray-50 border-4 border-black p-4 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]"
        )
    )

def NoteItem(note: Dict[str, Any]) -> rx.Component:
    """Componente individual de nota."""
    return rx.box(
        rx.vstack(
            # Header con título y botones
            rx.hstack(
                rx.heading(
                    note["title"],
                    size="4",
                    class_name="text-lg font-bold"
                ),
                rx.hstack(
                    Button(
                        text="",
                        icon="edit",
                        color="white",
                        size="small"
                    ),
                    Button(
                        text="",
                        icon="trash-2",
                        color="red",
                        size="small",
                        on_click=lambda: NotesState.delete_note(note["id"])
                    ),
                    spacing="2"
                ),
                justify="between",
                align="start",
                width="100%"
            ),
            
            # Contenido
            rx.text(
                note["content"],
                class_name="text-sm font-medium whitespace-pre-wrap"
            ),
            
            # Footer con tags y fecha
            rx.hstack(
                rx.hstack(
                    rx.foreach(
                        note["tags"],
                        lambda tag: rx.hstack(
                            rx.icon("tag", size=12),
                            rx.text(tag, class_name="text-xs font-bold"),
                            class_name="text-xs font-bold bg-white border border-black px-2 py-1 rounded",
                            spacing="1"
                        )
                    ),
                    spacing="2",
                    wrap="wrap"
                ),
                rx.text(
                    note["created_at"],
                    class_name="text-xs font-bold text-gray-600"
                ),
                justify="between",
                align="center",
                width="100%"
            ),
            spacing="3",
            align="start"
        ),
        class_name=f"{note['color']} border-4 border-black p-4 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transform rotate-1 hover:scale-105 transition-all cursor-pointer"
    )

def EmptyState() -> rx.Component:
    """Estado vacío cuando no hay notas."""
    return rx.cond(
        ~NotesState.has_notes,
        rx.center(
            rx.vstack(
                rx.icon("book-open", size=48, class_name="text-gray-400"),
                rx.text(
                    "No notes yet!",
                    class_name="text-lg font-bold text-gray-600"
                ),
                rx.text(
                    "Create your first note to get started.",
                    class_name="text-sm font-medium text-gray-500"
                ),
                spacing="3",
                align="center",
                class_name="bg-gray-100 border-4 border-black p-6 transform -rotate-1"
            ),
            class_name="py-8"
        )
    )

def NotesSection() -> rx.Component:
    """Sección principal de notas."""
    return rx.box(
        rx.vstack(
            # Header
            rx.hstack(
                rx.heading(
                    "📚 Notes",
                    size="8",
                    class_name="text-3xl font-black"
                ),
                Button(
                    text="New Note",
                    icon="plus",
                    color="green",
                    on_click=NotesState.toggle_creating
                ),
                justify="between",
                align="center",
                width="100%"
            ),
            
            # Formulario de creación
            CreateForm(),
            
            # Lista de notas
            rx.box(
                rx.cond(
                    NotesState.has_notes,
                    rx.vstack(
                        rx.foreach(NotesState.notes, NoteItem),
                        spacing="4"
                    ),
                    rx.fragment()
                ),
                EmptyState(),
                width="100%"
            ),
            
            spacing="6",
            align="start",
            width="100%"
        ),
        id="notes-section",
        class_name="bg-white border-4 border-black p-6 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] w-full"
    )