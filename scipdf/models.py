from typing import Optional, List
from pydantic import BaseModel

class Grobid(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True)
    authors: Optional[str] = Field(default=None, sa_column=Column(JSON))
    pub_date: str
    title: str
    abstract: str
    sections: List[dict] = Field(default=None, sa_column=Column(JSON))
    doi: str = Field(unique=True)