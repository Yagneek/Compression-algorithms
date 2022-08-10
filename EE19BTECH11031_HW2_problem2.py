import numpy as np

#Calculating empirical pmf and entropy
def H(p):	
	H = 0
	for i in p:
		if(i > 0):
			H -= i*np.log2(i)
	return H
input_file = open('inputfile_problem2_31.txt', encoding="utf8")
data = input_file.read()
input_file.close()
a = [ord(i)-ord('a') for i in data] #a is taken as 0, b as 1 and so on
count = 0
p = np.zeros(26)
for i in a:
	if i < 26:
		count += 1
		p[i] += 1
prob = p/count #empirical pmf
print("Empirical pmf = ", prob)
HX = H(prob)
print("Entropy of the txt file = "+str(HX))

def encoder(codes, input_fileName, code_name):
    input_file = open(input_fileName, encoding="utf8")
    data = input_file.read()
    input_file.close()
    #ensuring that the output file is empty
    output_file = open("EE19BTECH11031_HW2_problem2_"+code_name+".txt","w")
    output_file.write("")
    output_file.close()
    output_file = open("EE19BTECH11031_HW2_problem2_"+code_name+".txt","a")
    compressed_length = 0
    for i in data:
        output_file.write(codes[ord(i)-ord('a')])   #We write the corresponding encoded symbol for each character in the output file
        compressed_length += len(codes[ord(i)-ord('a')])
    output_file.close()
    print("length of the "+code_name+" compressed sequence = ", compressed_length)

def decoder(codes, input_fileName, code_name):
    input_file = open(input_fileName, encoding="utf8")
    data = input_file.read()
    input_file.close()
    #ensuring that the output file is empty
    output_file = open("EE19BTECH11031_HW2_problem2_"+code_name+"_decode.txt","w")
    output_file.write("")
    output_file.close()
    output_file = open("EE19BTECH11031_HW2_problem2_"+code_name+"_decode.txt","a")
    temp = ""
    #checks if x is a codeword
    def isCodeword(x):
        for i in range(len(codes)):
            if x==codes[i]:
                return chr(ord('a')+i)
        return '*'
    for i in data:
        temp += i
        ch = isCodeword(temp)
        #if temp is a codeword
        if ch!='*':
            output_file.write(ch)
            temp = ""
    output_file.close()


shannon_codes = ['1100','1101100','0','11010','10']
encoder(shannon_codes,'inputfile_problem2_31.txt','shannon')
decoder(shannon_codes,'EE19BTECH11031_HW2_problem2_shannon.txt','shannon')

huffman_codes = ['110','1111','0','1110','10']
encoder(huffman_codes,'inputfile_problem2_31.txt','huffman')
decoder(huffman_codes,'EE19BTECH11031_HW2_problem2_huffman.txt','huffman')

ShannonFanoElias_codes = ['00001','00010010','01','100111','110']
encoder(ShannonFanoElias_codes,'inputfile_problem2_31.txt','ShannonFanoElias')
decoder(ShannonFanoElias_codes,'EE19BTECH11031_HW2_problem2_ShannonFanoElias.txt','ShannonFanoElias')
