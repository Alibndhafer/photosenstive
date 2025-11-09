import streamlit as st
import pandas as pd

# إعداد الصفحة
st.set_page_config(
    page_title="Drug Photosensitivity Checker",
    page_icon="💊",
    layout="centered"
)

# العنوان والوصف
st.title("💊 Drug Photosensitivity Checker")
st.markdown("Check if a drug is photosensitive by entering its name below.")

try:
    # قراءة الملف
    df = pd.read_excel(r"work.xlsx")

    # تنظيف عمود الأدوية
    df["drug"] = df["drug"].astype(str).str.strip()

    # تقسيم الجدول
    oral = df.iloc[0:347]
    inj = df.iloc[350:]

    # إدخال اسم الدواء
    st.header("Check Drug Photosensitivity")
    drug_name = st.text_input(
        "Enter drug name:",
        placeholder="e.g., aspirin, ibuprofen...",
        help="Enter the name of the drug you want to check"
    )

    # زر الفحص
    if st.button("Check Photosensitivity", type="primary"):
        if drug_name.strip() == "":
            st.warning("⚠️ Please enter a drug name")
        else:
            name_lower = drug_name.strip().lower()
            
            # فحص الحساسية للضوء في كلا الجدولين
            is_photosensitive = (
                oral["drug"].str.lower().str.contains(name_lower).any() or
                inj["drug"].str.lower().str.contains(name_lower).any()
            )

            # عرض النتيجة
            st.subheader("Result:")
            if is_photosensitive:
                st.error("🚨 This drug is photosensitive")
                st.info("Photosensitive drugs can cause toxicity or lose their effectiveness when exposed to light.")
            else:
                st.success("✅ This drug isn't photosensitive")
                st.info("This drug is stable under normal light exposure.")

except FileNotFoundError:
    st.error("❌ The file path is incorrect. Please check the Excel file location.")
except KeyError:
    st.error("❌ The uploaded file doesn't contain a 'drug' column. Please check your file format.")
except Exception as e:
    st.error(f"❌ An unexpected error occurred: {str(e)}")

# -----------------------------
# 🧠 Sidebar and links
# -----------------------------
st.sidebar.header("About the Developer")
st.sidebar.info("Developed by Medicosis Illustrators Team.\n\nThis app checks if a drug is photosensitive using a preloaded Excel database.")

st.sidebar.header("📞 Contact")
st.sidebar.link_button("Telegram", "https://t.me/ali4dfr")

st.sidebar.header("📺 Channels")
st.sidebar.link_button("YouTube", "https://www.youtube.com/@Med_ilstr")
st.sidebar.link_button("Telegram Channel", "https://t.me/med_ilstr")
