import json
import datetime

class Produto:
    """Representa um produto com desconto no supermercado."""
    def __init__(self, nome, preco_original, preco_desconto, data_validade, quantidade):
        self.nome = nome
        try:
            self.preco_original = float(preco_original)
            self.preco_desconto = float(preco_desconto)
            self.data_validade = datetime.datetime.strptime(data_validade, '%Y-%m-%d').date()
            self.quantidade = int(quantidade)
            if self.preco_desconto > self.preco_original or self.preco_original <= 0 or self.preco_desconto < 0 or self.quantidade < 0:
                raise ValueError("Dados do produto inválidos.")
        except ValueError as e:
            raise ValueError(f"Erro ao criar produto: {e}")

    def calcular_desconto_percentual(self):
        """Calcula o percentual de desconto do produto."""
        if self.preco_original > 0:
            return ((self.preco_original - self.preco_desconto) / self.preco_original) * 100
        return 0

    def esta_proximo_vencimento(self, dias=7):
        """Verifica se o produto está próximo da data de validade."""
        hoje = datetime.date.today()
        diferenca = (self.data_validade - hoje).days
        return 0 <= diferenca <= dias

    def __str__(self):
        return f"{self.nome} - Preço Original: R${self.preco_original:.2f}, Preço com Desconto: R${self.preco_desconto:.2f}, Validade: {self.data_validade.strftime('%d/%m/%Y')}, Quantidade: {self.quantidade}"

class ColheitaUrbanaApp:
    def __init__(self, data_file="produtos_desconto.json"):
        self.data_file = data_file
        self.produtos = self.carregar_produtos()

    def carregar_produtos(self):
        """Carrega os produtos com desconto do arquivo JSON."""
        try:
            with open(self.data_file, 'r') as f:
                data = json.load(f)
                produtos_list = []
                for item in data:
                    try:
                        produto = Produto(item['nome'], item['preco_original'], item['preco_desconto'], item['data_validade'], item['quantidade'])
                        produtos_list.append(produto)
                    except ValueError as e:
                        print(f"Erro ao carregar produto '{item.get('nome', 'Desconhecido')}': {e}")
                return produtos_list
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Erro ao decodificar o arquivo de produtos. Iniciando com lista vazia.")
            return []

    def salvar_produtos(self):
        """Salva os produtos com desconto no arquivo JSON."""
        data_list = []
        for produto in self.produtos:
            data_list.append({
                'nome': produto.nome,
                'preco_original': produto.preco_original,
                'preco_desconto': produto.preco_desconto,
                'data_validade': str(produto.data_validade),
                'quantidade': produto.quantidade
            })
        try:
            with open(self.data_file, 'w') as f:
                json.dump(data_list, f, indent=4)
        except IOError:
            print("Erro ao salvar os produtos.")

    def adicionar_produto(self):
        """Adiciona um novo produto com desconto."""
        nome = input("Nome do produto: ")
        preco_original_str = input("Preço original: ")
        data_validade_str = input("Data de validade (AAAA-MM-DD): ")
        quantidade_str = input("Quantidade disponível: ")

        while True:
            tipo_desconto = input("Aplicar desconto por (P) Percentual ou (V) Valor fixo? ").upper()
            if tipo_desconto == 'P':
                try:
                    percentual_desconto = float(input("Digite o percentual de desconto (%): "))
                    preco_original = float(preco_original_str)
                    preco_desconto = preco_original * (1 - (percentual_desconto / 100))
                    produto = Produto(nome, preco_original_str, preco_desconto, data_validade_str, quantidade_str)
                    self.produtos.append(produto)
                    self.salvar_produtos()
                    print(f"Produto '{nome}' adicionado com sucesso!")
                    break
                except ValueError as e:
                    print(f"Erro ao calcular preço com desconto: {e}")
                except Exception as e:
                    print(f"Erro inesperado: {e}")
            elif tipo_desconto == 'V':
                preco_desconto_str = input("Digite o preço com desconto: ")
                try:
                    produto = Produto(nome, preco_original_str, preco_desconto_str, data_validade_str, quantidade_str)
                    self.produtos.append(produto)
                    self.salvar_produtos()
                    print(f"Produto '{nome}' adicionado com sucesso!")
                    break
                except ValueError as e:
                    print(f"Erro ao adicionar produto: {e}")
            else:
                print("Opção inválida. Escolha 'P' para percentual ou 'V' para valor fixo.")

    def listar_produtos(self):
        """Lista todos os produtos com desconto disponíveis."""
        if self.produtos:
            print("\n--- Produtos com Desconto ---")
            for i, produto in enumerate(self.produtos):
                print(f"{i+1}. {produto}")
            print("----------------------------")
        else:
            print("Nenhum produto com desconto disponível no momento.")

    def filtrar_produtos_por_preco(self, preco_maximo):
        """Filtra produtos com preço de desconto abaixo de um valor máximo."""
        produtos_filtrados = [produto for produto in self.produtos if produto.preco_desconto <= preco_maximo]
        if produtos_filtrados:
            print(f"\n--- Produtos com preço até R${preco_maximo:.2f} ---")
            for i, produto in enumerate(produtos_filtrados):
                print(f"{i+1}. {produto}")
            print("--------------------------------------------------")
        else:
            print(f"Nenhum produto encontrado com preço até R${preco_maximo:.2f}.")

    def listar_produtos_proximos_vencimento(self, dias=7):
        """Lista os produtos que estão próximos da data de validade."""
        produtos_proximos = [produto for produto in self.produtos if produto.esta_proximo_vencimento(dias)]
        if produtos_proximos:
            print(f"\n--- Produtos Próximos ao Vencimento (até {dias} dias) ---")
            for i, produto in enumerate(produtos_proximos):
                print(f"{i+1}. {produto}")
            print("------------------------------------------------------------")
        else:
            print(f"Nenhum produto próximo ao vencimento nos próximos {dias} dias.")

def main():
    app = ColheitaUrbanaApp()

    while True:
        print("\n--- Colheita Urbana ---")
        print("1. Adicionar Produto com Desconto")
        print("2. Listar Produtos com Desconto")
        print("3. Filtrar Produtos por Preço Máximo")
        print("4. Listar Produtos Próximos ao Vencimento")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            app.adicionar_produto()
        elif escolha == '2':
            app.listar_produtos()
        elif escolha == '3':
            try:
                preco_max = float(input("Digite o preço máximo desejado: "))
                app.filtrar_produtos_por_preco(preco_max)
            except ValueError:
                print("Entrada inválida para o preço.")
        elif escolha == '4':
            app.listar_produtos_proximos_vencimento()
        elif escolha == '5':
            print("Obrigado por usar o Colheita Urbana!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    main()
