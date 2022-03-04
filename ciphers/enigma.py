
alpha = "ABCDEFGHIJKLMNOPQRSTUVWVYZ"
enigma_1_rotor_I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
enigma_1_rotor_II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
enimga_1_rotor_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

# TODO determine difference from Enigma 1 - current enigma class probably doesn't work with this 
commercial_rotor_alphabets = {
    "IC":   "DMTWSILRUYQNKFEJCAZBPGXOHV",
    "IIC":  "HQZGPJTMOBLNCIFDYAWVEUSRKX",
    "IIIC": "UQNTLSZFMREHDPXKIBVYGJCWOA",
}

# TODO determine difference from Enigma 1 - current enigma class probably doesn't work with this
railway_rotor_alphabets = {
    "I":    "JGDQOXUSCAMIFRVTPNEWKBLZYH",
    "II":   "NTZPSFBOKMWRCJDIVLAEYUXHGQ",
    "III":  "JVIUBHTCDYAKEQZPOSGXNRMWFL",
    "UKW":  "QYHOGNECVPUZTFDJAXWMKISRBL", # reflector
    "ETW":  "QWERTZUIOASDFGHJKPYXCVBNML"  # initial alphabet (vice alpha var)
}


enigma_I_rotor_alphabets = {
    "I":   "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
    "II":  "AJDKSIRUXBLHWTMCQGZNPYFVOE",
    "III":  "BDFHJLCPRTXVZNYEIWGAKMUSQO",
}



reflector_b = "YRUHQSLDPXNGOKMIEBFZCWVJAT"


s1 = 15
s2 = 4
s3 = 1



rotors = [enigma_1_rotor_I, enigma_1_rotor_II, enimga_1_rotor_III]
rotor_states = [s1, s2, s3]

def enc_letter(letter):
    """
    x = enimga_1_rotor_III[alpha.index(letter) + s3-1]
    print(x)
    x = enigma_1_rotor_II[alpha.index(x) + s2-1]
    print(x)
    x = enigma_1_rotor_I[alpha.index(x) + s1-1]
    print(x)
    x = reflector_b[alpha.index(x)]
    print(x)
    x = alpha[enigma_1_rotor_I.index(x) + s1-1]
    print(x)
    x = alpha[enigma_1_rotor_II.index(x) + s2-1]
    print(x)
    x = alpha[enimga_1_rotor_III.index(x) + s3-1]
    print(x)
    """

    x = letter
    for i in range(len(rotors)):
        x = rotors[i][(alpha.index(x) + rotor_states[i]-1)%26]

    x = reflector_b[alpha.index(x)]

    for i in range(len(rotors)):
        x = alpha[(rotors[2-i].index(x) + rotor_states[2-i]-1)%26]

    return x



class Rotor():

    def __init__(self, alphabet, notch: int=26, state: int=1):
        self.alphabet = alphabet
        self.state = state
        self.notch = notch
        self.next = None
        

    def step(self, notched=True):
        
        if self.next:
            self.next.step(notched=self.state == self.notch)

        if notched or self.state == self.notch:
            self.state = ((self.state) % 26) + 1 # increment and 1-index modulo 
        
        return self.state



class Enigma():
    
    rotor_alphabets = {
        "I":   ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
        "II":  ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
        "III": ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V")
    }


    def __init__(self, rotors, rotor_states):
        self.rotors = []
        for i in range(len(rotors)):
            r = self.rotor_alphabets[rotors[i]]
            self.rotors.append(Rotor(r[0], alpha.index(r[1])+1, rotor_states[i]))

        for i in range(len(rotors)-1):
            self.rotors[i].next = self.rotors[i+1]


    def encrypt(self, text: str):
        ret_text = ""
        print(alpha[self.rotors[2].state-1], alpha[self.rotors[1].state-1], alpha[self.rotors[0].state-1])
        for char in text:
            ret_text += self.enc_letter(char)
            self.rotors[0].step()
            print(alpha[self.rotors[2].state-1], alpha[self.rotors[1].state-1], alpha[self.rotors[0].state-1])

        return ret_text



    def enc_letter(self, letter):
        x = letter
        for i in range(len(self.rotors)):
            r = self.rotors[i]
            x = r.alphabet[(alpha.index(x) + r.state-1)%26]
 
        x = reflector_b[alpha.index(x)]

        for i in range(0, len(rotors), -1):
            r = self.rotors[i]
            x = alpha[(r.alphabet.index(x) + r.state-1)%26]

        return x




if __name__ == "__main__":
    

    enigma = Enigma(["I", "II", "III"], (15,4,1))
    print(enigma.encrypt("TEST"))

    print(enc_letter("T"))