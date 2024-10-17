from pydantic import BaseModel, HttpUrl, field_validator
from typing import Optional, List, Dict, Any


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
    attachmentType: Optional[str] = None
    attachmentSize: Optional[int] = None
    title: Optional[str] = None
    length: Optional[int] = None


class Meta(BaseModel):
    creatorSummary: Optional[str] = None
    parsedDate: Optional[str] = None
    numChildren: Optional[int] = None


class Creator(BaseModel):
    creatorType: str
    firstName: Optional[str] = None
    lastName: Optional[str] = None
    name: Optional[str] = None


class Tag(BaseModel):
    tag: str


class Data(BaseModel):

    @field_validator('url', mode='before')
    def validate_url(cls, v):
        if v == '':
            return None
        return v
    
    key: str
    version: int
    itemType: str
    title: Optional[str] = None
    creators: Optional[List[Creator]] = None
    abstractNote: Optional[str] = None
    publicationTitle: Optional[str] = None
    volume: Optional[str] = None
    issue: Optional[str] = None
    pages: Optional[str] = None
    date: Optional[str] = None
    series: Optional[str] = None
    seriesTitle: Optional[str] = None
    seriesText: Optional[str] = None
    journalAbbreviation: Optional[str] = None
    language: Optional[str] = None
    DOI: Optional[str] = None
    ISSN: Optional[str] = None
    shortTitle: Optional[str] = None
    url: Optional[HttpUrl] = None
    accessDate: Optional[str] = None
    archive: Optional[str] = None
    archiveLocation: Optional[str] = None
    libraryCatalog: Optional[str] = None
    callNumber: Optional[str] = None
    rights: Optional[str] = None
    extra: Optional[str] = None
    tags: Optional[List[Tag]] = None
    collections: Optional[List[str]] = None
    relations: Dict[str, Any]
    dateAdded: Optional[str] = None
    dateModified: Optional[str] = None
    parentItem: Optional[str] = None
    linkMode: Optional[str] = None
    note: Optional[str] = None
    contentType: Optional[str] = None
    charset: Optional[str] = None
    filename: Optional[str] = None
    md5: Optional[str] = None
    mtime: Optional[int] = None


class ItemResponse(BaseModel):
    key: str
    version: int
    library: Library
    links: Dict[str, Links]
    meta: Optional[Meta] = None
    data: Data
