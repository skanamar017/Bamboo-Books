"""
Basic note creation, reading, updating, and deletion via command line
YAML header parsing and manipulation
Note searching and filtering capabilities
Simple formatting options
"""

#import os
import yaml 
from datetime import datetime
from typing import List, Dict, Optional

class Note: # title:str, created: datetime, and modified: datetime are required fields, tags: list[str], author: str, status: str, and priority: int (1-5) are optional fields
    def __init__(self, title:str, content: str, tags: Optional[List[str]] = None, author: Optional[str] = None, status: Optional[str] = None, priority: Optional[int] = None): 
        self.title = title
        self.content = content
        self.created = datetime.now()
        self.modified = datetime.now()
        self.tags = tags if tags is not None else []
        self.author = author
        self.status = status
        self.priority = priority
