import streamlit as st

class Libro:
    def __init__(self, titulo, autor, anio, genero, isbn):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo}, {self.autor}, {self.anio}, {self.genero}, ISBN: {self.isbn}"

class Inventario:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, isbn):
        self.libros = [libro for libro in self.libros if libro.isbn != isbn]

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def listar_libros(self):
        if not self.libros:
            st.warning("No hay libros en el inventario.")
        else:
            for libro in self.libros:
                st.write(libro)

    def actualizar_libro(self, isbn, nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_genero):
        for libro in self.libros:
            if libro.isbn == isbn:
                libro.titulo = nuevo_titulo
                libro.autor = nuevo_autor
                libro.anio = nuevo_anio
                libro.genero = nuevo_genero
                return True
        return False
