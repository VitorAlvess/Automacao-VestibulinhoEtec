# Vestibulinhoetec web scraping

# Ideia do projeto

- Criar um script que consiga:
    - Navegar pelo site do [vestibulinhoetec.com.br](http://vestibulinhoetec.com.br) pegando todos os dados de alunos ✅
    - Salvar os dados em um arquivo CSV ✅

# 2023:

- Script executado e ao concatenar os resultados CSV, chegou a um total de 73 mil linhas de alunos com suas devidas classificações , abrangendo as categorias de Ensino Médio Regular - 1ª série, Ensino Médio com Habilitação Técnica Profissional - 1ª série - (M-Tec), Ensino Médio com Habilitação Técnica Profissional - 1ª série - (M-Tec - PI) - Período Integral e Cursos de Especialização

# Instalações necessarias:

- Python
- Selenium

```jsx
pip install selenium
```

- chromedriver
    - Descobrir a versão do chrome instalado
    - Baixar nesse site [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)
    - salvar na pasta do script

# Passo a passo realizado pelo script:

- Se precisar fazer login é só descomentar o codigo refente a login e inserir seus dados no codigo
1. Navega até [www.vestibulinhoetec.com.br/home](https://www.vestibulinhoetec.com.br/home/)
    
    ![Screenshot_1.png](Vestibulinhoetec%20web%20scraping%20a6e23cad9c9845a08f1378c69e0411c3/Screenshot_1.png)
    
2. Click “Ver classificação geral”
    
    ![Untitled](Vestibulinhoetec%20web%20scraping%20a6e23cad9c9845a08f1378c69e0411c3/Untitled.png)
    
3. Seleciona qual modalidade deseja, como por exemplo: “Ensino Médio Regular - 1ª série”
    
    ![Untitled](Vestibulinhoetec%20web%20scraping%20a6e23cad9c9845a08f1378c69e0411c3/Untitled%201.png)
    
    - Lembre-se de alterar no **código** para escolher qual o script deve **selecionar!**
4. Click no dropdown e seleciona o município definido no código ( Script está definido como 9668 = São Paulo )   . 
    
    ![Untitled](Vestibulinhoetec%20web%20scraping%20a6e23cad9c9845a08f1378c69e0411c3/Untitled%202.png)
    
    ![Untitled](Vestibulinhoetec%20web%20scraping%20a6e23cad9c9845a08f1378c69e0411c3/Untitled%203.png)
    
5. Seleciona a etec
    
    ![Untitled](Vestibulinhoetec%20web%20scraping%20a6e23cad9c9845a08f1378c69e0411c3/Untitled%204.png)
    
6. Seleciona o curso e período
    
    ![Untitled](Vestibulinhoetec%20web%20scraping%20a6e23cad9c9845a08f1378c69e0411c3/Untitled%205.png)
    
7. Click em continuar.
8. Click “Lista de Classificação - 1ª opção”
    
    ![Untitled](Vestibulinhoetec%20web%20scraping%20a6e23cad9c9845a08f1378c69e0411c3/Untitled%206.png)
    
9. Recolhe todos os dados
    
    ![Untitled](Vestibulinhoetec%20web%20scraping%20a6e23cad9c9845a08f1378c69e0411c3/Untitled%207.png)
    
10. Repete todos os passos anteriores alterando para pegar todos os dados