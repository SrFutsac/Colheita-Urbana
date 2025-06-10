# README.md - Colheita Urbana

## Introdução

O projeto "Colheita Urbana" visa mitigar o desperdício de alimentos em supermercados, conectando-os a consumidores interessados em adquirir produtos próximos do vencimento a preços reduzidos. Este aplicativo de linha de comando em Python implementa funcionalidades básicas para cadastrar, listar e filtrar esses produtos.

## Funcionalidades

O aplicativo oferece as seguintes funcionalidades:

-   **Adicionar Produto com Desconto:** Permite cadastrar novos produtos com informações como nome, preço original, preço com desconto, data de validade e quantidade disponível.
-   **Listar Produtos com Desconto:** Exibe todos os produtos com desconto atualmente cadastrados.
-   **Filtrar Produtos por Preço Máximo:** Permite aos usuários visualizar produtos com preço de desconto abaixo de um valor especificado.
-   **Listar Produtos Próximos ao Vencimento:** Exibe os produtos cuja data de validade está próxima (definido como até 7 dias por padrão).
-   **Salvar e Carregar Dados:** Os dados dos produtos são persistidos em um arquivo JSON (`produtos_desconto.json`).

## Conceitos de Programação Implementados

-   **Uso de Condicionais (`if`, `else`, `elif`):** Utilizados para controlar o fluxo do programa, como na escolha de opções do menu e na verificação de condições (por exemplo, se há produtos na lista).
-   **Uso de Laços de Repetição (`while`, `for`):** O laço `while` mantém o menu principal em execução até que o usuário escolha sair. O laço `for` é usado para iterar sobre a lista de produtos ao listar e filtrar.
-   **Uso de Funções:** O código é organizado em funções (métodos dentro da classe `ColheitaUrbanaApp`) para realizar tarefas específicas, como `adicionar_produto`, `listar_produtos`, `filtrar_produtos_por_preco`, etc., promovendo a reutilização e organização do código.
-   **Utilização de Estruturas de Dados (`list`, `dict`):** Uma lista (`self.produtos`) é usada para armazenar os objetos da classe `Produto`. Dicionários são utilizados para salvar os dados dos produtos no arquivo JSON.
-   **Tratamento de Erros (`try-except`):** Implementado para lidar com possíveis erros de entrada do usuário (por exemplo, ao converter preços para números) e ao carregar/salvar dados no arquivo JSON. A classe `Produto` também possui tratamento de erros na sua inicialização para garantir a validade dos dados.
-   **Práticas Básicas de Programação Orientada a Objetos:**
    -   **Criação de Classe (`Produto`, `ConectaSupermercadoApp`):** O projeto utiliza duas classes para modelar as entidades principais do sistema: `Produto` (com atributos como nome, preços, data de validade e métodos para calcular desconto e verificar proximidade do vencimento) e `ConectaSupermercadoApp` (que gerencia a lista de produtos e as operações principais do aplicativo).
    -   **Atributos:** As classes possuem atributos para armazenar os dados relevantes (por exemplo, `self.nome`, `self.preco_original` na classe `Produto`).
    -   **Métodos:** As classes contêm métodos que definem o comportamento dos objetos (por exemplo, `calcular_desconto_percentual`, `esta_proximo_vencimento` na classe `Produto`, e `adicionar_produto`, `listar_produtos` na classe `ConectaSupermercadoApp`).

## Como Testar

1.  **Salve o código:** Salve o código Python fornecido em um arquivo chamado `conecta_supermercado.py`.
2.  **Execute o aplicativo:** Abra um terminal ou prompt de comando, navegue até o diretório onde você salvou o arquivo e execute o comando `python conecta_supermercado.py`.
3.  **Siga o menu:** O aplicativo apresentará um menu com várias opções. Siga as instruções para interagir com o aplicativo:
    -   **Adicionar Produto com Desconto (1):** Digite as informações do produto quando solicitado (nome, preço original, preço com desconto, data de validade no formato AAAA-MM-DD e quantidade).
    -   **Listar Produtos com Desconto (2):** Visualize todos os produtos cadastrados.
    -   **Filtrar Produtos por Preço Máximo (3):** Digite um valor máximo para ver os produtos com preço de desconto abaixo desse valor.
    -   **Listar Produtos Próximos ao Vencimento (4):** Veja os produtos que vencem nos próximos 7 dias.
    -   **Sair (5):** Encerra o aplicativo.
4.  **Arquivo de dados:** Os produtos cadastrados serão armazenados no arquivo `produtos_desconto.json` no mesmo diretório onde o script é executado. Você pode abrir este arquivo para verificar como os dados estão sendo salvos.
5.  **Teste de erros:** Tente inserir dados inválidos ao adicionar um produto (por exemplo, formato de data incorreto, preço com desconto maior que o original) para verificar o tratamento de erros.

Este aplicativo fornece uma base para o projeto "Colheita Urbana", demonstrando os conceitos de programação solicitados em um contexto prático de redução do desperdício de alimentos. Em versões futuras, o aplicativo poderia ser expandido com mais funcionalidades, como interface gráfica, integração com geolocalização, sistema de usuários para supermercados, etc.
