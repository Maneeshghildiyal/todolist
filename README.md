
# Todo List App

A simple and user-friendly Todo List application built with Python's `tkinter` library and styled with `ttkbootstrap`. This app allows you to manage your tasks efficiently, with features like adding, marking as done, deleting, and viewing task statistics.

---

## Features

- **Add Tasks**: Input new tasks into the list.
- **Mark as Done**: Mark tasks as completed with a green highlight.
- **Delete Tasks**: Remove tasks from the list.
- **Task Statistics**: View total tasks and completed tasks.
- **Persistent Storage**: Automatically saves tasks to a JSON file (`tasks.json`) and reloads them on startup.
- **Modern Styling**: Styled with `ttkbootstrap` for an enhanced user interface.

---

## Requirements

- Python 3.7 or later
- Required Python libraries:
  - `ttkbootstrap`

---

## Installation

1. **Clone or Download the Repository**:
   ```bash
   git clone https://github.com/your-repository/todo-list-app.git
   cd todo-list-app
   ```

2. **Install Dependencies**:
   Install the required Python library using pip:
   ```bash
   pip install ttkbootstrap
   ```

3. **Run the Application**:
   Execute the Python script:
   ```bash
   python todo_list_app.py
   ```

---

## How to Use

1. **Add a Task**:
   - Enter your task in the input field. 
   - Click the **Add** button to add it to the list.

2. **Mark as Done**:
   - Select a task from the list.
   - Click the **Done** button to mark it as completed (text color changes to green).

3. **Delete a Task**:
   - Select a task from the list.
   - Click the **Delete** button to remove it.

4. **View Task Statistics**:
   - Click the **View Stats** button to see the total number of tasks and completed tasks.

---

## File Structure

- **`todo_list_app.py`**: Main Python script for the application.
- **`tasks.json`**: Automatically generated file to store tasks persistently.

---

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your enhancements or bug fixes.

