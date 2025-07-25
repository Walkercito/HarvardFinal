import reflex as rx
from typing import List, Dict, Any
from datetime import datetime
from .Button import Button

class TaskState(rx.State):
    """Estado para manejar las tareas."""
    tasks: List[Dict[str, Any]] = []
    new_task: str = ""
    show_advanced_form: bool = False
    filter_status: str = "all"  # all, pending, completed
    new_task_priority: str = "medium"
    new_task_due_date: str = ""
    
    def add_task(self):
        """Agregar nueva tarea."""
        if self.new_task.strip():
            task = {
                "id": len(self.tasks) + 1,
                "text": self.new_task,
                "completed": False,
                "priority": self.new_task_priority,
                "due_date": self.new_task_due_date,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            self.tasks.append(task)
            self.new_task = ""
            self.new_task_priority = "medium"
            self.new_task_due_date = ""
            self.show_advanced_form = False
    
    def toggle_task(self, task_id: int):
        """Alternar estado de completado de una tarea."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = not task["completed"]
                break
    
    def delete_task(self, task_id: int):
        """Eliminar tarea."""
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
    
    def toggle_advanced_form(self):
        """Alternar formulario avanzado."""
        self.show_advanced_form = not self.show_advanced_form
    
    def set_filter(self, status: str):
        """Cambiar filtro de tareas."""
        self.filter_status = status
    
    @rx.var
    def filtered_tasks(self) -> List[Dict[str, Any]]:
        """Obtener tareas filtradas."""
        if self.filter_status == "all":
            return self.tasks
        elif self.filter_status == "pending":
            return [task for task in self.tasks if not task["completed"]]
        else:  # completed
            return [task for task in self.tasks if task["completed"]]
    
    @rx.var
    def has_tasks(self) -> bool:
        """Verificar si tiene tareas."""
        return len(self.tasks) > 0

def FilterButtons() -> rx.Component:
    """Botones de filtro para las tareas."""
    return rx.hstack(
        rx.cond(
            TaskState.filter_status == "all",
            Button(
                text="All",
                color="blue",
                on_click=lambda: TaskState.set_filter("all"),
                size="small"
            ),
            Button(
                text="All",
                color="white",
                on_click=lambda: TaskState.set_filter("all"),
                size="small"
            )
        ),
        rx.cond(
            TaskState.filter_status == "pending",
            Button(
                text="Pending",
                color="yellow",
                on_click=lambda: TaskState.set_filter("pending"),
                size="small"
            ),
            Button(
                text="Pending",
                color="white",
                on_click=lambda: TaskState.set_filter("pending"),
                size="small"
            )
        ),
        rx.cond(
            TaskState.filter_status == "completed",
            Button(
                text="Completed",
                color="green",
                on_click=lambda: TaskState.set_filter("completed"),
                size="small"
            ),
            Button(
                text="Completed",
                color="white",
                on_click=lambda: TaskState.set_filter("completed"),
                size="small"
            )
        ),
        spacing="2"
    )

def AdvancedForm() -> rx.Component:
    """Formulario avanzado para crear tareas."""
    return rx.cond(
        TaskState.show_advanced_form,
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.text("Priority", class_name="text-sm font-bold"),
                    rx.select(
                        ["low", "medium", "high"],
                        value=TaskState.new_task_priority,
                        on_change=TaskState.set_new_task_priority,
                        class_name="border-2 border-black"
                    ),
                    spacing="1"
                ),
                rx.vstack(
                    rx.text("Due Date", class_name="text-sm font-bold"),
                    rx.input(
                        type="date",
                        value=TaskState.new_task_due_date,
                        on_change=TaskState.set_new_task_due_date,
                        class_name="border-2 border-black"
                    ),
                    spacing="1"
                ),
                spacing="4"
            ),
            spacing="3",
            class_name="bg-gray-100 border-2 border-black p-3 mt-3"
        )
    )

def TaskItem(task: Dict[str, Any]) -> rx.Component:
    """Componente para mostrar una tarea individual."""
    return rx.hstack(
        rx.checkbox(
            checked=task["completed"],
            on_change=lambda checked: TaskState.toggle_task(task["id"]),
            class_name="mr-3"
        ),
        rx.vstack(
            rx.cond(
                task["completed"],
                rx.text(
                    task["text"],
                    class_name="font-medium line-through text-gray-500"
                ),
                rx.text(
                    task["text"],
                    class_name="font-medium"
                )
            ),
            rx.hstack(
                rx.text(
                    f"Priority: {task['priority']}",
                    class_name="text-xs text-gray-600"
                ),
                rx.cond(
                    task["due_date"] != "",
                    rx.text(
                        f"Due: {task['due_date']}",
                        class_name="text-xs text-gray-600"
                    ),
                    rx.fragment()
                ),
                spacing="3"
            ),
            align="start",
            spacing="1"
        ),
        rx.spacer(),
        Button(
            text="",
            icon="trash-2",
            color="red",
            size="small",
            on_click=lambda: TaskState.delete_task(task["id"])
        ),
        align="center",
        class_name=f"bg-{task['priority']}-100 border-2 border-black p-3 shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transition-all w-full"
    )

def EmptyTaskState() -> rx.Component:
    """Estado vacío cuando no hay tareas."""
    return rx.cond(
        ~TaskState.has_tasks,
        rx.center(
            rx.vstack(
                rx.icon("check-circle", size=48, class_name="text-gray-400"),
                rx.text(
                    "No tasks yet!",
                    class_name="text-lg font-bold text-gray-600"
                ),
                rx.text(
                    "Add your first task to get started.",
                    class_name="text-sm font-medium text-gray-500"
                ),
                spacing="3",
                align="center",
                class_name="bg-gray-100 border-4 border-black p-6 transform rotate-1"
            ),
            class_name="py-8"
        )
    )

def TaskSection() -> rx.Component:
    """Sección principal de tareas."""
    return rx.box(
        rx.vstack(
            # Header con título y filtros
            rx.hstack(
                rx.heading(
                    "📝 Tasks",
                    size="8",
                    class_name="text-3xl font-black"
                ),
                FilterButtons(),
                justify="between",
                align="center",
                width="100%"
            ),
            
            # Formulario de nueva tarea
            rx.vstack(
                rx.hstack(
                    rx.input(
                        placeholder="Add a new task...",
                        value=TaskState.new_task,
                        on_change=TaskState.set_new_task,
                        class_name="border-4 border-black font-medium focus:outline-none focus:ring-2 focus:ring-blue-400 px-3 py-2",
                        width="100%"
                    ),
                    Button(
                        text="",
                        icon="settings",
                        color="purple",
                        on_click=TaskState.toggle_advanced_form
                    ),
                    Button(
                        text="",
                        icon="plus",
                        color="blue",
                        on_click=TaskState.add_task
                    ),
                    spacing="2",
                    width="100%"
                ),
                AdvancedForm(),
                spacing="0",
                width="100%"
            ),
            
            # Lista de tareas
            rx.box(
                rx.cond(
                    TaskState.has_tasks,
                    rx.vstack(
                        rx.foreach(TaskState.filtered_tasks, TaskItem),
                        spacing="3"
                    ),
                    rx.fragment()
                ),
                EmptyTaskState(),
                width="100%"
            ),
            
            spacing="6",
            align="start",
            width="100%"
        ),
        id="task-section",
        class_name="bg-white border-4 border-black p-6 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] w-full"
    )