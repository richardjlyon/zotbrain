from pydantic import BaseModel, HttpUrl
from typing import Optional, Dict, Any


class LibraryLinks(BaseModel):
    href: HttpUrl
    type: str


class Library(BaseModel):
    type: str
    id: int
    name: str
    links: Dict[str, LibraryLinks]


class Links(BaseModel):
    href: HttpUrl
    type: str


class Meta(BaseModel):
    numCollections: Optional[int]
    numItems: int


class Data(BaseModel):
    key: str
    version: int
    name: str
    parentCollection: Optional[bool]
    relations: Dict[str, Any]


class CollectionResponse(BaseModel):
    key: str
    version: int
    library: Library
    links: Dict[str, Links]
    # meta: Meta
    data: Data
