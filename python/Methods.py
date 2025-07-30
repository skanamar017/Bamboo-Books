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






















#note listing and basic search

#make a notes directory if one doesn't exist yet
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
            note = read_note_from_file(file)
            note["filename"]=file   #FIX HERE

            #FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE 
            #FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE 
            #FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE 
            #FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE 
            #FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE 
            #FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE 
            #FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE 
            #FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE 
            #FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE 
            #FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE FIX HERE 
  



            notes.append(note)
        except:
            print("Warning: Could not read "+file)
    return notes

def search_notes(notes, query):
    results=[]
    query=query.lower()

    for note in notes:
        if query in note.title.lower():
            results.append(note)
            continue
        if query in note.content.lower():
            results.append(note)
            continue
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

    




        
















def main():
    notes_dir="directory"
    ensure_notes_directory(notes_dir)


    note1 = create_note("My First Note", "Hello There!")
    save_note_to_file(note1, "note1.txt")
    read_note1 = read_note_from_file("note1.txt")
    print(f"Title: {read_note1.title}\nContent: {read_note1.content}")

    note2 = create_note("My Second Note", "Example Test!", ["example", "test"])
    save_note_to_file(note2, "note2.txt")
    read_note2 = read_note_from_file("note2.txt")
    print(f"Title: {read_note2.title}\nContent: {read_note2.content}")

    notes_5=[
        ("My Favorite Anime", "Jojo's Bizzare adventure, Fullmetal, Dragon Ball", ["anime", "intrests"]),
        ("Weekend Plans", "I will work on this project and watch the Fantastic Four movie", ['plans', 'Marvel', 'productive']),
        ('Tasks for Tonight', 'finish this part of the project and update Linkedin from what Lam said', ['career', 'friend']),
        ('Harry Potter review', 'Boy spends 7 years being third wheel', ['fantacy', 'review', 'shitpost']),
        ('wakrjfh', 'ekhufgs kaeufhslieu aeukhfg keufb', ['random', 'bull', 'shit'])
    ]


    for i, (title, content, tags) in enumerate(notes_5, start=3):
        note = create_note(title, content, tags)
        filename = os.path.join(notes_dir, f"note{i}.txt")
        save_note_to_file(note, filename)

    print(list_files_in_directory(notes_dir))

    print("\nAll Notes:")
    all_notes = list_all_notes(notes_dir)
    display_note_list(all_notes)


    print("\nSearch for 'Plans' in titles:")
    results_title = search_notes(all_notes, "Plans")
    display_note_list(results_title)

    print("\nSearch for 'Project' in titles:")
    results_content = search_notes(all_notes, "Project")
    display_note_list(results_content)


    print("\n🔍 Search for tag 'shit':")
    results_tag = search_notes(all_notes, "shit")
    display_note_list(results_tag)


if __name__ == "__main__":
    main()


