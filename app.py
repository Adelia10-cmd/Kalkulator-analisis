import streamlit as st

st.set_page_config(
    page_title="Kalkulator Analisis Kimia",
    layout="centered"
)

st.title("Kalkulator Analisis Kimia")
st.caption("Aplikasi perhitungan analisis kimia")

parameter = st.selectbox(
    "Pilih Parameter Analisis",
    [
        "FFA sebagai Palmitat",
        "FFA sebagai Laurat",
        "Bilangan Asam",
        "Bilangan Iodium",
        "Bilangan Penyabunan",
        "Kadar Gliserol Total",
        "Kadar Air",
        "Kadar Pengotor",
        "Kadar Abu",
        "Bilangan Peroksida"
    ]
)

st.divider()

# ================= FFA PALMITAT =================
if parameter == "FFA sebagai Palmitat":
    W = st.number_input("Bobot Sampel (g)", min_value=0.0, format="%.4f")
    V = st.number_input("Volume Titran (mL)", min_value=0.0, format="%.3f")
    N = st.number_input("Normalitas KOH/NaOH (N)", min_value=0.0, format="%.4f")

    if st.button("Hitung FFA Palmitat"):
        if W > 0:
            hasil = (V * N * 25.6) / W
            st.success(f"FFA sebagai Palmitat = {hasil:.3f} %")
        else:
            st.error("Bobot sampel tidak boleh 0")

# ================= FFA LAURAT =================
elif parameter == "FFA sebagai Laurat":
    W = st.number_input("Bobot Sampel (g)", min_value=0.0, format="%.4f")
    V = st.number_input("Volume Titran (mL)", min_value=0.0, format="%.3f")
    N = st.number_input("Normalitas KOH/NaOH (N)", min_value=0.0, format="%.4f")

    if st.button("Hitung FFA Laurat"):
        if W > 0:
            hasil = (V * N * 20.0) / W
            st.success(f"FFA sebagai Laurat = {hasil:.3f} %")
        else:
            st.error("Bobot sampel tidak boleh 0")

# ================= BILANGAN ASAM =================
elif parameter == "Bilangan Asam":
    W = st.number_input("Bobot Sampel (g)", min_value=0.0, format="%.4f")
    V = st.number_input("Volume Titran (mL)", min_value=0.0, format="%.3f")
    N = st.number_input("Normalitas KOH (N)", min_value=0.0, format="%.4f")

    if st.button("Hitung Bilangan Asam"):
        if W > 0:
            hasil = (V * N * 56.1) / W
            st.success(f"Bilangan Asam = {hasil:.2f} mg KOH/g")
        else:
            st.error("Bobot sampel tidak boleh 0")

# ================= BILANGAN IODIUM =================
elif parameter == "Bilangan Iodium":
    W = st.number_input("Bobot Sampel (g)", min_value=0.0, format="%.4f")
    B = st.number_input("Volume Blanko (mL)", min_value=0.0, format="%.3f")
    S = st.number_input("Volume Sampel (mL)", min_value=0.0, format="%.3f")
    N = st.number_input("Normalitas Na2S2O3 (N)", min_value=0.0, format="%.4f")

    if st.button("Hitung Bilangan Iodium"):
        if W > 0:
            hasil = ((B - S) * N * 12.69) / W
            st.success(f"Bilangan Iodium = {hasil:.2f}")
        else:
            st.error("Bobot sampel tidak boleh 0")

# ================= BILANGAN PENYABUNAN =================
elif parameter == "Bilangan Penyabunan":
    W = st.number_input("Bobot Sampel (g)", min_value=0.0, format="%.4f")
    B = st.number_input("Volume Blanko (mL)", min_value=0.0, format="%.3f")
    S = st.number_input("Volume Sampel (mL)", min_value=0.0, format="%.3f")
    N = st.number_input("Normalitas HCl (N)", min_value=0.0, format="%.4f")

    if st.button("Hitung Bilangan Penyabunan"):
        if W > 0:
            hasil = ((B - S) * N * 56.1) / W
            st.success(f"Bilangan Penyabunan = {hasil:.2f} mg KOH/g")
        else:
            st.error("Bobot sampel tidak boleh 0")

# ================= GLISEROL TOTAL =================
elif parameter == "Kadar Gliserol Total":
    W = st.number_input("Bobot Sampel (g)", min_value=0.0, format="%.4f")
    Vs = st.number_input("Volume Sampel (mL)", min_value=0.0, format="%.3f")
    Vb = st.number_input("Volume Blanko (mL)", min_value=0.0, format="%.3f")
    N = st.number_input("Normalitas (N)", min_value=0.0, format="%.4f")

    if st.button("Hitung Gliserol Total"):
        if W > 0:
            hasil = ((Vb - Vs) * N * 2.302) / W
            st.success(f"Kadar Gliserol Total = {hasil:.2f} %")
        else:
            st.error("Bobot sampel tidak boleh 0")

# ================= KADAR AIR =================
elif parameter == "Kadar Air":
    W1 = st.number_input("Bobot Sampel (g)", min_value=0.0, format="%.4f")
    W2 = st.number_input("Bobot Sampel + Wadah Awal (g)", min_value=0.0, format="%.4f")
    W3 = st.number_input("Bobot Sampel + Wadah Akhir (g)", min_value=0.0, format="%.4f")

    if st.button("Hitung Kadar Air"):
        if W1 > 0:
            hasil = ((W2 - W3) / W1) * 100
            st.success(f"Kadar Air = {hasil:.2f} %")
        else:
            st.error("Bobot sampel tidak boleh 0")

# ================= KADAR PENGOTOR =================
elif parameter == "Kadar Pengotor":
    Wsk = st.number_input("Bobot Sampel + Kertas Saring (g)", min_value=0.0, format="%.4f")
    Ws = st.number_input("Bobot Sampel (g)", min_value=0.0, format="%.4f")
    Wk = st.number_input("Bobot Kertas Saring (g)", min_value=0.0, format="%.4f")

    if st.button("Hitung Kadar Pengotor"):
        if Ws > 0:
            hasil = ((Wsk - Wk) / Ws) * 100
            st.success(f"Kadar Pengotor = {hasil:.2f} %")
        else:
            st.error("Bobot sampel tidak boleh 0")

# ================= KADAR ABU =================
elif parameter == "Kadar Abu":
    Wa = st.number_input("Bobot Cawan Kosong (g)", min_value=0.0, format="%.4f")
    Ws = st.number_input("Bobot Sampel (g)", min_value=0.0, format="%.4f")
    Wak = st.number_input("Bobot Sampel + Cawan Akhir (g)", min_value=0.0, format="%.4f")

    if st.button("Hitung Kadar Abu"):
        if Ws > 0:
            hasil = ((Wak - Wa) / Ws) * 100
            st.success(f"Kadar Abu = {hasil:.2f} %")
        else:
            st.error("Bobot sampel tidak boleh 0")

# ================= BILANGAN PEROKSIDA =================
elif parameter == "Bilangan Peroksida":
    W = st.number_input("Bobot Sampel (g)", min_value=0.0, format="%.4f")
    B = st.number_input("Volume Blanko (mL)", min_value=0.0, format="%.3f")
    S = st.number_input("Volume Sampel (mL)", min_value=0.0, format="%.3f")
    N = st.number_input("Normalitas Na2S2O3 (N)", min_value=0.0, format="%.4f")

    if st.button("Hitung Bilangan Peroksida"):
        if W > 0:
            hasil = ((B - S) * N * 1000) / W
            st.success(f"Bilangan Peroksida = {hasil:.2f} meq O2/kg")
        else:
            st.error("Bobot sampel tidak boleh 0")
