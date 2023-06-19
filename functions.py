import pandas as pd
df = pd.read_csv('treino-flask-dev/fabio-quirino/dados-flask-treino.csv')

# Tratando valores da coluna "salario" (transformando de str para float)
df['salario_float'] = df['salario'].str.replace("$","")
df['salario_float'] = pd.to_numeric(df['salario_float'])

### Funções
# Input -> país
# Output -> média salarial do país inputado
def media_salarial(dataframe, pais):
    x = dataframe
    x = x[x['pais'] == pais]
    media = round(x['salario_float'].mean(),2)
    return media

# Input -> país (str)
# Output -> média salarial por idade do país inputado 
def media_salarial_idade(dataframe, pais):
    x = dataframe
    x = x[x['pais'] == pais]
    x_1_20 = x[x['idade']<20]
    x_20_40 = x[(x['idade']>=20) & (x['idade']<40)]
    x_40_60 = x[(x['idade']>=40) & (x['idade']<60)]
    x_60_80 = x[(x['idade']>=60) & (x['idade']<80)]
    x_80_100 = x[(x['idade']>=80) & (x['idade']<=100)]
    l = [x_1_20,  
         x_20_40, 
         x_40_60, 
         x_60_80, 
         x_80_100]
    l2 = []
    media = 0
    for i in l:
        l2.append(round(i['salario_float'].mean(),2))
    return l2

# Input -> país
# Output -> representatividade de cada genero no país inputado (%)
def representatividade_genero(dataframe, pais):
    x = dataframe[dataframe["pais"] == pais]
    x1 = x["genero"].value_counts()
    total = x.count()[0]
    s = pd.Series((x1.values/total)*100, index = x1.index)
    s = s.round(2)
    return s

#Função cuja entrada é o país e o dataframe. Retorna uma str contendo o texto que vai para o site
#def texto(dataframe, pais):
#    return media_salarial(dataframe, pais) + "\n\n\n" + media_salarial_idade(dataframe, pais) + '\n\n' + representatividade_genero(dataframe, pais)



#print (media_salarial(df, 'Venezuela'))
#print (media_salarial_idade(df, 'Brazil'))
#print (representatividade_genero(df, 'Brazil'))
#print (texto(df, "Brazil"))
