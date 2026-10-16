import streamlit as st
from google import genai

# Cấu hình giao diện trang web
st.set_page_config(
    page_title="AI Copywriter",
    page_icon="🚀",
    layout="centered"
)
# --- ẨN GIAO DIỆN MẶC ĐỊNH CỦA STREAMLIT ---
st.markdown("""
    <style>
    /* Ẩn menu Hamburger góc trên bên phải */
    #MainMenu {visibility: hidden;}
    /* Ẩn thanh header chứa nút Deploy trắng phía trên */
    header {visibility: hidden;}
    /* Ẩn dòng chữ Made with Streamlit ở dưới cùng */
    footer {visibility: hidden;}
    
    /* (Tùy chọn) Bo góc và tạo bóng cho form nhập liệu nhìn xịn hơn */
    div[data-testid="stForm"] {
        background-color: #ffffff;
        box-shadow: 0px 8px 16px rgba(0,0,0,0.05);
        border: none;
        border-radius: 12px;
        padding: 20px;
    }
    </style>
""", unsafe_allow_html=True)
# --- HỆ THỐNG ĐĂNG NHẬP (TÊN ĐĂNG NHẬP + MẬT KHẨU) ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔒 Cổng đăng nhập AI Copywriter")
    st.write("Vui lòng đăng nhập để sử dụng hệ thống.")
    
    # Tạo 2 ô nhập liệu
    ten_dang_nhap = st.text_input("Tên đăng nhập:")
    mat_khau_nhap = st.text_input("Mật khẩu:", type="password")
    
    if st.button("Đăng nhập"):
        # Lấy danh sách tài khoản từ file secrets
        danh_sach_tai_khoan = st.secrets["credentials"]
        
        # Kiểm tra: Tên đăng nhập có tồn tại KHÔNG? VÀ Mật khẩu có khớp KHÔNG?
        if ten_dang_nhap in danh_sach_tai_khoan and danh_sach_tai_khoan[ten_dang_nhap] == mat_khau_nhap:
            st.session_state.logged_in = True
            st.session_state.user = ten_dang_nhap  # Lưu tên user lại để dùng về sau
            st.rerun()  # Tải lại trang để vào hệ thống
        else:
            st.error("❌ Tên đăng nhập hoặc mật khẩu không chính xác!")
    
    st.stop()  # Chặn toàn bộ code phía dưới nếu chưa đăng nhập thành công
# ------------------------------------------------------
st.title("🚀 AI Copywriter")
st.write("Tạo bài viết Marketing chốt sale cực bén bằng AI")

# 1. Cấu hình API (Bảo mật tuyệt đối qua secrets.toml)
try:
    client = genai.Client(api_key=st.secrets["GMIAPI"])
except KeyError:
    st.error("⚠️ Không tìm thấy khóa GMIAPI trong file .streamlit/secrets.toml!")
    st.stop()

# 2. Xây dựng Form nhập liệu (Giúp web không bị tải lại liên tục khi gõ)
with st.form("form_tao_bai_viet"):
    st.subheader("📦 Thông tin sản phẩm")
    
    ten_sp = st.text_input("Tên sản phẩm *", placeholder="Ví dụ: Giày thể thao nam siêu nhẹ")
    tinh_nang = st.text_area("Đặc điểm nổi bật *", placeholder="Ví dụ: Chống nước, êm chân, bám đường tốt")
    
    col1, col2 = st.columns(2)
    with col1:
        khuyen_mai = st.text_input("Khuyến mãi", placeholder="Ví dụ: Giảm 20%, Freeship")
    with col2:
        khach_hang = st.text_input("Khách hàng mục tiêu", placeholder="Ví dụ: Sinh viên, người đi làm")

    st.subheader("✍️ Tùy chỉnh bài viết")
    
    col3, col4 = st.columns(2)
    with col3:
        phong_cach = st.selectbox(
            "Phong cách viết",
            ["Chuyên nghiệp, thuyết phục", "Trẻ trung, Gen Z", "Thân thiện, gần gũi", "Sang trọng, cao cấp", "Bán hàng mạnh mẽ"]
        )
    with col4:
        so_tu = st.slider(
            "Số từ mong muốn", 
            min_value=50,   # Ít nhất 50 từ
            max_value=500,  # Dài nhất 500 từ
            value=150,      # Mặc định để ở mức 150 từ
            step=10         # Mỗi lần kéo tăng/giảm 10 từ
        )

    # Nút bấm tạo nội dung
    submitted = st.form_submit_button("🔥 Tạo bài viết", type="primary")

# 3. Xử lý Tạo nội dung khi người dùng bấm nút
if submitted:
    if not ten_sp.strip() or not tinh_nang.strip():
        st.warning("⚠️ Vui lòng nhập Tên sản phẩm và Đặc điểm nổi bật!")
    else:
        # Prompt mới: Cân bằng hoàn hảo giữa cảm xúc chốt sale và sự trung thực
        prompt = f"""
        Bạn là một chuyên gia Copywriter thực chiến trên Facebook. Bạn viết văn rất cuốn hút, năng động, biết cách đẩy cảm xúc khách hàng lên cao để chốt sale, nhưng bạn LÀM VIỆC NGHIÊM NGẶT DỰA TRÊN SỰ THẬT.

        THÔNG TIN SẢN PHẨM (TUYỆT ĐỐI CHỈ DÙNG DỮ LIỆU NÀY, KHÔNG TỰ BỊA THÊM):
        - Tên sản phẩm: {ten_sp}
        - Đặc điểm nổi bật: {tinh_nang}
        - Khuyến mãi: {khuyen_mai or "Không có"}
        - Khách hàng mục tiêu: {khach_hang or "Khách hàng phổ thông"}
        - Phong cách: {phong_cach}
        - Độ dài: Xấp xỉ {so_tu} từ.

        YÊU CẦU DÀNH CHO BẠN:
        1. Văn phong "Cháy" & Bắt mắt: Tự do sử dụng emoji (vừa đủ để đẹp mắt), viết in hoa các TỪ KHÓA quan trọng để tạo điểm nhấn thị giác. Hook mở đầu phải thật ấn tượng và đánh trúng tâm lý.
        2. Biến tính năng thành sự khao khát: Tập trung miêu tả cảm giác sung sướng, thoải mái hoặc lợi ích tuyệt vời mà khách hàng có được khi trải nghiệm các "Đặc điểm nổi bật" trên.
        3. Ranh giới sự thật (CẤM VI PHẠM): 
           - TUYỆT ĐỐI KHÔNG tự phát minh ra các tính năng, thông số, hoặc chất liệu không được cung cấp.
           - TUYỆT ĐỐI KHÔNG tự bịa ra sự khan hiếm giả (như "chỉ còn 49 suất", "duy nhất hôm nay") hay quà tặng kèm nếu phần "Khuyến mãi" không ghi.
           - KHÔNG đưa ra các tuyên bố chữa bệnh y tế nếu không có căn cứ.
        4. Kêu gọi hành động (CTA) thôi thúc: Cuối bài, dùng ngôn từ mạnh mẽ thúc giục khách hàng "Nhắn tin (Inbox) cho shop" ngay để chốt {khuyen_mai or "đơn hàng"}.

        CHỈ TRẢ VỀ KẾT QUẢ LÀ BÀI VIẾT HOÀN CHỈNH, KHÔNG GIẢI THÍCH.
        """

        with st.spinner("🤖 AI đang dồn chất xám viết bài..."):
            try:
                # Đang sử dụng bản Flash để đảm bảo tốc độ nhanh và không bị giới hạn quota
                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=prompt
                )

                if response.text:
                    st.success("✅ Đã tạo bài viết thành công!")
                    # --- ĐOẠN CODE GHI LỊCH SỬ THÊM VÀO Ở ĐÂY ---
                    import datetime
                    with open("lich_su.txt", "a", encoding="utf-8") as f:
                        f.write(f"{datetime.datetime.now()} | User: {st.session_state.user} | Sản phẩm: {ten_sp}\n")
                    # -------------------------------------------
                    st.subheader("📝 Bài viết của bạn")
                    st.text_area("Chỉnh sửa (nếu cần) và Copy để đăng ngay:", value=response.text, height=450)
                else:
                    st.error("❌ AI không trả về nội dung.")

            except Exception as e:
                st.error(f"⚠️ Không thể tạo bài viết. Lỗi chi tiết: {e}")