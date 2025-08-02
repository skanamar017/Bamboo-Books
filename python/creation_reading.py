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
import shutil

#note creation, reading, and YAML implemention
def create_note(title: str, content: str, tags: Optional[List[str]]=None) -> Note:
    """Create a new note with the given title and content."""
    note = Note(title, content, tags=tags)
    return note

def write_to_file(filename: str, content: str) -> None:
    """Write the given content to a file."""
    with open(filename, "w") as file:
        file.write(content)

def save_note_to_file(note: Note, filename: str) -> None:
    """Save the note to a file."""
    yamlHeader = "---\n"
    yamlHeader += "title: " + note.title + "\n"  
    yamlHeader += "created: " + str(note.created) + "\n"
    yamlHeader += "modified: " + str(note.modified) + "\n"
    yamlHeader += "tags: [" + ", ".join(note.tags) + "]\n"
    yamlHeader += "---\n\n"
    note.filename = filename  
    file_content = yamlHeader + note.content
    write_to_file(filename, file_content)

def read_from_file(filename: str) -> str:
    """Read content from a file and return it as a string."""
    with open(filename, "r") as file:
        return file.read()  
    
def read_note_from_file(filename: str) -> Note:
    """Read a note from a file and return a Note object."""
    content = read_from_file(filename)
    if not content.startswith("---"):
        raise ValueError("File does not contain a valid YAML header.")  
    parts=content.split("---", 2)
    yaml_section = parts[1].strip()
    note_content = parts[2].strip() if len(parts) > 2 else ""
    metadata = yaml.safe_load(yaml_section) 
    title = metadata.get("title", "")
    content = note_content
    tags = metadata.get("tags", [])
    note=Note(title, content, tags)  
    note.created = metadata.get("created")
    note.modified = metadata.get("modified")
    note.tags = metadata.get("tags", []) 
    return note

