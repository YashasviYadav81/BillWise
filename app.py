import pandas as pd

from modules.data_processor import extract_invoice_data

from modules.file_handler import extract_text_from_pdf
import streamlit as st

st.set_page_config(
    page_title="BillWise",
    page_icon="📊",
    layout="wide"
)

st.title("BillWise")
st.subheader("Smart Invoice and Receipt Management System")

st.write("Upload and analyse your invoices automatically.")

st.divider()

st.header("Upload Invoice")

st.header("Upload Invoice")

uploaded_file = st.file_uploader(
    "Choose an invoice",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    st.success("File uploaded successfully!")

    if uploaded_file.type == "application/pdf":

        extracted_text = extract_text_from_pdf(uploaded_file)

        invoice_data=extract_invoice_data(extracted_text)

        df=pd.DataFrame([invoice_data])
        st.subheader("Invoice Data Table")
        st.dataframe(df)

        st.subheader("Invoice Summary")
        st.write("Total Invoice Amount:", df["Total"].sum())

        st.write("Average Invoice Amount:", df["Total"].mean())

        st.write("Highest Invoice Amount:", df["Total"].max())

        st.write("Lowest Invoice Amount:", df["Total"].min())

        st.subheader("Extracted Invoice Information")
        st.json(invoice_data)

        st.subheader("Extracted Invoice Text")

        st.text_area(
            "Invoice Contents",
            extracted_text,
            height=300
        )

    else:
        st.info("Image extraction will be implemented next.")