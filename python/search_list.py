"""
Basic note creation, reading, updating, and deletion via command line
YAML header parsing and manipulation
Note searching and filtering capabilities
Simple formatting options
"""

import os
from datetime import datetime
from Note import Note

import creation_reading 



#note listing and basic search
def ensure_notes_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

def list_files_in_directory(path):
    files = []
    for item in os.listdir(path): # goes through each item in the directory specified by the path
        full_path = os.path.join(path, item) # combines directory path and item name
        if os.path.isfile(full_path):
            files.append(item)
    return files

def list_all_notes(notes_directory):
    files = list_files_in_directory(notes_directory)
    note_files = []
    for file in files:
        if file.endswith(".note") or file.endswith(".txt"):
            note_files.append(file)
    notes=[]
    for file in note_files:
        try: 
            full_path = os.path.join(notes_directory, file)
            note = creation_reading.read_note_from_file(full_path)
            note.filename=file
            notes.append(note)
        except:
            print("Warning: Could not read "+file)
    return notes

def list_note_by_tag(notes, tag):
    results=[]
    for note in notes:
        if tag in note.tags:
            results.append(note)
    return results

def search_notes(notes, query):
    results=[]
    query=query.lower()
    for note in notes:
        if query in note.title.lower() or query in note.content.lower():
            results.append(note)
        for tag in note.tags:
            if query in tag.lower():
                results.append(note)
                break
    return results

def display_note_list(notes):
    print(f"Found {len(notes)} notes:\n")
    for i, note in enumerate(notes):
        print(f"{i+1}. {note.title}")
        print(f"    Created: {note.created}")
        if len(note.tags)>0:
            print(f"    Tags: {", ".join(note.tags)}")
        print("")

def display_note(note):
    print(f"Title: {note.title}")
    print(f"Created: {note.created}")
    print(f"Modified: {note.modified}")
    if len(note.tags)>0:
        print(f"Tags: {", ".join(note.tags)}")
    print("\n"+note.content)
