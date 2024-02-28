from selenium.webdriver.common.by import By


class ElementsWhatsapp:
  # foto do wpp para reconhecer quando o whatsapp abriu
  load = (By.CLASS_NAME, "_3WByx")
  # pegar a div que abre as conversas
  div_contacts = (By.CLASS_NAME, 'Mk0Bp')
  # pegar o contato padrão
  default_contact = (By.CLASS_NAME, "_2H6nH")
  # pegar todas as mensagens que não foram abertas
  waiting_messages = (By.CLASS_NAME, 'aumms1qt')
  # pegar o numero/nome do contato que está aberto
  name_header = (By.XPATH, '//*[@id="main"]/header/div[2]/div/div/div/span')
  # pegar todas as mensagens da conversa que está aberta
  conversation_message = (By.CLASS_NAME, "_21Ahp")
  # Input aonde envia a mensagem para a pessoa
  input_message = (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')
  # button novo contato
  btn_new_contact = (By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[4]/div/span')
  # input novo contato
  input_new_contact = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]/div/div[1]')
  # span reconhecer numero
  span_new_contact = (By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div[2]/div[2]/div[2]/div/div/span')