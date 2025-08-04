"""
Basic note creation, reading, updating, and deletion via command line
YAML header parsing and manipulation
Note searching and filtering capabilities
Simple formatting options
"""

import os
import pathlib
import yaml 
from datetime import datetime
from typing import List, Dict, Optional
from Note import Note

class SearchQuery:
    def __init__(
        self,
        text_query: str,
        required_tags: Optional[List[str]] = None,
        excluded_tags: Optional[List[str]] = None,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        title_only: bool = False
    ):
        self.text_query = text_query
        self.required_tags = required_tags if required_tags is not None else []
        self.excluded_tags = excluded_tags if excluded_tags is not None else []
        self.date_from = date_from
        self.date_to = date_to
        self.title_only = title_only


def parse_search_query(query_string: str) -> SearchQuery:
    query = SearchQuery()
    parts = query_string.split()
    text_parts = []

    for part in parts:
        if part.startswith("tag:"):
            query.required_tags.append(part[4:])
        elif part.startswith("-tag:"):
            query.excluded_tags.append(part[5:])
        elif part.startswith("after:"):
            try:
                query.date_from = datetime.strptime(part[6:], "%Y-%m-%d")
            except ValueError:
                pass  # Handle invalid date format if needed
        elif part.startswith("before:"):
            try:
                query.date_to = datetime.strptime(part[7:], "%Y-%m-%d")
            except ValueError:
                pass
        elif part == "title:":
            query.title_only = True
        else:
            text_parts.append(part)

    query.text_query = " ".join(text_parts)
    return query

def matches_query(note, query):
    # Text search
    if query.text_query:
        query_lower = query.text_query.lower()
        found = False
        if query.title_only:
            found = query_lower in note.title.lower()
        else:
            found = query_lower in note.title.lower() or query_lower in note.content.lower()
        if not found:
            return False
    # Required tags
    for required_tag in query.required_tags:
        if required_tag not in note.tags:
            return False
    # Excluded tags
    for excluded_tag in query.excluded_tags:
        if excluded_tag in note.tags:
            return False
    # Date range
    if query.date_from and note.created < query.date_from:
        return False
    if query.date_to and note.created > query.date_to:
        return False
    return True

def advanced_search(notes, search_query):
    results = []
    for note in notes:
        if matches_query(note, search_query):
            results.append(note)
    return results

def get_all_tags(notes):
    all_tags = set()
    for note in notes:
        for tag in note.tags:
            all_tags.add(tag)
    return sorted(all_tags)


def get_notes_with_tag(notes, tag_name):
    return [note for note in notes if tag_name in note.tags]

