from controller.driver import ChromeDriverController
from controller.elements import ElementsWhatsapp
from controller.list_contacts import Contact, ListContacts
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class WhatsappNotification:

    def __init__(self, chrome: ChromeDriverController, list_contacts: ListContacts) -> None:
        self.chrome = chrome
        self.list_contacts = list_contacts
        self.chrome.get_element_with_tuple(ElementsWhatsapp.load, 60)
        time.sleep(1)
        self.default = None
        self.get_default_contact()
        self.get_all_contacts()
    
    def get_default_contact(self) -> Contact:
        try:
            element = self.chrome.get_element_with_tuple(ElementsWhatsapp.default_contact)
            c = Contact('default', element)
            self.list_contacts.add(c)
            self.default = c
        except Exception as e:
            raise Exception("ERROR GET DEFAULT CONTACT - " + str(e))
        
    def get_all_contacts(self):
        try:
            div_contats = self.chrome.driver.find_elements(*ElementsWhatsapp.div_contacts)
            for div in div_contats:
                span = div.find_element(By.TAG_NAME, 'span')
                if span:
                    self.list_contacts.add(Contact(span.text, div))
        except Exception as e:
            raise Exception("ERROR GET CONTACTS - " + str(e))
        
    def send_message(self, c: Contact, message: str):
        try:
            c.element.click()
            input = self.chrome.get_element_with_tuple(ElementsWhatsapp.input_message)
            if not input:
                raise Exception("Não foi possivel enviar a mensagem")
            input.click()
            input.send_keys(message, Keys.ENTER)
            self.default.element.click()
        except Exception as e:
            raise Exception("ERROR SEND MESSAGE - " + str(e))
        
    def send_message_new_contact(self, number: str, message: str):
        try:
            btn = self.chrome.get_element_with_tuple(ElementsWhatsapp.btn_new_contact)
            btn.click()
            input = self.chrome.driver.execute_script("return document.activeElement")
            input.send_keys(number)
            try:
                contact = self.chrome.get_element_with_tuple(ElementsWhatsapp.span_new_contact)
                contact.click()
                input_message = self.chrome.get_element_with_tuple(ElementsWhatsapp.input_message)
                if not input_message:
                    raise Exception("Não foi possivel enviar a mensagem")
                input_message.click()
                input_message.send_keys(message, Keys.ENTER)
                self.default.element.click()
            except:
                self.send_message(self.list_contacts.get_contact('default'), f'O contato {number} não foi encontrado, a mensagem que seria enviada era: {message}')

        except Exception as e:
            raise Exception("ERROR SEND MESSAGE NEW CONTACT - " +str(e))