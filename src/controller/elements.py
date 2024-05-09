from selenium.webdriver.common.by import By


class ElementsWhatsapp:
  # foto do wpp para reconhecer quando o whatsapp abriu
  load = (By.CLASS_NAME, 'x1n2onr6')
  # pegar a div que abre as conversas
  div_contacts = (By.CLASS_NAME, 'Mk0Bp')
  # pegar o contato padrão
  # default_contact = (By.CLASS_NAME, "_ahlk")
  default_contact = (By.XPATH, "//span[@data-icon='pinned2']")
  # pegar todas as mensagens que não foram abertas
  waiting_messages = (By.CLASS_NAME, 'aumms1qt')
  # pegar o numero/nome do contato que está aberto
  name_header = (By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/span')
  # pegar todas as mensagens da conversa que está aberta
  conversation_message = (By.CLASS_NAME, "_akbu")
  # Input aonde envia a mensagem para a pessoa
  input_message = (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
  # input novo contato
  input_new_contact = (By.XPATH, "//span[@data-icon='new-chat-outline']")
  # span reconhecer numero
  new_contacts_div = (By.CLASS_NAME, '_ak8q')
