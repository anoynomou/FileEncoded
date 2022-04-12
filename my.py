from simple_chalk import *
import os
import marshal

class EncriptionOpatations:

    
    @staticmethod
    def DecriptFile(input_filename,output_filename):
        with open(input_filename,"rb") as f:
            with open(output_filename+".py","w") as s:
                EncriptFileString = marshal.dumps(f.read())

                s.write(f"""import marshal\nexec(marshal.loads({EncriptFileString}))""")
                
            



subINPC = green.bgGray
infoINPB = gray.bgGreen



print(red("███████╗██╗██╗░░░░░███████╗  ███████╗███╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░████████╗██╗░█████╗░███╗░░██╗"))
print(red("██╔════╝██║██║░░░░░██╔════╝  ██╔════╝████╗░██║██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║"))
print(red("█████╗░░██║██║░░░░░█████╗░░  █████╗░░██╔██╗██║██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║██║░░██║██╔██╗██║"))
print(red("██╔══╝░░██║██║░░░░░██╔══╝░░  ██╔══╝░░██║╚████║██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║██║░░██║██║╚████║"))
print(red("██║░░░░░██║███████╗███████╗  ███████╗██║░╚███║╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░██║╚█████╔╝██║░╚███║"))
print(red("╚═╝░░░░░╚═╝╚══════╝╚══════╝  ╚══════╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝"))
print(yellow.bgGreen("\t\t\t\t\t\t\t\t\t\t\t version-1.0.0 \n\n\n"))



while True:
    input_file_path =str(input(subINPC("Enter File path >")))
    if(os.path.isfile(input_file_path) == True):
        print(green("\n file founded \n"))
        break
    else:
        print(red("\n file not found \n"))
        continue



while True:
    print(infoINPB("\n Enter Output FileName \n"))

    output_filename = str(input(subINPC( "FileName :")))
    if(len(output_filename) >0):
       EncriptionOpatations.DecriptFile(input_filename=input_file_path,output_filename=output_filename)
       break
    else:
        continue
    

    


