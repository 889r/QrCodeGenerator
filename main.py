import configparser
import qrcode

print(r" _____  _          __          __   _ _    _____      _ ")
print(r"|  __ \| |         \ \        / /  | | |  |  __ \    (_)")
print(r"| |__) | |_   _  __ \ \  /\  / /_ _| | | _| |__) |___ _ ")
print(r"|  ___/| | | | |/ _` \ \/  \/ / _` | | |/ /  _  // _ \ |")
print(r"| |    | | |_| | (_| |\  /\  / (_| | |   <| | \ \  __/ |")
print(r"|_|    |_|\__,_|\__, | \/  \/ \__,_|_|_|\_\_|  \_\___|_|")

def generate_qr_code(url, file_name="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=50,
        border=50,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

def get_website_url_from_config(config_file="config.ini"):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config.get("Settings", "website_url")

if __name__ == "__main__":
    website_url = get_website_url_from_config()
    generate_qr_code(website_url)
    print(f"QR code for {website_url} QrCode Generated Saved As qrcode.png.")
