from autor import Autor
from livro import Livro
from biblioteca import Biblioteca

def menu():
    print("\nBiblioteca menu:")
    print("1. colocar Livro")
    print("2. tirar Livro")
    print("3. procurar Livro")
    print("4. Listar Livros")
    print("5. Sair")

def main():
    biblioteca = Biblioteca()

    while True:
        menu()
        opcao = input("digite uma opção: ")

        if opcao == "1":
            titulo = input("Título do livro: ")
            nome_autor = input("Nome do autor: ")
            nacionalidade_autor = input("Nacionalidade do autor: ")
            data_nascimento_autor = input("Data de nascimento do autor: ")
            ano_publicacao = int(input("Ano de publicação: "))
            
            autor = Autor(nome_autor, nacionalidade_autor, data_nascimento_autor)
            livro = Livro(titulo, autor, ano_publicacao)
            biblioteca.adicionarLivro(livro)
            print("Livro adicionado com sucesso!")

        elif opcao == "2":
            titulo = input("Título do livro a remover: ")
            if biblioteca.removerLivro(titulo):
                print("Livro removido com sucesso!")
            else:
                print("Livro não encontrado.")

        elif opcao == "3":
            titulo = input("Título do livro a buscar: ")
            livro = biblioteca.buscarLivro(titulo)
            if livro:
                autor = livro.get_autor()
                print(f"\nTítulo: {livro.get_titulo()}")
                print(f"Autor: {autor.get_nome()}")
                print(f"Nacionalidade do Autor: {autor.get_nacionalidade()}")
                print(f"Data de Nascimento do Autor: {autor.get_dataNascimento()}")
                print(f"Ano de Publicação: {livro.get_anoPublicacao()}")
            else:
                print("Livro não encontrado.")

        elif opcao == "4":
            print(biblioteca.listarLivros())

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
