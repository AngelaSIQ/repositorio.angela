class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionarLivro(self, livro):
        self.livros.append(livro)

    def removerLivro(self, titulo):
        for livro in self.livros:
            if livro.get_titulo() == titulo:
                self.livros.remove(livro)
                return True
        return False

    def buscarLivro(self, titulo):
        for livro in self.livros:
            if livro.get_titulo() == titulo:
                return livro
        return None

    def listarLivros(self):
        if not self.livros:
            return "Nenhum livro disponível."
        return "\n".join([f"Título: {livro.get_titulo()}, Autor: {livro.get_autor().get_nome()}, Ano de Publicação: {livro.get_anoPublicacao()}" for livro in self.livros])
