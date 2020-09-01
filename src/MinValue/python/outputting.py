import simple_input as si
num = 1
adr_out = "../output/output" + str(num) + '.txt'
fout = open(adr_out, 'w')

fout.write(str(si.maximum))

fout.close()
