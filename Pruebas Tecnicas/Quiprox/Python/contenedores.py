import sys 


def organize_balls(q, queries):
    # necesito cajas y bolas en caja
    for query in queries:
        # cuente cuantas cajas y cuente bolas en caja: ¿Como lo hago??
        n, M = query[0], query[1:]

        # Necesito saber cuantas bolas hay en cada caja
        cont_cap = [sum(container) for container in M] # suma de bolas en cada contenedor

        # de que tipo es cada bola? cuantas?
        type_count = []

        # Iteramos sobre los indices de las bolas del mismo tipo en cada contenedor
        for i in range(len(M[0])):
            # Inicializamos la suma para el tipo actual
            total_balls_of_type = 0

            # Iteramos sobre los contenedores
            for container in M:
                # Sumamos las bolas del mismo tipo en el contenedor actual
                total_balls_of_type += container[i]

            # Agregamos el total a type_count
            type_count.append(total_balls_of_type)
        
        # recomendacion de chat gpt: type_count = [sum(x) for x in zip(*M)]; es lo mismo pero en una sola linea

        # Verifica set igual
        if set(type_count) == set(cont_cap):
            print('Possible')
        else:
            print('Impossible')

if __name__ == "__main__":
    q = int(input().strip())
    queries = []

    # Para cada consulta
    for _ in range(q):
        n = int(input().strip())
        M = [list(map(int, input().strip().split())) for _ in range(n)]
        queries.append([n] + M)

    # deberia d fncionar
    organize_balls(q, queries)