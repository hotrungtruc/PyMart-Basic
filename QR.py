import qrcode
import tkinter as tk
from PIL import ImageTk, Image
from ttkbootstrap import Style
import tkinter.ttk as ttk
import urllib.parse

root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x500")
style = Style(theme='flatly')
style.theme_use()

def generate_qr_code():
    # Thông tin thanh toán MoMo
    partnerCode = "MOMO"
    partnerName = "Đối tác MoMo"
    storeId = "momo_store_123456"
    storeName = "Cửa hàng MoMo"
    requestId = "123456789"
    amount = amount_entry.get()  # Số tiền do người dùng nhập vào
    orderId = requestId  # Sử dụng requestId làm orderId
    orderInfo = "Thanh toán dịch vụ"
    redirectUrl = "https://your-return-url.com"
    ipnUrl = "https://your-notify-url.com"
    extraData = ""  # Dữ liệu thêm nếu có

    # Tạo URL thanh toán MoMo
    base_url = "https://api.momo.vn/gw_payment/transactionProcessor"
    params = {
        "partnerCode": partnerCode,
        "partnerName": partnerName,
        "storeId": storeId,
        "storeName": storeName,
        "requestId": requestId,
        "amount": amount,
        "orderId": orderId,
        "orderInfo": orderInfo,
        "redirectUrl": redirectUrl,
        "ipnUrl": ipnUrl,
        "extraData": extraData,
        "lang": "vi"
    }

    query_string = urllib.parse.urlencode(params)
    momo_url = f"{base_url}?{query_string}"

    # Tạo mã QR từ URL
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(momo_url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img = img.resize((300, 300))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.configure(image=img_tk)
    qr_label.image = img_tk

# Giao diện người dùng
amount_label = ttk.Label(master=root, text="Enter Amount (VND):")
amount_label.pack(pady=10)
amount_entry = ttk.Entry(master=root, width=50)
amount_entry.pack()

# Tạo nút để tạo mã QR
generate_button = ttk.Button(master=root, text="Generate QR Code",
                             command=generate_qr_code, style='success.TButton')
generate_button.pack(pady=10)

# Tạo nhãn để hiển thị mã QR
qr_label = ttk.Label(master=root)
qr_label.pack()

root.mainloop()
