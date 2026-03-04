import numpy as np
# 50 Product Names (Realistic E-commerce Products)
product_names = np.array([
" Laptop"," Mouse"," Keyboard"," Monitor"," Headphones",
" USB Cable"," Webcam"," External Hard Drive"," Printer"," Router",
" Tablet"," Smartphone"," Speakers"," Microphone"," Gaming Chair",
" Power Bank"," Smart Watch"," Graphics Card"," SSD"," RAM",
" Cooling Pad"," HDMI Cable"," Laptop Stand"," Wireless Charger"," Bluetooth Adapter",
" Portable SSD"," Mechanical Keyboard"," Gaming Mouse"," LED Monitor"," Noise Cancelling Headphones",
" Office Chair"," Desk Lamp"," Network Switch"," Smart TV"," Streaming Device",
" VR Headset"," Drone Camera"," Action Camera"," Tripod"," DSLR Camera",
" Memory Card"," CPU Processor"," Motherboard"," PC Cabinet"," UPS Battery Backup",
" WiFi Extender"," Ethernet Cable"," Touchscreen Monitor"," Stylus Pen"," Tablet Cover"
])

# 100 Users × 50 Products rating matrix
# Ratings: 0–5 (0 = Not purchased / Not rated)

num_users = 100
num_products = 50

ratings = np.random.randint(0,6,(num_users,num_products))

print("Total Products:", len(product_names))
print(product_names)

print("\nDataset Shape (Users × Products):")
print(ratings.shape)

print("\nUser-Product Rating Matrix:")
print(ratings)