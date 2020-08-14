#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'), primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'), primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='places', viewonly=False)
    else:
        @property
        def reviews(self):
            """Return list of Review instances with place_id equal to current
            Place.id."""
            reviews_list = []
            for review in models.storage.all(Review).values:
                if self.id == review.place_id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """Getter that returns the list of Amenity instances
            that contain all Amenity.id linked to the Place."""
            list_amenities = []
            for amenity in models.storage.all(Amenity).values:
                if self.id == amenity.place_id:
                    list_amenities.append(amenity)
            return list_amenities

        @amenities.setter
        def amenities(self, obj):
            """Setter that handles append method for adding an Amenity.id."""
            if isinstance(obj, 'Amenity'):
                self.amenity_ids.append(obj.id)
