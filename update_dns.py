import subprocess

# Tên giao diện mạng bạn muốn thay đổi
interface_name = "Ethernet 3"
# Địa chỉ DNS cũ bạn muốn thay đổi
old_dns = "11.11.4.3"
# Địa chỉ DNS mới bạn muốn đặt
new_dns = "11.11.11.11"

try:
    # Xóa DNS cũ trước (nếu có)
    subprocess.run(
        ["netsh", "interface", "ipv4", "delete", "dns", interface_name, old_dns],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    # Thêm DNS mới
    subprocess.run(
        ["netsh", "interface", "ipv4", "add", "dns", interface_name, new_dns, "index=1"],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    print(f"DNS đã được thay đổi thành {new_dns} trên giao diện mạng {interface_name}.")
except subprocess.CalledProcessError as e:
    print(f"Lỗi khi thay đổi DNS: {e.stderr}")