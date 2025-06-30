import random
import copy
import time
# import arbic_reshaper

class char:
    def __init__(self, charOrg, charLeet, charUpDown):
        self.charOrg = charOrg
        self.charLeet = charLeet
        self.charUpDown = charUpDown
        self.charCurr = charOrg
        self.corType = 0

    def charPrint(self):
        print(self.charCurr, end ='')

    def charPrintSlow(self, delayMinor):
        for x in self.charCurr:
            print(x, end = "", flush = True)
            time.sleep(delayMinor)

    def corLeet(self):
        self.charCurr = self.charLeet[random.randint(0, len(self.charLeet)-1)]

    def corUpDown(self):
        self.charCurr = self.charUpDown

char_a = char('a', ['4','@','Z','/\\','/-\\','^',], 'ɐ')
char_b = char('b', ['8','6','|3','13'], 'q')
char_c = char('c', ['(','{','<'], 'ɔ')
char_d = char('d', ['|)','[)','I>','|>','cl'], 'p')
char_e = char('e', ['3','&','[-'], 'ǝ')
char_f = char('f', ['|=','1=','ph'], 'ɟ')
char_g = char('g', ['6','9','&','(_+','C-'], 'ᵷ')
char_h = char('h', [']-[','}-{','#','}{'], 'ɥ')
char_i = char('i', ['l','1','|','!'], '!')
char_j = char('j', ['_|','_/',']'], 'f')
char_k = char('k', ['X','|<','|{'], 'ʞ')
char_l = char('l', ['I','|','7','|_'], 'l')
char_m = char('m', ['nn','|V|','IYI','.\\\\','/\\/\\','/|\\'], 'w')
char_n = char('n', ['|\\|','[\\]','<\\>','~'], 'u')
char_o = char('o', ['0','()','[]'], 'o')
char_p = char('p', ['|*','|"','?'], 'd')
char_q = char('q', ['9','O_','<|','O,'], 'b')
char_r = char('r', ['12','2','|2','|~','|^','|Z'], 'ɹ')
char_s = char('s', ['5','$','z'], 's')
char_t = char('t', ['7','+','-|-'], 'ʇ')
char_u = char('u', ['|_|','/_/','[_]','M'], 'n')
char_v = char('v', ['\\/'], 'ʌ')
char_w = char('w', ['vv','uu','.//','(n)','\\|/','\\/\\/'], 'ʍ')
char_x = char('x', ['%','*','><','}{'], 'x')
char_y = char('y', ['J','`/','`(','-/'], 'ʎ')
char_z = char('z', ['2','>=','~/_','3','7_'], 'z')
char_space = char(' ', [' '], ' ')

class word:
    def __init__(self, wordOrg):
        self.wordOrg = wordOrg
        self.wordArr = []
        self.corType = 0
        for ch in self.wordOrg:
            if ch == ' ':
                self.wordArr.append(copy.deepcopy(char_space))
            else:
                self.wordArr.append(copy.deepcopy(globals()['char_'+str(ch.lower())]))

    def wordPrint(self):
        match self.corType:
            case 2:
                print('█' * len(self.wordOrg), end = '')
            case 3:
                print("[REDACTED]", end = '')
            case 5:
                for i in range(len(self.wordArr)-1,-1,-1):
                    print(self.wordArr[i].charUpDown, end = '')
            case _:
                for ch in self.wordArr:
                    print(ch.charCurr, end = "")

    def wordPrintSlow(self, delay, delayMinor):
        match self.corType:
            case 2:
                for i in range(len(self.wordOrg)):
                    print('█', end = '', flush = True)
                    time.sleep(delay + delayMinor)
            case 3:
                for i in "[REDACTED]":
                    print(i, end = '', flush = True)
                    time.sleep(delay + delayMinor)
            case 5:
                for i in range(len(self.wordArr)-1,-1,-1):
                    print(self.wordArr[i].charUpDown, end = '', flush = True)
                    time.sleep(delay + delayMinor)
            case _:
                for ch in self.wordArr:
                    ch.charPrintSlow(delayMinor)

        time.sleep(delay)

    def corRandom(self):
        match random.randint(0,7):
            case 1|2:
                self.corLeet(20)
            case 3|4:
                self.corUpDown(10)
            case 5:
                self.corBlock()
            case 6:
                self.corRedact()
            case 7:
                self.corRotate()
            case _:
                pass
    
    def corLeet(self, chance):
        self.corType = 1
        for ch in self.wordArr:
            if random.randint(0,100) <= chance:
                ch.corLeet()

    def corBlock(self):
        self.corType = 2
    
    def corRedact(self):
        self.corType = 3

    def corUpDown(self, chance):
        self.corType = 4
        for ch in self.wordArr:
            if random.randint(0,100) <= chance:
                ch.corUpDown()
    
    def corRotate(self):
        self.corType = 5

class sentance:
    def __init__(self, sentance):
        self.sentanceArr = []
        wrd = ''
        self.sentanceOrg = sentance
        for ch in sentance:
            if ch != " ":
                wrd = wrd + ch
            else:
                self.sentanceArr.append(word(wrd))
                wrd = ''
                self.sentanceArr.append(copy.deepcopy(char_space))
        self.sentanceArr.append(word(wrd))

    def sentancePrint(self):
        for wrd in self.sentanceArr:
            if isinstance(wrd, word):
                wrd.wordPrint()
            elif isinstance(wrd, char):
                wrd.charPrint()
        print()

    def sentancePrintSlow(self, delay, delayMajor, delayMinor):
        for wrd in self.sentanceArr:
            if isinstance(wrd, word):
                wrd.wordPrintSlow(delay, delayMinor)
            elif isinstance(wrd, char):
                wrd.charPrintSlow(delayMinor)
        print()
        time.sleep(delayMajor)

    def corRandom(self, chance):
        for wrd in self.sentanceArr:
            if isinstance(wrd, word):
                if random.randint(0,100) <= chance:
                    wrd.corRandom()

def str2chararr(string):
    arr = []
    for i in string:
        arr.append(copy.deepcopy(globals()['char_'+str(i.lower())]))
    return arr

s = sentance("all work and no play makes ramy a dull boy")
for i in range(10):
    s.sentancePrintSlow(0.04,0.02,0.1)
    s.corRandom(10)
