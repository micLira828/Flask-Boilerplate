from datetime import datetime
from app.extensions import db

class Item(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)
  
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relationship: one album has many tracks
    items = db.relationship(
        "Item",
        back_populates="parent",
        cascade="all, delete-orphan",
        lazy=True
    )

    def to_dict(self, include_tracks=False):
        data = {
            "id": self.id,
            "title": self.title,
            "created_at": self.created_at.isoformat() if self.created_at else None,
        }

        if include_items:
            data["items"] = [i.to_dict() for i in self.items]

        return data