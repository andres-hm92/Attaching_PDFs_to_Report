import sys
import streamlit.web.cli as stcli

if __name__ == '__main__':
    sys.argv = ["streamlit", "run", "Attaching_PDFs_to_Report_Rev1_Streamlit.py"]
    sys.exit(stcli.main())
