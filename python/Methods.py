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

import creation_reading
import search_list 
import edit_delete 


def main():
    notes_dir="directory"
    search_list.ensure_notes_directory(notes_dir)
    #test for note creation, reading, and YAML implemention
    note_first = creation_reading.create_note("My First Note", "Hello There!")
    creation_reading.save_note_to_file(note_first, "note_first.txt")
    read_note_first = creation_reading.read_note_from_file("note_first.txt")
    print(f"Title: {read_note_first.title}\nContent: {read_note_first.content}")
    note_second = creation_reading.create_note("My Second Note", "Example Test!", ["example", "test"])
    creation_reading.save_note_to_file(note_second, "note_second.txt")
    read_note_second = creation_reading.read_note_from_file("note_second.txt")
    print(f"Title: {read_note_second.title}\nContent: {read_note_second.content}")
    
    #test for note listing and basic search
    notes_5=[
        ("My Favorite Anime", "Jojo's Bizzare adventure, Fullmetal, Dragon Ball", ["anime", "intrests"]),
        ("Weekend Plans", "I will work on this project and watch the Fantastic Four movie", ['plans', 'Marvel', 'productive']),
        ('Tasks for Tonight', 'finish this part of the project and update Linkedin from what Lam said', ['career', 'friend']),
        ('Harry Potter review', 'Boy spends 7 years being third wheel', ['fantacy', 'review', 'shitpost']),
        ('wakrjfh', 'ekhufgs kaeufhslieu aeukhfg keufb', ['random', 'bull', 'shit'])
    ]
    for i, (title, content, tags) in enumerate(notes_5, start=1):
        note = creation_reading.create_note(title, content, tags)
        filename = os.path.join(notes_dir, f"note{i}.txt")
        note.filename = filename
        creation_reading.save_note_to_file(note, filename)
    print("\nAll Notes:")
    all_notes = search_list.list_all_notes(notes_dir)
    search_list.display_note_list(all_notes)
    print("\nSearch for 'Plans' in titles:")
    results_title = search_list.search_notes(all_notes, "Plans")
    search_list.display_note_list(results_title)
    print("\nSearch for 'Project' in titles:")
    results_content = search_list.search_notes(all_notes, "Project")
    search_list.display_note_list(results_content)
    print("\nSearch for tag 'shit':")
    results_tag = search_list.search_notes(all_notes, "shit")
    search_list.display_note_list(results_tag)
    print("\nSearch note for tag 'intrests':")
    interest_tag_list=search_list.list_note_by_tag(all_notes,"intrests")
    search_list.display_note_list(interest_tag_list)

    #test for note editing and deletion
    print(notes_dir)
    while True:
        question=input("Select: edit, delete, press andy other key to quit \n")
        if question=='edit':
            note_used=edit_delete.select_note_interactively(all_notes)
            note_used=edit_delete.edit_note(note_used, notes_dir)
        elif question=='delete':
            note_used=edit_delete.select_note_interactively(all_notes)
            is_deleted=edit_delete.delete_note(note_used, notes_dir)
            print(is_deleted)
        else:
            print("quitting")
            break


if __name__ == "__main__":
    main()

