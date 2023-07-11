import string

class EnigmaM3:
    def __init__(self, rotor_config, rotor_positions, ring_settings):
        self.alphabet = string.ascii_uppercase
        self.rotors = {}
        self.position = rotor_positions
        self.rings = ring_settings
        self.reflector = {
            'A': 'Y', 'B': 'R', 'C': 'U', 'D': 'H', 'E': 'Q', 'F': 'S', 'G': 'L', 'H': 'D', 'I': 'P',
            'J': 'X', 'K': 'N', 'L': 'G', 'M': 'O', 'N': 'K', 'O': 'M', 'P': 'I', 'Q': 'E', 'R': 'B',
            'S': 'F', 'T': 'Z', 'U': 'C', 'V': 'W', 'W': 'V', 'X': 'J', 'Y': 'A', 'Z': 'T'
        }
        self.rotor_config_default = {
            'I': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
            'II': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
            'III': 'BDFHJLCPRTXVZNYEIWGAKMUSQO'
        }
        self.turnovers = {
            'I': 'Q', 'II': 'E', 'III': 'V'
        }
        self.turnover_default = {
            'I': 'Q', 'II': 'E', 'III': 'V'
        }
        self.reverse_wire_default = {'I': ['U', 'W', 'Y', 'G', 'A', 'D', 'F', 'P', 'V', 'Z', 'B', 'E', 'C', 'K', 'M', 'T', 'H', 'X', 'S', 'L', 'R', 'I', 'N', 'Q', 'O', 'J'], 
                                     'II': ['A', 'J', 'P', 'C', 'Z', 'W', 'R', 'L', 'F', 'B', 'D', 'K', 'O', 'T', 'Y', 'U', 'Q', 'G', 'E', 'N', 'H', 'X', 'M', 'I', 'V', 'S'], 
                                     'III': ['T', 'A', 'G', 'B', 'P', 'C', 'S', 'D', 'Q', 'E', 'U', 'F', 'V', 'N', 'Z', 'H', 'Y', 'I', 'X', 'J', 'W', 'L', 'R', 'K', 'O', 'M']}  
        self.reverse_wire = {}
        self.reverse_wire['I'] =  [''] * 26
        self.reverse_wire['II'] = [''] * 26
        self.reverse_wire['III'] = [''] * 26
        self.plugboard = {}
        for rotor, wiring in rotor_config.items():
            self.rotors[rotor] = wiring
            for i in range(26):
                self.reverse_wire[rotor][self.alphabet.index(self.rotors[rotor][i])] = self.alphabet[i]
        
    def rotate(self):
        self.position['III'] = self.alphabet[(self.alphabet.index(self.position['III']) + 1) % 26]
        if self.position['III'] == self.turnovers['III']:
            self.position['II'] = self.alphabet[(self.alphabet.index(self.position['II']) + 1) % 26]
            if self.position['II'] == self.turnovers['II']:
                self.position['I'] = self.alphabet[(self.alphabet.index(self.position['I']) + 1) % 26]
    
    def encrypt(self, char):
        if char not in self.alphabet:
            return char
        print()
        self.rotate()
        print("Current Rotor Position:\nLeft: " + self.position['I'] + "\nMiddle: " + self.position['II'] + "\nRight: " + self.position['III'])
        print()
        print("Input character: " + char)
        
        char = self.plugboard.get(char, char)
        print("Enkripsi Plugboard: " + char)
        char = self.alphabet[(self.alphabet.index(self.rotors['III'][(self.alphabet.index(char) + self.alphabet.index(self.position['III']) - self.alphabet.index(self.rings['III'])) % 26]) - (self.alphabet.index(self.position['III']) - self.alphabet.index(self.rings['III']))) % 26]
        print("Enkripsi rotor kanan: " + char)
        char = self.alphabet[(self.alphabet.index(self.rotors['II'][(self.alphabet.index(char) + self.alphabet.index(self.position['II']) - self.alphabet.index(self.rings['II'])) % 26]) - (self.alphabet.index(self.position['II']) - self.alphabet.index(self.rings['II']))) % 26]
        print("Enkripsi rotor tengah: " + char)
        char = self.alphabet[(self.alphabet.index(self.rotors['I'][(self.alphabet.index(char) + self.alphabet.index(self.position['I']) - self.alphabet.index(self.rings['I'])) % 26]) - (self.alphabet.index(self.position['I']) - self.alphabet.index(self.rings['I']))) % 26]
        print("Enkripsi rotor kiri: " + char)
        char = self.reflector[char]
        print("Enkripsi reflector: " + char)
        char = self.alphabet[(self.alphabet.index(self.reverse_wire['I'][(self.alphabet.index(char) + self.alphabet.index(self.position['I']) - self.alphabet.index(self.rings['I'])) % 26]) - (self.alphabet.index(self.position['I']) - self.alphabet.index(self.rings['I']))) % 26]
        print("Enkripsi rotor kiri: " + char)
        char = self.alphabet[(self.alphabet.index(self.reverse_wire['II'][(self.alphabet.index(char) + self.alphabet.index(self.position['II']) - self.alphabet.index(self.rings['II'])) % 26]) - (self.alphabet.index(self.position['II']) - self.alphabet.index(self.rings['II']))) % 26]
        print("Enkripsi rotor tengah: " + char)
        char = self.alphabet[(self.alphabet.index(self.reverse_wire['III'][(self.alphabet.index(char) + self.alphabet.index(self.position['III']) - self.alphabet.index(self.rings['III'])) % 26]) - (self.alphabet.index(self.position['III']) - self.alphabet.index(self.rings['III']))) % 26]
        print("Enkripsi rotor kanan: " + char)
        char = self.plugboard.get(char, char)
        print("Enkripsi Plugboard: " + char)
        print()
        
        return char
    
    def set_rotor_position(self, rotor, position):
        self.position[rotor] = position
    
    def set_ring(self, rotor, position):
        self.rings[rotor] = position
    
    def set_ring_setting(self, rotor, setting):
        self.rings[rotor] = setting
    
    def add_plug(self, char1, char2):
        if char1 not in self.plugboard.values() and char2 not in self.plugboard.values():
            self.plugboard[char1] = char2
            self.plugboard[char2] = char1
            print("Plug added: " + char1 + "-" + char2)
        else:
            print("Plug already exists!")

    def print_positions(self):
        print()
        print("Current Rotor Positions:")
        
        print("1. Left Rotor: " + self.position['I'])
        print("2. Middle Rotor: " + self.position['II'])
        print("3. Right Rotor: " + self.position['III'])
        print()
        
    def print_rings(self):
        print()
        print("Current Rotor Ring Positions:")
        
        print("1. Left Rotor: " + self.rings['I'])
        print("2. Middle Rotor: " + self.rings['II'])
        print("3. Right Rotor: " + self.rings['III'])
        print()
            
    def remove_plug(self, char):
        if char in self.plugboard:
            char2 = self.plugboard[char]
            del self.plugboard[char]
            del self.plugboard[char2]
    
    def set_initial_position(self, initial_positions):
        for rotor, position in initial_positions.items():
            self.set_rotor_position(rotor, position)
    
    def set_initial_ring_setting(self, initial_settings):
        for rotor, setting in initial_settings.items():
            self.set_ring_setting(rotor, setting)
    
    def encrypt_text(self, text):
        text = text.upper()
        encrypted_text = ''

        for char in text:
            if char == ' ':
                encrypted_text += ' '
            else:
                encrypted_text += self.encrypt(char)

        return encrypted_text

    
    def decrypt_text(self, text):
        text = text.upper()
        decrypted_text = ''

        for char in text:
            if char == ' ':
                decrypted_text += ' '
            else:
                decrypted_text += self.encrypt(char)

        return decrypted_text
    
    def get_rotor(self, id):
        return self.rotors[id]
    
    def set_rotor(self, rotor_id, rotor_target):
        self.rotors[rotor_id] = self.rotor_config_default[rotor_target]
        self.turnovers[rotor_id] = self.turnover_default[rotor_target]
        self.reverse_wire[rotor_id] = self.reverse_wire_default[rotor_target]
            
        
    def print_plugboard(self):
        print("Plugboard Configuration:")
        for char1, char2 in self.plugboard.items():
            print(f"{char1}-{char2}")
    
    def set_turnover(self, id,target):
        self.turnovers[id] = self.turnover_default[target]

def decryptor(ciphertext):
    # enigma = EnigmaM3({}, {'I': 'A', 'II': 'A', 'III': 'A'}, {'I': 'A', 'II': 'A', 'III': 'A'})
    decrypted_text = ""

    rotor_config = {
    'I': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ',
    'II': 'AJDKSIRUXBLHWTMCQGZNPYFVOE',
    'III': 'EKMFLGDQVZNTOWYHXUSPAIBRCJ'
    }

    rotor_positions = {
        'I': 'A',
        'II': 'A',
        'III': 'A'
    }

    ring_positions = {
        'I': 'A',
        'II': 'A',
        'III': 'A'
    }


    enigma = EnigmaM3(rotor_config, rotor_positions, ring_positions)

    initial_positions = {
        'I': 'A',
        'II': 'A',
        'III': 'A'
    }

    enigma.set_initial_position(initial_positions)
    enigma.set_turnover('III','I')
    
    for rotor1 in enigma.rotor_config_default.keys(): 
        for rotor2 in enigma.rotor_config_default.keys():
            for rotor3 in enigma.rotor_config_default.keys():
            # rotor3 = 'II'    
                for pos1 in enigma.alphabet:
                    for pos2 in enigma.alphabet:
                        for pos3 in enigma.alphabet:
                            enigma.set_rotor('I', rotor1)
                            enigma.set_rotor('II', rotor2)
                            enigma.set_rotor('III', rotor3)
                            enigma.set_rotor_position('I', pos1)
                            enigma.set_rotor_position('II', pos2)
                            enigma.set_rotor_position('III', pos3)
                            print(enigma.position)
                            print(enigma.rotors)
                            decrypted_text = enigma.decrypt_text(ciphertext[:10])
                            if decrypted_text.startswith('HELLO SUDO'):
                                enigma.set_rotor('I', rotor1)
                                enigma.set_rotor('II', rotor2)
                                enigma.set_rotor('III', rotor3)
                                enigma.set_rotor_position('I', pos1)
                                enigma.set_rotor_position('II', pos2)
                                enigma.set_rotor_position('III', pos3)
                                return enigma.decrypt_text(ciphertext)
                            
    return "NOT FOUND"
