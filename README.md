# ZotBrain

This is an application for extracting structured data from a Zotero library of academic papers.

A backend server is used to extract data from the Zotero API and store it in a database. The frontend is a React application that allows users to search and filter the data.

## How to use

- install all deps including uv with mise `mise install`
- install python with uv `uv python install`
- init venv with uv `uv venv`
- run commands with uv run `uv run --package zotero pytest -f`
