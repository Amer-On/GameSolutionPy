import main
adr_out = "../output/output" + str(main.num) + '.txt'
fout = open(adr_out, 'w')

fout.writelines(str(main.maximum) + '\n')
fout.writelines(" ".join(main.moves))


fout.close()
