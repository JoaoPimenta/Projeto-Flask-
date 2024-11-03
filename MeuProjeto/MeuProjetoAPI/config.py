import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///meus_dados.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False