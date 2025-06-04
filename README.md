# 🚀 ClarityFlow — Intelligent Task Manager & Productivity Booster

ClarityFlow is a sleek, modern task management web application designed to help individuals and teams organize, prioritize, and track their work efficiently. Built with a powerful **React** frontend and a lightweight **Python Flask** backend, ClarityFlow combines an intuitive UI with a robust API to deliver a seamless productivity experience.

---

## ✨ Key Features

- **Task Creation & Editing:** Add, update, and delete tasks with ease.
- **Priority Levels:** Assign priorities to tasks (High, Medium, Low) for better organization.
- **Auto-Delete Completed Tasks:** Automatically remove tasks marked completed after 2 hours.
- **Dynamic UI:** Smooth animations for task addition, deletion, and updates using React Transition Group.
- **Multi-Tab Synchronization:** Real-time updates between tabs (optional extension).
- **RESTful API:** Flask backend provides task CRUD endpoints.
- **CORS Enabled:** Enables smooth communication between React frontend and Flask backend.
- **Dark Mode (Planned):** Prepare for theme toggling.
- **Expandable for Authentication:** Easily integrate login/signup features.

---

## 🛠️ Tech Stack

| Layer           | Technology                     |
|-----------------|--------------------------------|
| Frontend        | React, React Transition Group |
| Backend         | Python, Flask, Flask-CORS     |
| API Communication | Axios                        |
| State Management | React Hooks (useState, useEffect) |
| Styling         | CSS, React Animations         |

---

## 📁 Project Structure

```plaintext
ClarityFlow/
├── backend/
│   ├── app.py                    # Flask backend app with RESTful APIs
│   ├── requirements.txt         # Python dependencies for backend
├── frontend/
│   ├── public/                  # Static files (index.html, favicon, etc.)
│   ├── src/
│   │   ├── components/          # React components (TaskList, TaskForm, etc.)
│   │   ├── App.js               # Main React app component
│   │   ├── index.js             # React entry point
│   │   ├── App.css              # Styling and animations
│   ├── package.json             # Node dependencies
├── README.md                    # Project documentation
├── .gitignore                   # Ignore files for Git
