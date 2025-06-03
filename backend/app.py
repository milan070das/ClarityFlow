from flask import Flask, request, jsonify
from flask_cors import CORS  # Allows frontend (React) to interact with this backend
from datetime import datetime, timedelta
from models import db, Task  # Importing the SQLAlchemy instance and Task model

app = Flask(__name__)
CORS(app)  # Enables Cross-Origin Resource Sharing (CORS)

# Configuring SQLite database for storing tasks
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db.init_app(app)  # Binds SQLAlchemy to the Flask app

# Create all database tables (only runs once on app startup)
with app.app_context():
    db.create_all()

# GET /tasks - Fetch all tasks (auto-deletes old completed ones before returning)
@app.route('/tasks', methods=['GET'])
def get_tasks():
    auto_delete_completed_tasks()  # Clean up old completed tasks
    tasks = Task.query.all()  # Fetch all tasks from the database
    return jsonify([task.to_dict() for task in tasks])  # Return tasks as JSON list

# POST /tasks - Add a new task to the database
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json  # Get task data from the request
    task = Task(
        title=data['title'],
        completed=data['completed'],
        priority=data['priority'],
        dueDate=data['dueDate'],
        completed_at=datetime.utcnow() if data['completed'] else None  # Save timestamp if task is marked completed
    )
    db.session.add(task)  # Add task to the session
    db.session.commit()   # Save it to the database
    return jsonify(task.to_dict()), 201  # Return the newly created task

# DELETE /tasks/<id> - Delete a task by ID
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)  # Find task or return 404
    db.session.delete(task)  # Mark it for deletion
    db.session.commit()      # Save changes to database
    return '', 204

# Auto-delete logic: removes completed tasks older than a certain time (1 minute here)
def auto_delete_completed_tasks():
    expiration_time = datetime.utcnow() - timedelta(minutes=1)  # Define expiration threshold
    # Find all completed tasks that were marked done before the expiration time
    old_tasks = Task.query.filter(Task.completed == True, Task.completed_at <= expiration_time).all()
    for task in old_tasks:
        db.session.delete(task)  # Mark each for deletion
    db.session.commit()  # Apply deletions to the DB

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)