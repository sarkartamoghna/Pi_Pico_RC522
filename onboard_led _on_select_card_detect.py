from mfrc522 import MFRC522
import utime
import machine

# Initialize RFID reader with SPI0 on Raspberry Pi Pico
rfid_reader = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)

# Initialize onboard LED (Pin 25 on Raspberry Pi Pico)
led = machine.Pin(25, machine.Pin.OUT)

# List of authorized card UIDs
authorized_cards = ["834734DA2A", "838E252A02"]

print("Waiting for a card...")

while True:
    # Check if a card is present
    (status, _) = rfid_reader.request(MFRC522.REQIDL)

    if status == rfid_reader.OK:
        print("Card detected!")  

        # Get UID of the detected card
        (status, uid) = rfid_reader.anticoll(MFRC522.PICC_ANTICOLL1)

        if status == rfid_reader.OK:
            rfid_card = "".join(["{:02X}".format(i) for i in uid])
            print("Detected Card UID:", rfid_card)

            # Check if the detected card is authorized
            if rfid_card in authorized_cards:
                print("Access Granted! Turning on LED.")
                led.value(1)  # Turn on LED
                utime.sleep(5)  # Keep LED on for 5 seconds
                led.value(0)  # Turn off LED
                print("LED turned off.")
            else:
                print("Access Denied.")

        else:
            print("Failed to read card UID")

    else:
        print("No card detected")  

    utime.sleep_ms(500)  # Short delay to prevent excessive polling

