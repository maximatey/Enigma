from Enigma import EnigmaM3
import string

rotor_config = {
    'I': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
    'II': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
    'III': 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
}

alphabet = string.ascii_uppercase

rotor_positions = {
    'I': 'A',
    'II': 'A',
    'III': 'A'
}

enigma = EnigmaM3(rotor_config, rotor_positions, rotor_positions)

initial_positions = {
    'I': 'A',
    'II': 'A',
    'III': 'Z'
}

enigma.set_initial_position(initial_positions)

print("Welcome to Virtual Enigma Machine!")
print("Catatan : Karena enkripsi dan dekripsi mesin enigma melewati proses yang sama, gunakan opsi 2 atau 3 untuk melakukan enkripsi dan/atau dekripsi.")
print("=" * 50)

option = -1
settingOption = -1
optionText = "Pilih Nomor Opsi yang ingin digunakan! (1/2/3) \n1. Setting Mesin\n2. Input per huruf\n3. Input kalimat\n999. Keluar"
settingText = "1. Setting rotor\n2. Setting plugboard\n3. Setting Rotor Position\n999. Kembali"
rotorListText = "Berikut list rotor yang tersedia:\n1. Rotor I : EKMFLGDQVZNTOWYHXUSPAIBRCJ \n2. Rotor II : AJDKSIRUXBLHWTMCQGZNPYFVOE\n3. Rotor III: BDFHJLCPRTXVZNYEIWGAKMUSQO"
while True:
    option = -1
    
    print("Current configs: ")
    print()
    print("Current rotors :\n1. Rotor kiri: " + enigma.get_rotor('I') + "\n2. Rotor tengah: " + enigma.get_rotor('II') + "\n3. Rotor kanan: "+ enigma.get_rotor('III'))
    print()
    enigma.print_plugboard()
    print()
    enigma.print_positions()
    print()
    
    print(optionText)
    option = input("Pilihan: ")
    print("=*" * 25)
    if option == '1':
        while True:
            print(settingText)
            settingOption = input("Pilihan: ")
            print("=*" * 25)
            if settingOption == '1':
                print("Current rotors :\n1. Rotor kiri: " + enigma.get_rotor('I') + "\n2. Rotor tengah: " + enigma.get_rotor('II') + "\n3. Rotor kanan: "+ enigma.get_rotor('III') + "\n999. Kembali")
                print("Pilih rotor yang ingin diubah")
                opsiUbahRotor = -1
                opsiUbahRotor = input()
                if opsiUbahRotor == '999':
                    break
                elif opsiUbahRotor == '1':
                    print(rotorListText)
                    opsiGear = input("Pilihan (I/II/III): ")
                    while opsiGear not in ['I','II','III']:
                        print("Invalid input, silahkan input kembali")
                        opsiGear = input("Pilihan: ")
                    enigma.set_rotor('I', opsiGear)
                elif opsiUbahRotor == '2':
                    print(rotorListText)
                    opsiGear = input("Pilihan (I/II/III): ")
                    while opsiGear not in ['I','II','III']:
                        print("Invalid input, silahkan input kembali")
                        opsiGear = input("Pilihan: ")
                    enigma.set_rotor('II', opsiGear)
                elif opsiUbahRotor == '3':
                    print(rotorListText)
                    opsiGear = input("Pilihan (I/II/III): ")
                    while opsiGear not in ['I','II','III']:
                        print("Invalid input, silahkan input kembali")
                        opsiGear = input("Pilihan: ")
                    enigma.set_rotor('III', opsiGear)
                else:
                    print("Invalid Input!")
            elif settingOption == '2':
                print("Current Plugboard:\n")
                enigma.print_plugboard()
                print("1. Add plug\n2. Remove plug\n999. Kembali")
                print("Pilihan: ")
                optionPlug = -1
                optionPlug = input()
                if optionPlug=='1':
                    plug1 = input("Plug 1 :").upper()
                    plug2 = input("Plug 2 :").upper()
                    
                    while (plug1 not in alphabet) or (plug2 not in alphabet):
                        print("Invalid inputs, please try again")
                        plug1 = input("Plug 1 :").upper()
                        plug2 = input("Plug 2 :").upper()
                    
                    enigma.add_plug(plug1,plug2)
                elif optionPlug == '2':
                    plug1 = input("Plug (Choose either character) :").upper()
                    
                    while (plug1 not in alphabet) :
                        print("Invalid inputs, please try again")
                        plug1 = input("Plug (Choose either character) :").upper()
                        
                    enigma.remove_plug(plug1)
                elif optionPlug == '999':
                    break
                else: 
                    print("Invalid Input!")
            elif settingOption == '3':
                enigma.print_positions()
                print("Pilihan (1/2/3)")
                posOption = input()
                if posOption == '1':
                    print("Pilih posisi rotor (A-Z) :")
                    poschar = input().upper()
                    while poschar not in alphabet:
                        print("Invalid Input!")
                        print("Pilih posisi rotor (A-Z) :")
                        poschar = input().upper()
                    enigma.set_rotor_position('I',poschar)
                    print("\nRotor I has set to position "  + poschar + "\n")
                elif posOption == '2':
                    print("Pilih posisi rotor (A-Z) :")
                    poschar = input().upper()
                    while poschar not in alphabet:
                        print("Invalid Input!")
                        print("Pilih posisi rotor (A-Z) :")
                        poschar = input().upper()
                    enigma.set_rotor_position('II',poschar)
                    print("\nRotor II has set to position "  + poschar + "\n")
                elif posOption == '3':
                    print("Pilih posisi rotor (A-Z) :")
                    poschar = input().upper()
                    while poschar not in alphabet:
                        print("Invalid Input!")
                        print("Pilih posisi rotor (A-Z) :")
                        poschar = input().upper()
                    enigma.set_rotor_position('III',poschar)
                    print("\nRotor III has set to position "  + poschar + "\n")
                else :
                    print("Invalid input!")
            elif settingOption == '999':
                break
            else:
                print("Invalid Input!")
                print()
    elif option == '2':
        intext = ""
        outtext = ""
        print("INPUT 999 UNTUK KELUAR")
        while True:
            char = input("Input:").upper()
            if char in alphabet:
                intext = intext + char
                char2 = enigma.encrypt(char)
                outtext = outtext + char2
                print("Output: " + char2)
                print()
                print("Input text: " + intext)
                print("Output text: " + outtext)
            elif char == '999':
                break
            else:
                print("Invalid input")
    elif option == '3':
        intext = ""
        outtext = ""
        valid = True
        print("Input kalimat yang ingin dienkripsi/dekripsi")
        intext = input().upper()
        
        for char in intext:
            if char not in alphabet and char != ' ':
                valid = False
        
        while not valid:
            print("Invalid input")
            print()
            print("Input kalimat yang ingin dienkripsi/dekripsi")
            intext = input().upper
            valid = True
            
            for char in intext:
                if char not in alphabet and char != ' ':
                    valid = False
                    
        print("Encrypting: " + intext)
        outtext = enigma.encrypt_text(intext)
        print("Output: " + outtext)
        print()
        
    elif option=='999':
        break
    else:
        print("Invalid Input!")
    print()

print()
print("Sayonara~")
        
        
                
                
                    
                        
                    
    