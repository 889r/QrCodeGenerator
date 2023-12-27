import configparser
import qrcode

ascii_art = r"""
           
   ____        _____            
  / __ \      / ____|           
 | |  | |_ __| |  __  ___ _ __  
 | |  | | '__| | |_ |/ _ \ '_ \ 
 | |__| | |  | |__| |  __/ | | |
  \___\_\_|   \_____|\___|_| |_|
                                
                                
                                
"""

cool_message = """
  💻 Developed By @rei07x 
  🌐 GitHub: https://github.com/rei07x
  📡 Telegram: https://t.me/rei07x
"""

print(ascii_art)
print(cool_message)

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

def get_website_url_from_config(config_file="config.yaml"):
    config = configparser.ConfigParser()
    config.read(config_file)
    return config.get("Settings", "website_url")

if __name__ == "__main__":
    website_url = get_website_url_from_config()
    generate_qr_code(website_url)
    print(f"\nQR code for {website_url} Generated and Saved As qrcode.png.")

print()
