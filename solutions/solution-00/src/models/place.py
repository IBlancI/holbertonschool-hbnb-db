"""
Place related functionality
"""

from src.models.base import Base
from src.models.city import City
from src.models.user import User
from src import db


class Place(Base):
    __tablename__ = 'place'

    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    host_id = db.Column(db.String(36), db.ForeignKey('user.id'), nullable=False)
    city_id = db.Column(db.String(36), db.ForeignKey('city.id'), nullable=False)
    price_per_night = db.Column(db.Float, nullable=False)
    number_of_rooms = db.Column(db.Integer, nullable=False)
    number_of_bathrooms = db.Column(db.Integer, nullable=False)
    max_guests = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Place {self.id} ({self.name})>"

    def to_dict(self):
        return {
            "name": self.name,
            "id": self.id,
            "description": self.description,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "address": self.address,
            "host_id": self.host_id,
            "city_id": self.city_id,
            "number_of_rooms": self.number_of_rooms,
            "price_per_night": self.price_per_night,
            "max_guests": self.max_guests,
            "number_of_bathrooms": self.number_of_bathrooms,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @staticmethod
    def create(place_data):
        """Create a new place"""
        user = User.query.get(place_data["host_id"])
        if user is None:
            raise ValueError(f"User with ID {place_data['host_id']} not found")

        city = City.query.get(place_data["city_id"])
        if city is None:
            raise ValueError(f"City with ID {place_data['city_id']} not found")

        new_place = Place(**place_data)
        db.session.add(new_place)
        db.session.commit()
        return new_place

    @staticmethod
    def update(place_id, data):
        """Update an existing place"""
        place = Place.query.get(place_id)

        if place is None:
            return None

        for key, value in data.items():
            setattr(place, key, value)

        db.session.commit()
        return place
