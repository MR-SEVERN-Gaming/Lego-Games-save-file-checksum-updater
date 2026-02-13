import sys
import os
import math as m
import numpy as np

np.seterr(all='ignore')

def main():
    try:
        savefile = sys.argv[1]
    except IndexError:
        input("No file dropped! Please drop the save file you want to update the checksum of\nPress enter to close")
        return

    if not os.path.isfile(savefile):
        input(f"File not found: {savefile}\nPress enter to close")
        return

    filesize = os.path.getsize(savefile)

    with open(savefile, 'r+b') as file:
        def ChecksumCount(start, end, order, salt):
            checksum = salt
            file.seek(start)
            for _ in range(0, m.trunc((end - start) / 4)):
                fileread = file.read(4)
                checksum = np.uint32(int.from_bytes(fileread, byteorder=order, signed=False)) + np.uint32(checksum)
            oldchecksum = int.from_bytes(file.read(4), byteorder=order, signed=False)
            old_hex = int(oldchecksum).to_bytes(4, "little").hex().upper()
            new_hex = int(checksum).to_bytes(4, "little").hex().upper()
            old_hex = " ".join(old_hex[i:i+2] for i in range(0, len(old_hex), 2))
            new_hex = " ".join(new_hex[i:i+2] for i in range(0, len(new_hex), 2))
            if checksum == oldchecksum:
                input(f"New checksum ({old_hex}) already matches the existing one. Press enter to close")
                return True
            print(f"\nOld Checksum: {old_hex} ({oldchecksum})")
            print(f"\nNew Checksum: {new_hex} ({checksum})")
            file.seek(end)
            file.write(int(checksum).to_bytes(4, byteorder=order))
            return False


        # LIJ2
        if filesize == 537984:
            print("LIJ2 PC Save File Detected")
            if ChecksumCount(8232, 537976, "little", 6031769):
                return
        
        # LB1
        elif filesize == 40520:
            print("LB1 PC Save File Detected")
            if ChecksumCount(8232, 40512, "little", 6031769):
                return
        
        # LIJ1
        elif filesize == 40880:
            print("LIJ1 PC Save File Detected")
            if ChecksumCount(8232, 40872, "little", 6031769):
                return

        # TCS
        elif filesize == 40572:
            print("TCS PC Save File Detected")
            if ChecksumCount(8232, 40564, "little", 6031769):
                return
        elif filesize == 32336:
            print("TCS Ps3 Save File Detected")
            if ChecksumCount(0, 32332, "big", 6031769):
                return
        elif filesize == 32360:
            print("TCS Xbox 360 Save File Detected")
            if ChecksumCount(0, 32356, "big", 6031769):
                return
        elif filesize == 131072:
            print("TCS Wii Save File Detected")
            if ChecksumCount(60, 32392, "big", 6031769):
                return

        # LSW2
        elif filesize == 79252:
            print("LSW2 Ps2 (Ps3 Format) Save File Detected")
            if ChecksumCount(76272, 77276, "little", 0):
                return
        elif filesize == 960:
            print("LSW2 Ps2 Print Preview Save File Detected")
            if ChecksumCount(0, 956, "little", 0):
                return
        elif filesize == 1008:
            print("LSW2 PC/Ps2/Xbox 360 File Detected")
            version = input("Enter 1 for PC/Ps2 Save or 2 for Xbox 360 Save.\nIf you select the wrong one, just run it again and choose the correct one: ")
            if version == "1":
                if ChecksumCount(0, 1004, "little", 0):
                    return
            elif version == "2":
                if ChecksumCount(0, 1004, "big", 0):
                    return
            else:
                input("Invalid choice. Press enter to close")
                return
        elif filesize == 1032:
            print("LSW2 Xbox Save File Detected")
            if ChecksumCount(4, 1008, "little", 0):
                return
        elif filesize == 8528:
            print("LSW2 GC Save File Detected")
            if ChecksumCount(1996, 3000, "big", 0):
                return
        elif filesize == 8256:
            print("LSW2 GC Save File Detected")
            if ChecksumCount(1724, 2728, "big", 0):
                return
        elif filesize == 1040:
            print("LSW2 PSP Save File Detected")
            if ChecksumCount(4, 1036, "little", 0):
                return

        # LSW1
        elif filesize == 532:
            print("LSW1 PC/Ps2/Ps2 Preview Save File Detected")
            if ChecksumCount(0, 528, "little", 0):
                return
        elif filesize == 58550:
            print("LSW1 Ps2 Save FIle Detected")
            if ChecksumCount(58014, 58542, "little", 0):
                return
        elif filesize == 24640:
            print("LSW1 GC Save FIle Detected")
            if ChecksumCount(8852, 9380, "big", 0):
                return
        elif filesize == 24912:
            print("LSW1 GC Save FIle Detected")
            if ChecksumCount(1952, 2480, "big", 0):
                return
        elif filesize == 57620:
            print("LSW1 Ps2 (Ps3 Format) Save File Detected")
            if ChecksumCount(57088, 57616, "little", 0):
                return

        else:
            input("This is not a valid save file. Press enter to close")
            return

    input("\nChecksum of the save file has been updated. Press enter to close")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press enter to close the window")
