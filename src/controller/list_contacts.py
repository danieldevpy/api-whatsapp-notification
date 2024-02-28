from dataclasses import dataclass
from selenium.webdriver.remote.webelement import WebElement
from typing import Dict

@dataclass
class Contact:
    name: str
    element: WebElement



class ListContacts:
    
    def __init__(self) -> None:
        self.list: Dict[str, Contact] = {}

    def add(self, c: Contact):
        self.list[c.name] = c

    def get_contacts_list(self):
        return [key for key in self.list]
    
    def get_contact(self, number: str):
        if number in self.list:
            return self.list[number]
        return False