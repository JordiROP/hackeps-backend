from enum import Enum
from typing import Optional
from pydantic import EmailStr, BaseModel, Field


from app.modules.base.models import BaseUser

class Status(str, Enum):
    accepted = 'ACCEPTED'
    rejected = 'REJECTED'
    dropped = 'DROPPED'
    waiting = 'WAITING'

class User(BaseUser):
    id:Optional[str] = Field(description='User id, must be the same as the generated in the register process')
    country:str = Field(description='Country')
    auto_comunity:str = Field(description='Autonomous Comunity')
    city:str = Field(description='City')
    street:str = Field(description='Street')
    postal_code:int = Field(description='Postal code')
    number:int = Field(description='Direction street number')
    linkedin:Optional[str] = Field(description='Link to LinkedIn profile')
    git:Optional[str] = Field(description='Link to github profile')
    gdpr:bool = Field(description='Boolean True or False depending on if user has accepted the gdpr')
    terms:bool = Field(description='Boolean True or False depending on if user has accepted the terms and conditions')
    email:EmailStr = Field(description='User email')
    team:str = Field(description='Team reference')
    status: Status = Field(description='User status ACCEPT, REJECTED, DROPED, WAITING')

class Teams(BaseModel):
    name:str
    