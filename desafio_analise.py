import pandas as pd

# Carregar o dataset
df = pd.read_csv('caminho_do_arquivo/netflix_titles.csv')

# Exibir as primeiras linhas para verificar a estrutura do dataset
df.head()

# 1. Quantos filmes estão disponíveis na Netflix?
# Filtrar o dataset para contar apenas as entradas onde o tipo é 'Movie'
num_movies = df[df['type'] == 'Movie'].shape[0]
print(f"Total de filmes na Netflix: {num_movies}")

# 2. Quem são os 5 diretores com mais filmes e séries na plataforma?
# Contar a frequência dos diretores e selecionar os 5 mais frequentes
directors_count = df['director'].value_counts().head(5)
print("Diretores com mais produções na Netflix:")
print(directors_count)

# 3. Quais diretores também atuaram como atores em suas próprias produções?
#cruzar as colunas 'director' e 'cast', sem contar as colunas 'director' e 'cast' sem valor
df_directors_actors = df.dropna(subset=['director', 'cast'])

# Verificar se algum nome de diretor está listado na coluna 'cast'
directors_actors = df_directors_actors[df_directors_actors.apply(lambda row: any(
    actor in row['director'] for actor in row['cast'].split(',')), axis=1)]

# Exibir diretores que também atuaram
print("Diretores que atuaram como atores:")
print(directors_actors[['director', 'title']])

# 4. Insight adicional: Qual país tem mais produções disponíveis na Netflix?
# Contar a frequência de produções por país
most_common_country = df['country'].value_counts().idxmax()
print(f"O país com mais produções na Netflix é: {most_common_country}")
