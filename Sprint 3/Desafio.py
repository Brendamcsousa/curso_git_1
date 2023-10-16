# Criando os 5 arquivos vazios
for i in range(1, 6):
    file_path = 'Sprint 3/etapa-' + str(i) + '.txt'
    with open(file_path, 'w') as file:
        pass

# Função para ler o arquivo actors.csv e retornar uma matriz de dados
def ler_arquivo_csv():
    data = []
    with open('C:\\Users\\Caio.Sousa\\Brenda\\1_primeiro_repo\\Sprint 3\\actors.csv', 'r') as file:
        lines = file.readlines()
        headers = lines[0].strip().split(',')
        
        for line in lines[1:]:
            values = []
            parts = line.strip().split(',')
            value = ""
            in_quoted_field = False

            for part in parts:
                if in_quoted_field:
                    value += ',' + part
                    if part.endswith('"'):
                        in_quoted_field = False
                        values.append(value[1:-1])  # Remove enclosing double quotes
                elif part.startswith('"'):
                    in_quoted_field = True
                    value = part
                else:
                    values.append(part)

            data.append(dict(zip(headers, values)))
    
    return data



# Resposta à Pergunta 1
data = ler_arquivo_csv()
filtered_data = [x for x in data if x['Number of Movies'].isdigit()]
max_movies_actor = max(filtered_data, key=lambda x: int(x['Number of Movies']))
# print(filtered_data)
with open('Sprint 3/etapa-1.txt', 'w') as file:
    file.write(f'"{max_movies_actor["Actor"]}" - {max_movies_actor["Number of Movies"]}')

# Resposta à Pergunta 2
total_gross = [float(row['Gross']) for row in data if row['Gross'].replace('.', '', 1).isdigit()]
average_gross = sum(total_gross) / len(total_gross)
with open('Sprint 3/etapa-2.txt', 'w') as file:
    file.write(f'{average_gross:.2f}')

# Resposta à Pergunta 3
max_average_gross_actor = max(data, key=lambda x: float(x['Average per Movie']))
with open('Sprint 3/etapa-3.txt', 'w') as file:
    file.write(f'{max_average_gross_actor["Actor"]} - {float(max_average_gross_actor["Average per Movie"]):.2f}')

# Resposta à Pergunta 4
from collections import Counter
movie_counts = Counter(row['#1 Movie'] for row in data)
sorted_movies = sorted(movie_counts.items(), key=lambda x: (-x[1], x[0]))
with open('Sprint 3/etapa-4.txt', 'w') as file:
    for movie, count in sorted_movies:
        file.write(f'{movie} - O filme {movie} aparece {count} vez(es) no dataset\n')

# Resposta à Pergunta 5    
def parse_total_gross(value):
    try:
        value = value.replace('$', '').replace(',', '').strip()
        return float(value)
    except ValueError:
        return 0.0

data = ler_arquivo_csv()

# Sort the data by total gross earnings in descending order
actors_sorted_by_gross = sorted(data, key=lambda x: parse_total_gross(x['Total Gross']), reverse=True)
with open('Sprint 3/etapa-5.txt', 'w') as file:
    for actor in actors_sorted_by_gross:
        actor_name = actor['Actor'].strip('"')
        gross = parse_total_gross(actor["Total Gross"])
        file.write(f'"{actor_name}" - {gross:.2f}\n')




