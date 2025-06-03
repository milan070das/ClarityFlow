from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a SQLAlchemy database instance
db = SQLAlchemy()

# Define the Task model (represents a task in the database)
class Task(db.Model):
    # Unique identifier for each task (Primary Key)
    id = db.Column(db.Integer, primary_key=True)

    # Title of the task (cannot be null)
    title = db.Column(db.String(120), nullable=False)

    # Boolean flag to indicate if the task is completed (default is False)
    completed = db.Column(db.Boolean, default=False)

    # Task priority (High, Medium, Low — default is Medium)
    priority = db.Column(db.String(10), default='Medium')

    # Optional due date stored as a string (e.g., "2025-06-03")
    dueDate = db.Column(db.String(20), default='')

    # Timestamp for when the task was completed (used for auto-deletion)
    completed_at = db.Column(db.DateTime, nullable=True)

    # Method to convert the Task object into a dictionary (for JSON response)
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'completed': self.completed,
            'priority': self.priority,
            'dueDate': self.dueDate,
            # Note: completed_at is not returned to the frontend
        }
