from typing import Optional
from sqlalchemy import func
from sqlalchemy.sql.expression import select, delete
from storage.database import Session


class BaseCRUDModel():

    @classmethod
    def get(cls, filters: Optional[dict] = {}):
        """Get method for all tables, fetches all items from database

        Args:
            filters (Optional[dict], optional): filters for called table . Defaults to {}.

        Returns:
            list: list of all items from table in db
        """
        with Session() as db:
            stmt = select(cls)
            final_filters = []
            if filters == {}:
                items = db.execute(stmt).all()
                return items

            for key, value in filters.items():
                if type(value is int):
                    final_filters.append(getattr(cls, key) == value)
                else:
                    final_filters.append(
                        getattr(cls, key).like(value))

            stmt = stmt.filter(*final_filters)
            return (db.execute(stmt).all())

    @classmethod
    def get_by_id(cls, id):
        """Get by id method for all tables, get specific item from database

        Args:
            id (int): id of desired item

        Returns:
            (Row): item from database
        """
        with Session() as db:

            stmt = select(cls).where(cls.id == id)
            return (db.execute(stmt)).scallar()

    @classmethod
    def create(cls, **data):
        """Create method for all tables, creates a item in database

        Returns:
            id(int): id of newly created item
        """
        with Session() as db:
            rec = cls(**data)
            db.add(rec)
            db.commit()
        return {"id": rec.id}

    @classmethod
    def update(cls, index, **data):
        """Update method for all tables, updates a item in database with new information

        Args:
            index (int): id of the item to update
        """
        with Session() as db:
            stmt = select(cls).where(cls.id == index)
            rec = (db.execute(stmt).scallar())
            for key in data:
                setattr(rec, key, data[key])
            db.commit()

    @classmethod
    def delete_by_id(cls, id):
        """Delete method for all tables, removes specific item from database

        Args:
            id (int): id of desired item

        Returns:
            int: 1 or 0 either the item was deleted or not
        """
        with Session() as db:
            stmt = delete(cls).where(cls.id == id)
            res = db.execute(stmt).scallar()
            db.commit()
        return res.rowcount
