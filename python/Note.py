"""
Basic note creation, reading, updating, and deletion via command line
YAML header parsing and manipulation
Note searching and filtering capabilities
Simple formatting options
"""

#import os
#import yaml 
from datetime import datetime
from typing import List, Dict, Optional

class Note: # title:str, created: datetime, and modified: datetime are required fields, tags: list[str], author: str, status: str, and priority: int (1-5) are optional fields
    def __init__(self, title:str, content: str): 
        self.title = title
        self.content = content

def create_note(title: str, content: str) -> Note:
    """Create a new note with the given title and content."""
    note = Note(title, content)
    return note

def write_to_file(filename: str, content: str) -> None:
    """Write the given content to a file."""
    with open(filename, "w") as file:
        file.write(content)

def save_note_to_file(note: Note, filename: str) -> None:
    """Save the note to a file."""
    file_content = note.title + "\n" + "=" * len(note.title) + "\n\n" + note.content
    write_to_file(filename, file_content)

def read_from_file(filename: str) -> str:
    """Read content from a file and return it as a string."""
    with open(filename, "r") as file:
        return file.read()  

def read_note_from_file(filename: str) -> Note:
    """Read a note from a file and return a Note object."""
    content = read_from_file(filename)
    lines = content.split("\n")
    title = lines[0].strip()
    note_content = "\n".join(lines[3:]) # Skip the title and separator lines
    return Note(title, note_content)

def main():
    # Example usage
    note = create_note("My First Note", "Hello World!")
    save_note_to_file(note, "note1.txt")
    
    # Read the note back from the file
    read_note = read_note_from_file("note1.txt")
    print(f"Title: {read_note.title}\nContent: {read_note.content}")

if __name__ == "__main__":
    main()
