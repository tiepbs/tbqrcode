import qrcode
from PIL import Image

def generate_qr_code(url, file_path, logo_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white').convert('RGB')

    if logo_path:
        logo = Image.open(logo_path)
        logo = logo.convert("RGBA")
        logo_size = int(min(img.size) * 0.25)
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)
        mask = logo.split()[3]
        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos, mask)

    img.save(file_path)
    print(f"QR code generated and saved to {file_path} with embedded logo")
