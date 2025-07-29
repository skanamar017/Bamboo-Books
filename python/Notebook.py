"""
Basic note creation, reading, updating, and deletion via command line
YAML header parsing and manipulation
Note searching and filtering capabilities
Simple formatting options
"""

#import yaml
from platform import node
from Note import Note 
from datetime import datetime
import subprocess
import os



class Notebook:
    def __init__(self):
        self.notes = []

    def create_note(self, title, author=None, status=None, priority=None): #create a note with vim
        """Creates a new note with the given title and optional metadata."""
        created = datetime.now()
        modified = created
        new_note = Note(title, created, modified, author=author, status=status, priority=priority)
        self.notes.append(new_note)
        return new_note

    def list_notes(self):
        return self.notes

    def list_notes_by_tag(self, tag):
        return [note for note in self.notes if tag in note.tags]

    def read_note(self, title):
        for note in self.notes:
            if note.title == title:
                return note
        return None

    def edit_note(self, note): #edit a note with vim
        """Updates an existing note. Note must be an instance of Note."""
        if not isinstance(note, Note):
            raise ValueError("note must be an instance of Note")
        # Find the note in the notebook and update it
        note.add_content(str(input("Enter new content for the note: ")))
        note.modified = datetime.now()

    def delete_note(self, title):
        note = self.read_note(title)
        if note:
            self.notes.remove(note)
            return True
        return False

    def search_query(self, query):
        results = []
        for note in self.notes:
            if query.lower() in note.title.lower() or query.lower() in note.content.lower():
                results.append(note)
        return results

    def stats(self):
        return {
            'total_notes': len(self.notes),
            'tags': {tag for note in self.notes for tag in note.tags},
            'authors': {note.author for note in self.notes if note.author},
            'statuses': {note.status for note in self.notes if note.status},
            'priorities': {note.priority for note in self.notes if note.priority}
        }
    

def main():
    notebook = Notebook()
    note1 = notebook.create_note("First Note", author="Alice", status="in review", priority=3)
    content1 = str(input("Enter content for the first note: "))
    note1.edit_note(content1)

    note2 = notebook.create_note("Second Note", author="Bob", status="completed", priority=5)
    content2 = str(input("Enter content for the second note: "))
    note2.edit_note(content2)

    print(note1)
    print(note2)
    
    print("All notes in the notebook:")
    for note in notebook.list_notes():
        print(note.get_title())
    
    print("Searching for 'first':")
    search_results = notebook.search_query("first")
    for result in search_results:
        print(result.get_title())

if __name__ == "__main__":
    main()