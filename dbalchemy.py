# -*- coding: utf-8 -*-

from flask_sqlalchemy import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func, label

db = SQLAlchemy()

class ModelDefault(db.Model):
    __abstract__ = True

    @classmethod
    def create(cls, commit=True, **kwargs):
        instance = cls(**kwargs)
        if commit:
            return instance.save()
        return instance.save(commit=commit)

    @classmethod
    def create_from_dict(cls, d):
        assert isinstance(d, dict)
        instance = cls(**d)
        return instance.save()

    @classmethod
    def create_many_from_list(cls, data_list):
        assert isinstance(data_list, list)

        db.session.add_all(
            [cls(**k) for k in data_list if isinstance(k, dict)]
        )
        try:
            db.session.commit()
        except Exception as e:
            return (e, 5002)

        return True

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)
        return commit and self.save() or self

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except Exception as e:
                if isinstance(e, sqlalchemy.exc.IntegrityError):
                    return (e, 5001)
                return (e, 5002)
        return self

    def delete(self, commit=True):
        db.session.delete(self)
        return commit and db.session.commit()


