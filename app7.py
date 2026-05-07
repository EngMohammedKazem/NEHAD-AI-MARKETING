import streamlit as st
import pandas as pd
import random
import time
import plotly.graph_objects as go
import os  # مكتبة للتعامل مع ملفات النظام

# 1. إعداد واجهة المستخدم (Premium UI)
st.set_page_config(page_title="REHAM AI - LOCAL PRO", layout="wide")

st.markdown("""
    <style>
    .stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); color: #fff; }
    .ad-box { background-color: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 15px; border-left: 5px solid #FFD700; }
    </style>
    """, unsafe_allow_html=True)

# 2. تعريف بيانات المنتجات والملفات المرتبطة بها
# ملاحظة: تأكد من تسمية الصور في مجلدك بنفس هذه الأسماء بالضبط
products_data = {
    "طاقة شمسية": {
        "image_file": "solar.png",  # اسم الصورة في مجلدك
        "audience": "عامة الناس / أصحاب المنازل",
        "verbs": ["نور بيتك بـ", "وفر كهربتك مع", "استثمر في المستقبل مع"],
        "desc": "طاقة نظيفة ومستدامة توفر عليك الكثير."
    },
    "ملابس": {
        "image_file": "clothes.png", # اسم الصورة في مجلدك
        "audience": "عامة الناس / محبي الأناقة",
        "verbs": ["تألق بأحدث", "جدد مظهرك بـ", "اكتشف روعة"],
        "desc": "أرقى الموديلات بجودة عالمية وسعر منافس."
    }
}

# 3. القائمة الجانبية
with st.sidebar:
    st.title("💎 REHAM LOCAL")
    app_mode = st.selectbox("المهمة:", ["🚀 مولد الحملات المحلية", "📊 رادار السوق"])

# --- المرحلة الأولى: مولد الحملات ---
if app_mode == "🚀 مولد الحملات المحلية":
    st.title("🚀 صناعة الحملات بالصور المحلية")
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        product_choice = st.selectbox("اختر المنتج من المجلد:", ["طاقة شمسية", "ملابس"])
        product_name = st.text_input("📦 اسم المنتج الدقيق", f"{product_choice} فاخرة")
        generate_btn = st.button("عرض المنتج وتوليد الحملة")

    with col2:
        if generate_btn:
            img_path = products_data[product_choice]["image_file"]
            
            # التحقق إذا كان الملف موجود فعلاً في المجلد لتجنب الخطأ
            if os.path.exists(img_path):
                st.image(img_path, caption=f"معاينة منتج: {product_choice}", use_container_width=True)
            else:
                st.error(f"⚠️ لم يتم العثور على ملف {img_path} في المجلد. تأكد من وضعه بجانب الكود.")

    if generate_btn:
        st.divider()
        with st.status("🔮 جاري الربط بين الصورة والنص التسويقي...", expanded=False):
            time.sleep(1)
        
        # توليد النص بناءً على البيانات المحلية
        v = random.choice(products_data[product_choice]["verbs"])
        ad_text = f"🔥 **{v} {product_name}**! \n\n {products_data[product_choice]['desc']} موجهة خصيصاً لـ **{products_data[product_choice]['audience']}**. اطلبها الآن!"
        
        st.markdown(f"<div class='ad-box'>{ad_text}</div>", unsafe_allow_html=True)
        st.success("✅ تم استدعاء البيانات والصورة بنجاح من جهازك.")

# --- المرحلة الثانية: رادار السوق ---
elif app_mode == "📊 رادار السوق":
    st.header("📊 رادار تحليل السوق")
    df = pd.DataFrame({'القطاع': ['طاقة شمسية', 'ملابس'], 'الطلب': [88, 95]})
    fig = go.Figure(go.Bar(x=df['القطاع'], y=df['الطلب'], marker_color='#FFD700'))
    fig.update_layout(template="plotly_dark")
    st.plotly_chart(fig, use_container_width=True)

st.divider()
st.caption("نظام REHAM AI LOCAL - يعتمد على الموارد المحلية لمشروعك")
