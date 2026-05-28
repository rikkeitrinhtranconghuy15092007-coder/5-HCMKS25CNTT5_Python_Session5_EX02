# =============================================
# HỆ THỐNG THỐNG KÊ SỐ LƯỢNG HỌC VIÊN THEO CHI NHÁNH
# =============================================

so_chi_nhanh = int(input("Nhập số lượng chi nhánh: "))

for cn in range(1, so_chi_nhanh + 1):
    
    # === QUAN TRỌNG: Reset tổng về 0 khi bắt đầu chi nhánh mới ===
    total_students = 0
    
    so_lop = int(input(f"Chi nhánh {cn} có bao nhiêu lớp: "))
    
    for lop in range(1, so_lop + 1):
        hoc_vien = int(input(f"    Lớp {lop} có: "))
        total_students += hoc_vien
    
    # Hiển thị kết quả của chi nhánh
    print(f"Chi nhánh {cn}: {total_students} học viên\n")