import logging
from sqlalchemy import (
    Column, Integer, String, Boolean, Text, Enum, Numeric, inspect, or_
)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from biweeklybudget.models.base import Base, ModelAsDict
import enum

logger = logging.getLogger(__name__)

class PoolType(enum.Enum):
    Chlorine = 1
    Salt = 2
    Bromine = 3

class Pool(Base, ModelAsDict):

    __tablename__ = 'pool'
    __table_args__ = (
        {'mysql_engine': 'InnoDB'}
    )

    #: Primary Key
    id = Column(Integer, primary_key=True)

    #: Gallons of Water in the pool
    gallons = Column(Numeric(precision=4, scale=4))

    #: Type of Pool (Salt, Chlorine, Bromine)
    pool_type = Column(Enum(PoolType))

# class Chemicals(Base, ModelAsDict):

    def __repr__(self):
        return "<Pool(id=%d, name='%s')>" % (
            self.id, self.name
        )
