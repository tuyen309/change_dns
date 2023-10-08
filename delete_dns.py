import os
import subprocess

# Địa chỉ DNS cần xóa  
dns_to_remove = "11.11.11.11"

# Lấy danh sách DNS hiện tại
cmd = "netsh interface ip show dnsservers"
result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
dns_list = result.stdout.splitlines()
print("-------------------" ,dns_list)
interface_name = "Ethernet 3"
# Duyệt qua các dòng để tìm và xóa DNS
for line in dns_list:
    if dns_to_remove in line:
        # # Xóa DNS đó đi
        # delete_cmd = f"netsh interface ipv4 delete dns \"{line.strip()}\""
        # os.system(delete_cmd)
        subprocess.run(
            ["netsh", "interface", "ipv4", "delete", "dns", interface_name, dns_to_remove],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )

print("Đã kiểm tra và xóa DNS thành công.")