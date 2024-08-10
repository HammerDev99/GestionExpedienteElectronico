import streamlit as st
import os
import pandas as pd
from index_generator import generate_index_from_scratch
from file_utils import rename_files
from excel_handler import save_excel_file
import base64
import tempfile
from datetime import datetime

# Configuración de Streamlit
st.set_page_config(
    page_title="Sistema de Gestión de Expedientes Electrónicos Judiciales",
    page_icon="📄",
    initial_sidebar_state='expanded',
    menu_items={
        'Get Help': 'https://alexander.oviedo.isabellaea.com/',
        'Report a bug': 'https://github.com/bladealex9848/GestionExpedienteElectronico/issues',
        'About': "El Sistema de Gestión de Expedientes Electrónicos Judiciales es una herramienta para generar índices electrónicos de expedientes judiciales, cumpliendo con los estándares establecidos por el Consejo Superior de la Judicatura."
    }
)

def get_binary_file_downloader_html(url, file_label='File'):
    href = f'<a href="{url}" target="_blank">Descargar {file_label}</a>'
    return href

def main():
    # Sidebar
    try:
        st.sidebar.image("assets/logo.png", width=200)
    except Exception as e:
        st.sidebar.error(f"Error al cargar la imagen del logo: {str(e)}")

    st.sidebar.title("Recursos Adicionales")
    with st.sidebar.expander("Ver Recursos Adicionales", expanded=False):
        st.markdown(get_binary_file_downloader_html("https://github.com/bladealex9848/GestionExpedienteElectronico/blob/main/assets/000IndiceElectronicoC0.xlsm", 'Plantilla Excel'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://github.com/bladealex9848/GestionExpedienteElectronico/blob/main/assets/guia_uso.pdf", 'Guía de Uso'), unsafe_allow_html=True)

    st.sidebar.title("Marco Normativo")
    with st.sidebar.expander("Ver Marco Normativo", expanded=False):
        st.markdown(get_binary_file_downloader_html("https://github.com/bladealex9848/GestionExpedienteElectronico/blob/main/marco_normativo/ACUERDO%20PCSJA20-11567.pdf", 'ACUERDO PCSJA20-11567'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://github.com/bladealex9848/GestionExpedienteElectronico/blob/main/marco_normativo/ACUERDO%20PCSJA23-12094.pdf", 'ACUERDO PCSJA23-12094'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://github.com/bladealex9848/GestionExpedienteElectronico/blob/main/marco_normativo/CIRCULAR%20PCSJC24-23.pdf", 'CIRCULAR PCSJC24-23'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://github.com/bladealex9848/GestionExpedienteElectronico/blob/main/marco_normativo/Plan%20Sectorial%20de%20Desarrollo%20Rama%20Judicial%202023-2026.pdf", 'Plan Sectorial de Desarrollo Rama Judicial 2023-2026'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://github.com/bladealex9848/GestionExpedienteElectronico/blob/main/marco_normativo/Protocolo%20para%20la%20gesti%C3%B3n%20de%20documentos%20electronicos.pdf", 'Protocolo para la gestión de documentos electronicos'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://github.com/bladealex9848/GestionExpedienteElectronico/blob/main/marco_normativo/UTDI_SGDE_ABC_V6.pdf", 'UTDI_SGDE_ABC_V6'), unsafe_allow_html=True)

    st.sidebar.title("Descargar Versiones Portables")
    with st.sidebar.expander("Ver Versiones Portables", expanded=False):
        st.markdown(get_binary_file_downloader_html("https://github.com/bladealex9848/GestionExpedienteElectronico/blob/main/assets/GestionExpedienteElectronico_Windows.zip", 'Versión Portable para Windows'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://github.com/bladealex9848/GestionExpedienteElectronico/blob/main/assets/GestionExpedienteElectronico_Mac.zip", 'Versión Portable para Mac'), unsafe_allow_html=True)
        st.markdown(get_binary_file_downloader_html("https://github.com/bladealex9848/GestionExpedienteElectronico/blob/main/assets/GestionExpedienteElectronico_Linux.zip", 'Versión Portable para Linux'), unsafe_allow_html=True)

    st.sidebar.markdown("---")
    st.sidebar.write("Desarrollado por Alexander Oviedo Fadul")
    st.sidebar.write("Consejo Seccional de la Judicatura de Sucre")
    st.sidebar.write("[GitHub](https://github.com/bladealex9848) | [Website](https://alexander.oviedo.isabellaea.com/) | [LinkedIn](https://www.linkedin.com/in/alexander-oviedo-fadul-49434b9a/)")

    # Main content
    st.title("Sistema de Gestión de Expedientes Electrónicos Judiciales")
    
    st.write("""
    [![ver código fuente](https://img.shields.io/badge/Repositorio%20GitHub-gris?logo=github)](https://github.com/bladealex9848/GestionExpedienteElectronico)
    ![Visitantes](https://api.visitorbadge.io/api/visitors?path=https%3A%2F%2Fgestionexpedienteelectronico.streamlit.app&label=Visitantes&labelColor=%235d5d5d&countColor=%231e7ebf&style=flat)
    """)

    st.write("Esta aplicación permite generar el índice electrónico de expedientes judiciales.")

    uploaded_files = st.file_uploader("Seleccione los archivos que contienen los documentos del expediente:", type=None, accept_multiple_files=True)

    if uploaded_files:
        with tempfile.TemporaryDirectory() as temp_folder:
            original_dates = {}
            for uploaded_file in uploaded_files:
                file_path = os.path.join(temp_folder, uploaded_file.name)
                with open(file_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                # Guardar la fecha original del archivo
                original_dates[uploaded_file.name] = uploaded_file.file_uploader_metadata.get('modification_date', datetime.now())
            
            st.success("Archivos seleccionados correctamente.")
            
            if st.button("Generar Índice Electrónico"):
                progress_bar = st.progress(0)
                try:
                    rename_files(temp_folder)
                    progress_bar.progress(33)
                    
                    df = generate_index_from_scratch(temp_folder, original_dates)
                    if df is None:
                        raise ValueError("La generación del índice falló.")
                    
                    progress_bar.progress(66)
                    
                    index_file_path = os.path.join(temp_folder, "000IndiceElectronicoC0.xlsx")
                    save_excel_file(df, index_file_path, use_template=False)
                    
                    progress_bar.progress(100)
                    st.success("Índice electrónico generado con éxito.")
                    
                    with open(index_file_path, "rb") as f:
                        st.download_button(label='Descargar Índice Electrónico', data=f, file_name=os.path.basename(index_file_path), mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                
                except Exception as e:
                    st.error(f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    main()