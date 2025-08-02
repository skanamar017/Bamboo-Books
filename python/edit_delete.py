"""
Basic note creation, reading, updating, and deletion via command line
YAML header parsing and manipulation
Note searching and filtering capabilities
Simple formatting options
"""

import os

from datetime import datetime
from Note import Note
import shutil

import creation_reading

# note editing and deletion
def select_note_interactively(notes):
    print(f"Enter note number (1-{len(notes)})")  
    user_input=input()
    note_index=int(user_input)-1
    if note_index<0 or note_index>=len(notes):
        print("Invalid selection")
        return None
    return notes[note_index]
    
def edit_note(note, dir):
    print(f"Current title: {note.title}")
    print("New title (or press Enter to keep current): ")
    new_title=input()
    if new_title:
        note.title=new_title
    print(f"Current content: {note.content}")
    print("\nEnter new content (type 'END' on a line by itself to finish):")
    new_content=''
    while True:
        line=input()
        if line=="END":
            break
        new_content+=line+"\n"
    if new_content:
        note.content=new_content.strip()  
    print(f"Current tags: {", ".join(note.tags)}")
    print ("New tags (comma-separated, or Enter to keep current): ")
    tag_input=input()
    if tag_input:
        note.tags=tag_input.split(',')
        note.tags = [tag.strip() for tag in note.tags]
    note.modified=datetime.now()
    full_path = os.path.join(dir, os.path.basename(note.filename))    
    creation_reading.save_note_to_file(note, full_path)
    return note

def delete_note(note, dir):
    print(f"Are you sure you want to delete {note.title}?")
    conformation=input()
    if conformation.lower()!="yes":
        print("Deletion cancalled")
        return False
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file_name = f"{note.filename}.backup.{timestamp}"
    full_path = os.path.join(dir, os.path.basename(note.filename))
    shutil.copyfile(full_path, backup_file_name)
    print(f"Backup created: {backup_file_name}")
    os.remove(full_path)
    print(f"Deleted: {note.filename}")
    return True
