#######################################################################################################################

###### VALOR DE LAS VARIABLES POR DEFECTO

Path_to_Folder_With_Input_Files = r'C:\Users\hermoso\Desktop\PDF\Input'

Input_File_Name = '1.1.1. MEMORIA VTO ALHAMA_V02_20220915.pdf\n' \
                  '1.1.2. ANEXOS VTO ALHAMA_V02_20220915\n' \
                  '2.1.1. Definición.pdf\n' \
                  '2.1.2. Acciones.pdf\n' \
                  '2.1.3. Resultados gráficos básicos.pdf\n' \
                  '2.1.4. Secuencia Constructiva.pdf\n' \
                  '2.2. Análisis tensional del tablero para la combinación ELS.pdf\n' \
                  '2.3.1. Esfuerzos en Estado Límite Último (ELU).pdf\n' \
                  '2.3.2.1. Armadura Longitudinal ELU Axil-Flector Cuadro Resumen.pdf\n' \
                  '2.3.2.2. Arm. Long. ELU Axil-Flector Servicio Granular.pdf\n' \
                  '2.3.2.3. Arm. Long. ELU Axil-Flector Servicio Arcilloso.pdf\n' \
                  '2.3.2.4. Arm. Long. ELU Axil-Flector Sismo Granular.pdf\n' \
                  '2.3.2.5. Arm. Long. ELU Axil-Flector Sismo Arcilloso.pdf\n' \
                  '2.3.2.6. Arm. Long. ELU Axil-Flector Sismo Granular Sin Roz.pdf\n' \
                  '2.3.3.1. Armadura Transversal ELU Cortante-Torsor Cuadro Resumen.pdf\n' \
                  '2.3.3.2. Armadura Transversal ELU Cortante-Torsor.pdf\n' \
                  '2.3.4.1. Comprobación ELU Rasante Viga-Losa In-situ Cuadro Resumen.pdf\n' \
                  '2.3.4.2. Comprobación ELU Rasante Viga-Losa In-situ.pdf\n' \
                  '2.3.5.1 Modelo Transversal 2 Vias Alhama.pdf\n' \
                  '2.3.6. Comprobación Viga Riostra.pdf'

Path_to_Folder_Index_File = r'C:\Users\hermoso\Desktop\PDF'

Index_File_Name = 'Viaducto-Alhama_Tablero_Anejo-de-Cálculos_Rev06_APÉNDICE.pdf'

Output_File_Name = 'Viaducto-Alhama_Tablero_Anejo-de-Cálculos_Rev06_APÉNDICE_Merged.pdf'

Page_Where_To_Insert_Input_File = '3, 3, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 22, 23, 25, 26, 27, 28'

#######################################################################################################################

import streamlit as st

st.header("Adjuntar Apéndices a un Documento")

st.subheader("1. Documento a crear")
Output_File_Name_Text_Input = st.text_input("Nombre del documento a crear",value=Output_File_Name)

st.subheader("2. Documento dónde se van a insertar los apéndices")
Index_File_Name_Text_Input = st.text_input("Nombre del documento",value=Index_File_Name)
Path_to_Folder_Index_File_Text_Input = st.text_input("Ruta al documento", value=Path_to_Folder_Index_File)

st.subheader("3. Apéndices")
Input_File_Name_Text_Input = st.text_area("Nombre de los apéndices", height=320, value=Input_File_Name)
Path_to_Folder_With_Input_Files_Text_Input = st.text_input("Ruta a los apéndices", value=Path_to_Folder_With_Input_Files)
Page_Where_To_Insert_Input_File_Text_Input = st.text_input("Número de página dónde insertar los apéndices", value=Page_Where_To_Insert_Input_File)

col1, col2, col3, col4, col5 = st.columns(5) #To place the bottom centered

with col3:
    generate_PDF_button = st.button("Generar PDF", key='Generate_PDF_Button')  

if generate_PDF_button:
    Output_File_Name = Output_File_Name_Text_Input
    print(Output_File_Name)
    print(type(Output_File_Name))
    print('\n')
        
    Index_File_Name = Index_File_Name_Text_Input
    print(Index_File_Name)
    print(type(Index_File_Name))
    print('\n')
    
    Path_to_Folder_With_Input_Files = Path_to_Folder_With_Input_Files_Text_Input
    print(Path_to_Folder_With_Input_Files_Text_Input)
    print(type(Path_to_Folder_With_Input_Files_Text_Input))
    print('\n')

    Input_File_Name = list(Input_File_Name_Text_Input.split("\n"))
    print(Input_File_Name)
    print(type(Input_File_Name))
    print('\n')

    Path_to_Folder_Index_File = Path_to_Folder_Index_File_Text_Input
    print(Path_to_Folder_Index_File)
    print(type(Path_to_Folder_Index_File))
    print('\n')

    Page_Where_To_Insert_Input_File = list(Page_Where_To_Insert_Input_File_Text_Input.split(","))
    Page_Where_To_Insert_Input_File=[int(x) for x in Page_Where_To_Insert_Input_File]

    print(Page_Where_To_Insert_Input_File)
    print(type(Page_Where_To_Insert_Input_File))
    print('\n')
     
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Python script that attaches PDFs to a existing file at specific locations (pages). 
    # The pdfs can be are merged in alphabetical order or like Windows file explorer. 

    # The following variables are used:
    # Path_to_Folder_With_Input_Files --> Path to the folder that contains the files that are going to be attached.  
    # Input_File_Name --> Name of the files that are going to be attached
    # Path_to_Folder_Index_File --> There are two different types of order: 'Windows', 'Alphabetically'
    # Index_File_Name --> Name of the existing file where the input files are going to be inserted
    # Output_File_Name --> File name of the document that is going to be created
    # Page_Where_To_Insert_Input_File --> Page where each input file is going to be inserted
    # Type_of_Order --> There are two different types of order: 'Windows', 'Alphabetically'
    # """""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    import os
    import sys
    import PyPDF2
    from natsort import os_sorted

    # CHECKING INPUT

    if (Index_File_Name.endswith(".pdf") == False):
        Index_File_Name = Index_File_Name + ".pdf"
    else:
        pass

    if (Output_File_Name.endswith(".pdf") == False):
        Output_File_Name = Output_File_Name + ".pdf"
    else:
        pass

    for Input_File_k in range(len(Input_File_Name)):

        if (Input_File_Name[Input_File_k].endswith(".pdf") == False):
            Input_File_Name[Input_File_k] = Input_File_Name[Input_File_k] + ".pdf"
        else:
            pass

    if len(Page_Where_To_Insert_Input_File) != len(Input_File_Name):
        print("The length of the list with 'Input files' does not math the length of the list with pages where to insert the appendix")
        sys.exit()

    # CODE

    pdfDir = Path_to_Folder_With_Input_Files
    Path_To_Index_File = Path_to_Folder_Index_File + '\\' + Index_File_Name
    Path_To_Output_File = Path_to_Folder_Index_File + '\\' + Output_File_Name

    print("Directory with appendixes: %s" % pdfDir)
    print("File to create: %s" % Output_File_Name)

    if (os.path.exists(pdfDir) == False): # Check if path to input files exists.
        print("Input path doesn't exist")
        sys.exit()
    if (os.path.exists(Path_to_Folder_Index_File) == False):  # Check if path to output file exist.
        print("Output path doesn't exist")
        sys.exit()
    if (os.path.isfile(Path_To_Output_File) == True):  # If output file already exists, it will be deleted.
        os.remove(Path_To_Output_File)

    pdfIndex = PyPDF2.PdfFileReader(open(Path_To_Index_File, "rb"))
    Number_Pages_Index_File = pdfIndex.getNumPages()
    if Page_Where_To_Insert_Input_File[0] != 0:
        Page_Where_To_Insert_Input_File.insert(0,0)

    pdfOutput = PyPDF2.PdfFileWriter()

    for Input_File_j in range(len(Input_File_Name)):

        # Adding pdfs to the Index File

        Start = Page_Where_To_Insert_Input_File[Input_File_j]
        End = Page_Where_To_Insert_Input_File[Input_File_j+1]

        while Start < End:
            pdfOutput.addPage(pdfIndex.getPage(Start))
            Start = Start + 1

        # Adding pdfs to the Index File
        print("Adding %s" % Input_File_Name[Input_File_j])
        pdfObj = open(Path_to_Folder_With_Input_Files + '\\' + Input_File_Name[Input_File_j], 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfObj, strict=False)
        numPages = pdfReader.getNumPages()
        for i in range(numPages):
            pdfOutput.addPage(pdfReader.getPage(i))

    if Number_Pages_Index_File != Page_Where_To_Insert_Input_File[len(Page_Where_To_Insert_Input_File) - 1]:
        for i in range(Page_Where_To_Insert_Input_File[len(Page_Where_To_Insert_Input_File)-2]+1,Number_Pages_Index_File,1):
            pdfOutput.addPage(pdfIndex.getPage(i))

    outputStream = open(Path_To_Output_File, 'wb')
    pdfOutput.write(outputStream)
    outputStream.close()

    print("Output pdf has been created")