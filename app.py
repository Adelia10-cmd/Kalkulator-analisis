import streamlit as st

st.set_page_config(
    page_title="Kalkulator Analisis Kimia",
    layout="centered"
)

st.title("Kalkulator Analisis Kimia")

parameter = st.selectbox(
    "Pilih Parameter Analisis",
    [
        "Kadar Asam Lemak Bebas (FFA)",
        "Bilangan Iodium"
    ]
)

st.write("---")

# ===================== FFA =====================
if parameter == "Kadar Asam Lemak Bebas (FFA)":

    bobot = st.number_input("Bobot Sampel (g)", min_value=0.0)
    normalitas = st.number_input("Normalitas NaOH/KOH (N)", min_value=0.0)
    volume = st.number_input("Volume Titran (mL)", min_value=0.0)

    if st.button("Hitung FFA"):
        if bobot > 0:
            ffa = (volume * normalitas * 28.2) / bobot
            st.success(f"Hasil Kadar Asam Lemak Bebas: {ffa:.2f} %")
        else:
            st.error("Bobot sampel tidak boleh 0")

# ================= BILANGAN IODIUM =================
elif parameter == "Bilangan Iodium":

    bobot = st.number_input("Bobot Sampel (g)", min_value=0.0)
    blanko = st.number_input("Volume Blanko (mL)", min_value=0.0)
    sampel = st.number_input("Volume Sampel (mL)", min_value=0.0)
    normalitas = st.number_input("Normalitas Na2S2O3 (N)", min_value=0.0)

    if st.button("Hitung Bilangan Iodium"):
        if bobot > 0:
            iv = ((blanko - sampel) * normalitas * 12.69) / bobot
            st.success(f"Hasil Bilangan Iodium: {iv:.2f}")
        else:
            st.error("Bobot sampel tidak boleh 0")
