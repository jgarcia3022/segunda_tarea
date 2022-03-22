import Bd
from sqlalchemy import Column, Integer, String

class Slang507(Bd.Base):
    __tablename__ = 'Slang'

    id = Column(Integer, primary_key=True)
    palabra = Column(String, nullable=False)
    definicion = Column(String, nullable=False)

    def __init__(self, palabra, definicion):
        self.palabra = palabra
        self.definicion = definicion

    def __repr__(self):
        return f'( {self.palabra}, {self.definicion})'

    def __str__(self):
        return self.definicion