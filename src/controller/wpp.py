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
        self.body = self.chrome.get_element("body", By.TAG_NAME)

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
        conversation_element = None
        try:
            btn_new = self.chrome.get_element_with_tuple(ElementsWhatsapp.input_new_contact)
            btn_new.click()
            input_new = self.chrome.driver.execute_script("return document.activeElement")
            input_new.send_keys(number)
            time.sleep(1)
            elements = self.chrome.get_elements_with_tuple(ElementsWhatsapp.new_contacts_div)
            for element in elements:
                try:
                    span = element.find_element(By.TAG_NAME, 'span')
                    if span.text == number:
                        conversation_element = span
                        break
                except: pass
            if not conversation_element:
                self.key_esc()
                raise Exception("O contato não foi encontrado")
            conversation_element.click()
            input_conversation = self.chrome.driver.execute_script("return document.activeElement")
            input_conversation.send_keys(message, Keys.ENTER)
            all_messages = self.chrome.get_elements_with_tuple(ElementsWhatsapp.conversation_message)
            last_message = all_messages[-1]
            if not last_message.text == message:
                raise Exception("A mensagem não foi enviada corretamente")
            self.key_esc()
        except Exception as e:
            raise Exception("ERROR SEND NEW MESSAGE - " + str(e))
        
    def key_esc(self):
        self.body.send_keys(Keys.ESCAPE)