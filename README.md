## Projeto de Algoritimos(BASE)


###	:building_construction:	:building_construction: UNDER CONSTRUCTION

<h2>:compass: Contexto</h2>
<p>A ideia destre projeto é desenvolver em python uma solução para o TSP-Visinho, mais conhecido como problema do caixeiro viajante.</p>

<h2>:books: Bibliotecas Utilizadas</h2>
<p>As bibiliotecas utilizadas foram:</p>
  <ul>haversine: Biblioteca utilizada para realizar o calculo de distancias para orientações longitudinais em um globo</ul>
  <ul>pandas: utilizado para realizar a leitura do arquivo de dados csv</ul>
  <ul>basemap: uma extensão utilizada em conjunto com o metablot para gerar os graficos</ul>
  <ul>matplotlib: biblioteca de geração de graficos</ul>



<h2>:rocket: Como rodar</h2>
1. Clone the repository and navigate to the downloaded folder.
   
   ```bash
    git clone https://github.com/evilhalba/projeto-algoritmos.git
    cd projeto-algoritimos-main
    ```

2. Install required packages:
	```bash
	pip install -e .
	```
    Or:
	```bash
	pip install -e . --user
	```

3. Navigate to the src folder and execute:
    ```bash
    cd src
    python3 main.py -v 1 --pop_size 500 --tourn_size 50 --mut_rate 0.02 --n_gen 20 --cities_fn '../data/places.csv'
    ```