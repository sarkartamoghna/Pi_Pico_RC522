from mfrc522 import MFRC522
import utime

# Initialize MFRC522 with SPI0 on Raspberry Pi Pico
rfid_reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)

print("Waiting for a card...")

while True:
    # ✅ Fix: Ensure request() has the correct arguments
    (status, _) = rfid_reader.request(MFRC522.REQIDL)  

    if status == rfid_reader.OK:
        print("Card detected!")  # Debugging print
        
        # ✅ Fix: Pass the required argument to `anticoll()`
        (status, uid) = rfid_reader.anticoll(MFRC522.PICC_ANTICOLL1)

        if status == rfid_reader.OK:
            rfid_card = "".join(["{:02X}".format(i) for i in uid])
            print("Detected Card UID:", rfid_card)
        else:
            print("Failed to read card UID")

    else:
        print("No card detected")  # Debugging print

    utime.sleep_ms(500)

