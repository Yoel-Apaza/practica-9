import streamlit as st
from gestion_libros.libros import Inventario, Libro

def main():
    st.title('Gestión de Inventario de una Librería')

    inventario = Inventario()

    menu = ['Agregar libro', 'Eliminar libro', 'Buscar libro', 'Listar libros', 'Actualizar libro']
    choice = st.sidebar.selectbox('Menú de opciones:', menu)

    if choice == 'Agregar libro':
        st.subheader('Agregar nuevo libro')
        titulo = st.text_input('Título:')
        autor = st.text_input('Autor:')
        anio = st.number_input('Año de publicación:', min_value=0, max_value=9999)
        genero = st.text_input('Género:')
        isbn = st.text_input('ISBN:')
        
        if st.button('Agregar'):
            libro = Libro(titulo, autor, anio, genero, isbn)
            inventario.agregar_libro(libro)
            st.success('Libro agregado correctamente.')

    elif choice == 'Eliminar libro':
        st.subheader('Eliminar libro')
        isbn_eliminar = st.text_input('ISBN del libro a eliminar:')
        
        if st.button('Eliminar'):
            inventario.eliminar_libro(isbn_eliminar)
            st.success('Libro eliminado correctamente.')

    elif choice == 'Buscar libro':
        st.subheader('Buscar libro')
        titulo_buscar = st.text_input('Título del libro a buscar:')
        
        if st.button('Buscar'):
            libro = inventario.buscar_libro(titulo_buscar)
            if libro:
                st.success(f'Libro encontrado: {libro}')
            else:
                st.warning('Libro no encontrado.')

    elif choice == 'Listar libros':
        st.subheader('Listado de libros en el inventario')
        inventario.listar_libros()

    elif choice == 'Actualizar libro':
        st.subheader('Actualizar información de un libro')
        isbn_actualizar = st.text_input('ISBN del libro a actualizar:')
        nuevo_titulo = st.text_input('Nuevo título:')
        nuevo_autor = st.text_input('Nuevo autor:')
        nuevo_anio = st.number_input('Nuevo año de publicación:', min_value=0, max_value=9999)
        nuevo_genero = st.text_input('Nuevo género:')
        
        if st.button('Actualizar'):
            if inventario.actualizar_libro(isbn_actualizar, nuevo_titulo, nuevo_autor, nuevo_anio, nuevo_genero):
                st.success('Libro actualizado correctamente.')
            else:
                st.warning('Libro no encontrado.')

if __name__ == '__main__':
    main()
