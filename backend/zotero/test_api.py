import pytest
from rich import print
from zotero.api import Zotero


@pytest.fixture
def zotero_client():
    return Zotero()


def test_get_collections(zotero_client):
    collections = zotero_client.get_collections()
    assert len(collections) > 0


def test_get_collection_ids(zotero_client):
    collection_ids = zotero_client.get_collection_ids()
    assert len(collection_ids) > 0
    print(collection_ids)


def test_get_items_for_collection(zotero_client):
    collection_key = "XI7V5WM2"  # Collection 'AZA'
    collections = zotero_client.get_items_for_collection(collection_key)
    assert len(collections) > 0


def test_pdf_folders(zotero_client):
    collection_name = "CLIMATE"
    collection_key = zotero_client.get_collection_id_for_name(collection_name)
    pdf_list = zotero_client.get_pdf_folders(collection_key)
    assert len(pdf_list) > 0
    print(pdf_list)
