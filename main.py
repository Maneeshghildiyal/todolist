import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json


class TodoListApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Todo List App")
        self.geometry("400x400")
        style = Style(theme="flatly")
        style.configure("Custom.TEntry", foreground="gray")

        # Input field for adding tasks
        self.task_input = ttk.Entry(
            self, font=("TkDefaultFont", 16), width=30, style="Custom.TEntry"
        )
        self.task_input.pack(pady=10)

        # Placeholder for input field
        self.placeholder_text = "Enter your todo here..."
        self.task_input.insert(0, self.placeholder_text)

        # Bind events to handle placeholder
        self.task_input.bind("<FocusIn>", self.clear_placeholder)
        self.task_input.bind("<FocusOut>", self.restore_placeholder)

        # Button to add tasks
        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)

        # Listbox to display tasks
        self.task_list = tk.Listbox(
            self, font=("TkDefaultFont", 16), height=10, selectmode=tk.SINGLE
        )
        self.task_list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Buttons for task management
        ttk.Button(self, text="Done", style="success.TButton",
                   command=self.mark_done).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Delete", style="danger.TButton",
                   command=self.delete_task).pack(side=tk.RIGHT, padx=10, pady=10)

        # Button for task statistics
        ttk.Button(self, text="View Stats", style="info.TButton",
                   command=self.view_stats).pack(side=tk.BOTTOM, pady=10)

        # Load saved tasks
        self.load_tasks()

    def clear_placeholder(self, event):
        """Clear placeholder when user focuses on input."""
        if self.task_input.get() == self.placeholder_text:
            self.task_input.delete(0, tk.END)
            self.task_input.configure(style="TEntry")

    def restore_placeholder(self, event):
        """Restore placeholder if input is empty."""
        if self.task_input.get() == "":
            self.task_input.insert(0, self.placeholder_text)
            self.task_input.configure(style="Custom.TEntry")

    def add_task(self):
        """Add a new task."""
        task = self.task_input.get().strip()
        if task and task != self.placeholder_text:
            self.task_list.insert(tk.END, task)
            self.task_list.itemconfig(tk.END, fg="orange")
            self.task_input.delete(0, tk.END)
            self.restore_placeholder(None)  # Restore placeholder if needed
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a valid task.")

    def mark_done(self):
        """Mark a selected task as done."""
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.itemconfig(task_index, fg="green")
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to mark as done.")

    def delete_task(self):
        """Delete a selected task."""
        task_index = self.task_list.curselection()
        if task_index:
            self.task_list.delete(task_index)
            self.save_tasks()
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def view_stats(self):
        """Display statistics about tasks."""
        done_count = 0
        total_count = self.task_list.size()
        for i in range(total_count):
            if self.task_list.itemcget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo(
            "Task Statistics", f"Total tasks: {total_count}\nCompleted tasks: {done_count}"
        )

    def load_tasks(self):
        """Load tasks from the JSON file."""
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    self.task_list.insert(tk.END, task["text"])
                    self.task_list.itemconfig(tk.END, fg=task["color"])
        except FileNotFoundError:
            pass

    def save_tasks(self):
        """Save tasks to the JSON file."""
        data = []
        for i in range(self.task_list.size()):
            text = self.task_list.get(i)
            color = self.task_list.itemcget(i, "fg")
            data.append({"text": text, "color": color})
        with open("tasks.json", "w") as f:
            json.dump(data, f)


if __name__ == "__main__":
    app = TodoListApp()
    app.mainloop()
