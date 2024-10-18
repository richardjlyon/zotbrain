import os
from pathlib import Path
from typing import List

import requests
from dotenv import load_dotenv
from rich import print

from zotero.models import CollectionResponse, ItemResponse, UserResponse


class Zotero:
    """
    Class to interact with the Zotero API
    """

    __api_base_url: str = "https://api.zotero.org"
    __file_system_base: Path = None
    __api_key: str = None
    __user_id: int = None

    def __init__(self):
        load_dotenv()
        self.__api_key = os.getenv("ZOTERO_API_KEY")
        if self.__api_key is None:
            raise ValueError("ZOTERO_API_KEY not found in environment variables")

        file_system_base = os.getenv("ZOTERO_LIBRARY_ROOT")
        if file_system_base is None:
            raise ValueError("ZOTERO_LIBRARY_ROOT not found in environment variables")
        self.__file_system_base = Path(file_system_base)

        self.__user_id = self.__get_user_id().user_id

    @property
    def __headers(self) -> dict:
        return {"Zotero-API-Key": self.__api_key}

    def __get_user_id(self) -> UserResponse:
        url = f"{self.__api_base_url}/keys/{self.__api_key}"
        response = requests.get(url, headers=self.__headers)
        response.raise_for_status()
        user = response.json()
        return UserResponse(**user)

    def get_collection_ids(self) -> List[dict]:
        """
        Get a dict of collection name and ids
        :return: a dict of collection name and ids
        """
        collections = self.get_collections()
        return {collection.data.name: collection.data.key for collection in collections}

    def get_collections(self) -> List[CollectionResponse]:
        """
        Get a list of collections
        :return: a list of CollectionResponse objects
        """
        url = f"{self.__api_base_url}/users/{self.__user_id}/collections"
        response = requests.get(url, headers=self.__headers)
        response.raise_for_status()
        collections = response.json()
        return [CollectionResponse(**collection) for collection in collections]

    def get_items_for_collection(self, collection_key: str) -> List[ItemResponse]:
        """
        Get a list of items for a given collection
        :param collection_key: the key of the collection
        :return: a list of ItemResponse objects
        """
        url = f"{self.__api_base_url}/users/{self.__user_id}/collections/{collection_key}/items"
        response = requests.get(url, headers=self.__headers)
        response.raise_for_status()
        items = response.json()
        out = []
        for item in items:
            try:
                out.append(ItemResponse(**item))
            except Exception as e:
                print(e, item)
                raise e

        return out

    def get_pdf_folders(self, collection_key: str) -> List[Path]:
        """
        Get a list of PDF folder paths for a given collection
        :param collection_key:  the key of the collection
        :return: a list of Path objects to PDF files in the file system
        """
        items = self.get_items_for_collection(collection_key)
        attachment_keys = [
            item.data.key
            for item in items
            if item.data.contentType == "application/pdf"
        ]

        return [
            self.__file_system_base / "storage" / attachment_key
            for attachment_key in attachment_keys
        ]
