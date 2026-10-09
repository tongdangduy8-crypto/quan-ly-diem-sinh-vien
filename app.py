import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cấu hình trang web
st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="📚",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Ứng dụng quản lý điểm và xếp loại sinh viên")

# 2. Tạo DataFrame
data = {
    "Ho_ten": [
        "An", "Binh", "Chi", "Dung", "Ha",
        "Lan", "Minh", "Nam", "Phuc", "Trang"
    ],
    "Chuyen_can": [4, 5, 6, 7, 8, 9, 10, 6, 7, 7],
    "Giua_ky": [10, 7, 6, 4, 8, 9, 5, 7, 7, 5],
    "Cuoi_ky": [8, 6, 7, 6, 9, 8, 7, 8, 8, 6]
}

df = pd.DataFrame(data)

# 3. Tính điểm tổng kết
df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
).round(2)

# 4. Xếp loại sinh viên
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 5. Hiển thị bảng điểm
st.subheader("1. Bảng điểm sinh viên")
st.dataframe(df, use_container_width=True)

# 6. Thống kê kết quả
st.subheader("2. Thống kê kết quả")

diem_tb = df["Tong_ket"].mean()
diem_cao_nhat = df["Tong_ket"].max()
diem_thap_nhat = df["Tong_ket"].min()
so_dat = int((df["Tong_ket"] >= 5).sum())

c1, c2, c3, c4 = st.columns(4)
c1.metric("Điểm trung bình", f"{diem_tb:.2f}")
c2.metric("Điểm cao nhất", f"{diem_cao_nhat:.2f}")
c3.metric("Điểm thấp nhất", f"{diem_thap_nhat:.2f}")
c4.metric("Số sinh viên đạt", f"{so_dat}/10")

# Hiển thị sinh viên có điểm cao nhất và thấp nhất
st.write(
    "**Sinh viên điểm cao nhất:**",
    ", ".join(df.loc[df["Tong_ket"] == diem_cao_nhat, "Ho_ten"])
)
st.write(
    "**Sinh viên điểm thấp nhất:**",
    ", ".join(df.loc[df["Tong_ket"] == diem_thap_nhat, "Ho_ten"])
)

# 7. Tra cứu sinh viên
st.subheader("3. Tra cứu sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Ho_ten"])
sv = df[df["Ho_ten"] == ten].iloc[0]

st.write(f"**Họ tên:** {sv['Ho_ten']}")
st.write(f"**Điểm chuyên cần:** {sv['Chuyen_can']}")
st.write(f"**Điểm giữa kỳ:** {sv['Giua_ky']}")
st.write(f"**Điểm cuối kỳ:** {sv['Cuoi_ky']}")
st.write(f"**Điểm tổng kết:** {sv['Tong_ket']}")
st.write(f"**Xếp loại:** {sv['Xep_loai']}")

# 8. Vẽ biểu đồ điểm tổng kết
st.subheader("4. Biểu đồ điểm tổng kết")

fig, ax = plt.subplots(figsize=(10, 5))
ax.barh(df["Ho_ten"], df["Tong_ket"])
ax.set_xlabel("Điểm tổng kết")
ax.set_ylabel("Sinh viên")
ax.set_xlim(0, 10)
ax.set_title("Điểm tổng kết của sinh viên")
fig.tight_layout()

st.pyplot(fig)
plt.close(fig)

# 9. Thông tin người thực hiện
st.divider()
st.caption("Người thực hiện: Tông Đăng Duy")
st.caption("MSSV: Điền mã số sinh viên của bạn")
