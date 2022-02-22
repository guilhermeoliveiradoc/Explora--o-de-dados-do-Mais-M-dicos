#!/usr/bin/env python
# coding: utf-8

# In[47]:


get_ipython().system('pip install requests')
import pandas as pd
import requests
from pandas.io.json import json_normalize


# In[48]:


base = requests.get("https://servicodados.ibge.gov.br/api/v3/agregados/6696/periodos/2010|2011|2012|2013|2014|2015|2016|2017|2018/variaveis/9732?localidades=N3[all]").json()
base_2 = base[0]['resultados'][0]['series']
b2_flat = json_normalize(base_2)
b3_flat = pd.DataFrame(b2_flat)
del b3_flat['localidade.nivel.id']
del b3_flat['localidade.nivel.nome']

b3_flat2 = b3_flat.rename(columns={'localidade.id':'id','localidade.nome': 'Estado', 'serie.2010': '2010', 'serie.2011':'2011', 'serie.2012':'2012', 'serie.2013': '2013', 'serie.2014': '2014', 'serie.2015': '2015', 'serie.2016': '2016', 'serie.2017': '2017', 'serie.2018': '2018'})

#b3_flat.drop(columns=['localidade.id','localidade.nome'], axis=1)

b3_flat2

b32 = pd.melt(b3_flat2, id_vars = ['Estado', 'id'], var_name = 'Year', value_name= 'valor')

b32.to_excel('b3a.xlsx')


# In[49]:


base_nascimentos = requests.get('https://servicodados.ibge.gov.br/api/v3/agregados/7498/periodos/2013|2014|2015|2016|2017|2018/variaveis/11598?localidades=N3[all]').json()
base_nasc1 = base_nascimentos[0]['resultados'][0]['series']
base_nasc2 = json_normalize(base_nasc1)
del base_nasc2['localidade.nivel.id']
del base_nasc2['localidade.nivel.nome']

#adicionando valores zerados ao dataframe

base_nasc3 = base_nasc2.rename(columns={'localidade.id': 'id', 'localidade.nome':'Estado', 'serie.2013': '2013', 'serie.2014':'2014', 'serie.2015':'2015', 'serie.2016':'2016', 'serie.2017':'2017', 'serie.2018':'2018'})

base_nasc4 = pd.DataFrame(base_nasc3)

base_nasc4.loc[:,'2010'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
base_nasc4.loc[:,'2011'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
base_nasc4.loc[:,'2012'] = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

#base_nasc4.to_excel('base_nasc4.xlsx') 

base_nasc5 = pd.melt(base_nasc4, id_vars= ["Estado", "id"], var_name = 'Year', value_name = 'valor')

#base_nasc6 = base_nasc5.xlsx

base_nasc5.to_excel('base5.xlsx')


# In[50]:


get_ipython().system('pip install psycopg2')


# In[51]:


import psycopg2

connect = psycopg2.connect(
                host = 'localhost',
                dbname = 'ironhack', 
                user ='postgres', 
                password ='281904',
                port = 5432)

cursor = connect.cursor()

funcao1 = "CREATE TABLE dados_natalidade2(id int PRIMARY KEY, name varchar(20) NOT NULL)"
cursor.execute(funcao1)
connect.commit()

cursor.close()
connect.close()


# In[60]:


#connect = psycopg2.connect(
host = 'localhost',
dbname = 'ironhack', 
user ='postgres', 
password ='281904',
port = 5432


# In[53]:


import sqlalchemy as db
db_server = 'postgresql'
user = 'postgres'
password = '281904'
ip = '127.0.0.1:5432'
db_name = 'ironhack'
engine = db.create_engine(f'{db_server}://{user}:{password}@{ip}/{db_name}')
conn = engine.connect()


# In[118]:


base_nasc4.to_sql(name='dados_natalidade1', con=conn, if_exists='append', index=False, schema ='projeto' )

#aqui eu coloquei três novas bases com dados mais precisos para investigar o tema

nova_base1 = pd.read_excel(r"C:\Users\User\Pictures\projeto\projeto2\Número de nascidos vivos cujas mães fizeram sete ou mais consultas de pré-natal segundo anos de estudo da mãe.xls")

nova_base2 = pd.read_excel(r"C:\Users\User\Pictures\projeto\projeto2\Número de nascidos vivos.xls")

nova_base3 = pd.read_excel(r"C:\Users\User\Pictures\projeto\projeto2\Proporção de óbitos de menores de um ano de idade por causas claramente evitáveis.xls")

# e daí então eu tive que tornar essas bases "long"

novab1df = pd.DataFrame(nova_base1)
novab2df = pd.DataFrame(nova_base2)
novab3df = pd.DataFrame(nova_base3)

novab1df

novab1dflong = pd.melt(novab1df, id_vars=['Localidade', 'Código IBGE', 'Código DataSUS'], value_name='Núm de nascidos vivos cujas mães fizeram sete ou mais consultas de pré-natal no ano', var_name='Ano')

with pd.ExcelWriter(r"C:\Users\User\Pictures\projeto\projeto2\novas bases\finalb 7 pré natais.xlsx") as writer:
    novab1dflong.to_excel(writer)  



# In[119]:


#novab1df = pd.DataFrame(nova_base1)
#novab2df = pd.DataFrame(nova_base2)
#novab3df = pd.DataFrame(nova_base3)

novab2df

novab2dflong = pd.melt(novab2df, id_vars=['Localidade', 'Código IBGE', 'Código DataSUS'], value_name='Núm de nascidos vivos', var_name='Ano')

with pd.ExcelWriter(r"C:\Users\User\Pictures\projeto\projeto2\novas bases\final numero de nascidos vivos.xlsx") as writer:
    novab2dflong.to_excel(writer)  

#novab2dflong.to_excel('número de nascidos vivos.xlsx')


# In[120]:


novab3df

novab3dflong = pd.melt(novab3df, id_vars=['Localidade', 'Código IBGE', 'Código DataSUS'], value_name='Proporção de óbitos de menores de um ano de idade por causas claramente evitáveis', var_name='Ano')

with pd.ExcelWriter(r"C:\Users\User\Pictures\projeto\projeto2\novas bases\final proporcao de obitos 2.xlsx") as writer:
    novab3dflong.to_excel(writer)  


# In[ ]:




