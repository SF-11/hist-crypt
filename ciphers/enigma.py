
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


s3 = 1
s2 = 1
s1 = 1



rotors = [enimga_1_rotor_III, enigma_1_rotor_II, enigma_1_rotor_I]
rotor_states = [s3, s2, s1]

def enc_letter(letter):
    print(letter)
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
        x = rotors[i][alpha.index(x) + rotor_states[i]-1]
        print(x)

    x = reflector_b[alpha.index(x)]
    print(x)

    for i in range(len(rotors)):
        x = alpha[rotors[2-i].index(x) + rotor_states[2-i]-1]
        print(x)



class Rotor():

    def __init__(self, state: int=1, notch: int=26):
        self.state = state
        self.notch = notch
        self.next = None
        

    def step(self):
        self.state += 1
        if self.state == 27: self.state = 1

        if self.state == self.notch and self.next != None:
            self.next.step()

        return self.state



class Engima():
    pass

    def __init__(self, rotor_states):
        self.rotors = [Rotor(rotor_states[i]) for i in rotor_states]


if __name__ == "__main__":
    
    r1 = Rotor(state=15, notch=17)
    r2 = Rotor(state=4, notch=5)
    r3 = Rotor(state=1, notch=22)
    

    r1.next = r2
    r2.next = r3

    print(alpha[r3.state-1], alpha[r2.state-1], alpha[r1.state-1])
    for i in range(10):
        r1.step()
        print(alpha[r3.state-1], alpha[r2.state-1], alpha[r1.state-1])

    print()    
    enc_letter("A")