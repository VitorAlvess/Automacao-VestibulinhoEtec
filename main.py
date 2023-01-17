# %%
import csv
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

# Inicializando o driver do Chrome

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.maximize_window()

# Acessando login (se precisar)
# driver.get("https://www.vestibulinhoetec.com.br/classificacao/")
# sleep(5)
# driver.find_element('xpath','//*[@id="CPF"]' ).send_keys('seusdados')
# driver.find_element('xpath','//*[@id="Senha"]' ).send_keys('suasenha')
# sleep(2)
# driver.find_element('xpath','//*[@id="primaryBox"]/div/div[2]/div/div/div[2]/form/div/div/button' ).click()
# sleep(2)

# driver.get("https://www.vestibulinhoetec.com.br/classificacao/")
# sleep(2)




# %%
driver.execute_script(f"window.scrollTo(0, 300)")
driver.find_element('xpath',f'//*[@id="change-table"]/tbody/tr[1]/td/label').click() #Modalidade (Mudar o numero entre parenteses para escolher mudar a modalidade)
driver.execute_script(f"window.scrollTo(0, 500)")
sleep(2)
select = Select(driver.find_element('xpath', '//*[@id="CodCidade"]'))
select.select_by_value('9668') #codigo do municipio de são paulo

# %%
sleep(2)
driver.execute_script(f"window.scrollTo(0, 700)")
select_option = driver.find_element('xpath', '//*[@id="CodEtec"]')
options_select_etec = select_option.find_elements(By.TAG_NAME, "option")
# Obtendo o tamanho
size_select_etec = len(options_select_etec)
sleep(2)
print(size_select_etec)
for xx in range(size_select_etec):
    xx = xx + 28
    if xx != 0:
        print(f'ETEC:{xx}')
        select_etec = Select(driver.find_element('xpath', '//*[@id="CodEtec"]'))
        select_etec.select_by_index(xx) #Selecionar ETEC
        sleep(5)
        
        select_option_cursoeperiodo = driver.find_element('xpath', '//*[@id="CodEscolaCurso"]')
        options_select_cursoeperiodo= select_option_cursoeperiodo.find_elements(By.TAG_NAME, "option")
        size_select_cursoeperiodo = len(options_select_cursoeperiodo)


        for i_select_cursoeperiodo in range(size_select_cursoeperiodo):
            if i_select_cursoeperiodo != 0:
                select_curso = Select(driver.find_element('xpath', '//*[@id="CodEscolaCurso"]'))
                select_curso.select_by_index(i_select_cursoeperiodo)
                sleep(2)
                driver.find_element('xpath', '//*[@id="form"]/div[6]/button').click()
                sleep(3)
                classificação_opcoes = driver.find_elements('xpath','/html/body/div[2]/div/div[2]/div/ul/li' )
                print(len(classificação_opcoes))
                for xxx in range(len(classificação_opcoes)):
                    classificar = xxx + 1
                    driver.execute_script(f"window.scrollTo(0, 500)")
                    sleep(2)
                    driver.find_element('xpath',f'/html/body/div[2]/div/div[2]/div/ul/li[{classificar}]/a' ).click()
                    sleep(5)
                    
                    
                    tbody = driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/div[3]/table/tbody')
                    rows = tbody.find_elements('xpath',"/html/body/div[2]/div/div[2]/div/div[3]/table/tbody/tr")
                    # Iterando sobre as linhas
                    data = []

                    nome1 = driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/h3' )
                    nome2 = driver.find_element('xpath','/html/body/div[2]/div/div[2]/div/h4' )
                    print(nome1.text)
                    print(nome2.text)
                    nome_completo = nome1.text + nome2.text
                    print(nome_completo)

                    for row in rows:
                        cells = row.find_elements(By.TAG_NAME, 'td')
                        row_data = [cell.text for cell in cells]
                        row_data.append(nome_completo)
                        data.append(row_data)

                    with open(f"{nome_completo}.csv", "w", newline="") as f:
                        writer = csv.writer(f)
                        for row in data:
                            writer.writerow(row)
                    
                    
                    
                    
                    driver.back()
                    sleep(5)
                driver.back()
                
                



# %%



