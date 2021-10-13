# malaria-cell-detector
Detecção do parasita da malaria em imagens de esfregaço de sangue

# Dataset
https://www.kaggle.com/iarunava/cell-images-for-detecting-malaria

# Images
As imagens dentro do diretório `images` são uma amostra do dataset, balanceadas com a mesma tonalidade.
Para evitar problemas com o treshold

# Dependencias

Nesse projeto é utilizado a implementação do opencv para python.  
Então é necessário ter ela instalada na máquina.  
[Clique aqui para: Como instalar o opencv](https://pypi.org/project/opencv-python/)

# Como executar

Para rodar os testes execute na raiz:
`python test.py`

# Estrutura do projeto

```bash
├── images // As imagens utilizadas nos testes
├── pipeline_segmentation.py // Arquivo com a sequencia de algoritmos para segmentação
├── test.py // Arquivo que chama os testes
└── utils.py // Arquivo com funções utilitarias
```