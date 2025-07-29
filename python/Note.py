"""
Basic note creation, reading, updating, and deletion via command line
YAML header parsing and manipulation
Note searching and filtering capabilities
Simple formatting options
"""
#import yaml
from datetime import datetime


# add a way to include vim


class Note:
    def __init__(self, title, created, modified, tags=None, author=None, status=None, priority=None):
        self.title = title #is string
        self.created = created #is datatime object
        self.modified = modified #is datatime object
        self.tags = tags if tags is not None else []
        self.author = author #is string
        self.status = status #status is either "in review" or "completed"
        self.priority = priority #priority is integer from 1 to 5
        self.header=[self.title, self.created, self.modified, self.tags, self.author, self.status, self.priority]
        self.content = ""
    
    #getters
    def get_title(self):
        return self.title
     
    def get_created(self):
        return self.created

    def get_modified(self):
        return self.modified

    def get_tags(self):
        return self.tags

    def get_author(self):
        return self.author

    def get_status(self):
        return self.status

    def get_priority(self):
        return self.priority
    
    def get_header(self):
        return self.header

    def get_content(self):
        return self.content
    

    #setters
    def set_title(self, title):
        self.title = title
        self.modified = datetime.now()
        return self.title   
    
    def set_author(self, author):  
        self.author = author
        self.modified = datetime.now()
        return self.author
    
    def set_tags(self, tags):
        if not isinstance(tags, list):
            raise ValueError("Tags must be a list.")
        self.tags = tags
        self.modified = datetime.now()
        return self.tags

    def set_content(self, content):
        if not isinstance(content, str):
            raise ValueError("Content must be a string.")
        self.content = content
        self.modified = datetime.now()
        return self.content
    
    def set_priority(self, priority):
        if priority < 1 or priority > 5:
            raise ValueError("Priority must be an integer between 1 and 5.")
        self.priority = priority
        self.modified = datetime.now()
        return self.priority
    
    def set_status(self, status):
        if status not in ["in review", "completed"]:
            raise ValueError("Status must be either 'in review' or 'completed'.")
        self.status = status
        self.modified = datetime.now()
        return self.status
    

    
    def __repr__(self):
        return f"Note(title={self.title}, created={self.created}, modified={self.modified}, tags={self.tags}, author={self.author}, status={self.status}, priority={self.priority})"

    def __str__(self):
        return f"Title: {self.title}\nCreated: {self.created}\nModified: {self.modified}\nTags: {self.tags}\nAuthor: {self.author}\nStatus: {self.status}\nPriority: {self.priority}\nContent: {self.content}"
    


    def add_content(self, content):
        """Adds content to the note."""
        if not isinstance(content, str):
            raise ValueError("Content must be a string.")
        self.content += content
        self.modified = self.created  # Update modified time to created time when content is added
        self.header = [self.title, self.created, self.modified, self.tags, self.author, self.status, self.priority]
        print(f"statuses: {self.status}")
        print(f"priorities: {self.priority}")
        return self.content
    

