"""
  This script defines the DBRepository class, which serves as a concrete implementation
  of the abstract Repository (Storage) interface. The DBRepository class provides
  methods for interacting with the database, including:
    - get_all: Retrieve all records of a specific model.
    - get: Retrieve a single record by its ID.
    - save: Persist a new record.
    - update: Commit changes to an existing record.
    - delete: Remove a record.
    - reload: (Currently not implemented)
"""

from src.persistence.repository import Repository
from src.models.base import Base
from src.models import User
from src import db


class DBRepository(Repository):
    """Concrete implementation of the Repository interface for database operations"""

    def __init__(self) -> None:
        """Initialize the DBRepository with the required models"""
        from src.models.user import User  # Import User model

        # Mapping model names to their respective classes
        self.models = {
            "users": User
        }

    def get_all(self, model_name: str) -> list:
        """Retrieve all instances of a given model"""
        model_class = Base._decl_class_registry.get(model_name.capitalize())
        if model_class:
            return model_class.query.all()
        return []

    def get(self, model_name: str, obj_id: str) -> Base | None:
        """Retrieve a specific instance by ID"""
        model_class = Base._decl_class_registry.get(model_name.capitalize())
        if model_class:
            return model_class.query.get(obj_id)
        return None

    def reload(self) -> None:
        """Reload method (currently not implemented)"""

    def save(self, obj: Base) -> None:
        """Persist a new object to the database"""
        db.session.add(obj)
        db.session.commit()

    def update(self, obj: Base) -> None:
        """Commit changes to an existing object"""
        db.session.commit()

    def delete(self, obj: Base) -> bool:
        """Remove an object from the database"""
        db.session.delete(obj)
        db.session.commit()
        return True
