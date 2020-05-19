
import shutil, os
import sys

## Text menu in Python

one = sys.argv[1] 
two = sys.argv[2]
three = sys.argv[3]

def print_menu():       ## Your menu design here
    #clear screen
    os.system('clear')
    #menu
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. encrypt *** cmd syntax --- pyemail.bat key_name_receiver filename key_name_sender")
    print("2. decrypt *** cmd syntax --- pyemail.bat key_name_receiver filename key_name_sender")
    print("3. Generate keysfrodo *** cmd syntax --- pyemail.bat keyname 1 1 ")
    print("4. Generate keysfalcon *** cmd syntax --- pyemail.bat keyname 1 1 ")
    print("5. Exit")
    print(67 * "-")
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = eval(input("Enter your choice [1-5]: "))
     
    if choice==1:  
        print("Menu 1 has been selected")
        print("*** copy and enter key from cmd prompt")
        # delete keys
        os.remove("pk.txt")
        os.remove("sk.txt")
        # copy pk.txt from frodo
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keysfrodo")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("pk" + one + ".txt")
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("pk" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(source, destination)
        # copy sk.txt from frodo
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keysfrodo")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("sk" + one + ".txt")
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("sk" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(source, destination)
        os.system('python enc.py')
        pause = (input("hit enter to continue: "))
        symfile = ("gpg --symmetric --cipher-algo AES256 " + two )
        os.system(symfile)
        pause = (input("hit enter to continue: "))
        # delete keys
        os.remove("pk.txt")
        os.remove("sk.txt")
        # copy pk.txt from falcon
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keysfalcon")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("pk" + three + ".txt")
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("pk" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(source, destination)
        # copy sk.txt from falcon
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keysfalcon")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("sk" + three + ".txt")
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("sk" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(source, destination)
        # python SignFile with file 
        signfile = ("python SignFile.py " + two + " " + two + ".sig" )
        os.system( signfile )
        pause = (input("hit enter to continue: "))
        # copy ct to msg directory 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("ct" + ".txt")
        source = (os.path.join(currentDirectory, filenamepk))
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("MESSAGE")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("ct" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk)) 
        shutil.copy(source, destination)
        # copy gpg to msg directory
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = (two + ".gpg")
        source = (os.path.join(currentDirectory, filenamepk))
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("MESSAGE")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = (two + ".gpg")
        destination = (os.path.join(currentDirectory, filenamepk)) 
        shutil.copy(source, destination)        
        # copy sig to msg directory
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = (two + ".sig")
        source = (os.path.join(currentDirectory, filenamepk))
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("MESSAGE")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = (two + ".sig")
        destination = (os.path.join(currentDirectory, filenamepk)) 
        shutil.copy(source, destination)        
        #delete ct
        os.remove("ct.txt")
        #delete two 
        filename = (two)
        os.remove(filename)
        #delete two + .gpg
        filename = (two + ".gpg")
        os.remove(filename)
        #delete two + .sig
        filename = (two + ".sig")
        os.remove(filename)
        #clear screen
        os.system('clear')
    elif choice==2:
        print("Menu 2 has been selected")
        print("*** copy and enter key from cmd prompt")
        # delete keys
        os.remove("pk.txt")
        os.remove("sk.txt")
        # copy pk.txt from frodo
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keysfrodo")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("pk" + one + ".txt")
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("pk" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(source, destination)
        # copy sk.txt from frodo
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keysfrodo")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("sk" + one + ".txt")
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("sk" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(source, destination)
        os.system('python Dec.py')
        pause = (input("hit enter to continue: "))
        symfile = ("gpg -o " + two + " -d " + two + ".gpg")
        os.system(symfile)
        pause = (input("hit enter to continue: "))
        # delete keys
        os.remove("pk.txt")
        os.remove("sk.txt")
        # copy pk.txt from falcon
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keysfalcon")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("pk" + three + ".txt")
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("pk" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(source, destination)
        # copy sk.txt from falcon
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keysfalcon")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("sk" + three + ".txt")
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("sk" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(source, destination)
        # python SignFile with file 
        signfile = ("python VerifyFile.py " + two + " " + two + ".sig" )
        os.system( signfile )
        pause = (input("hit enter to continue: "))
        # copy ct to msg directory 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("ct" + ".txt")
        source = (os.path.join(currentDirectory, filenamepk))
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("MESSAGE")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("ct" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk)) 
        shutil.copy(source, destination)
        # copy gpg to msg directory
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = (two)
        source = (os.path.join(currentDirectory, filenamepk))
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("MESSAGE")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = (two)
        destination = (os.path.join(currentDirectory, filenamepk)) 
        shutil.copy(source, destination)        
        # copy gpg to msg directory
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = (two + ".gpg")
        source = (os.path.join(currentDirectory, filenamepk))
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("MESSAGE")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = (two + ".gpg")
        destination = (os.path.join(currentDirectory, filenamepk)) 
        shutil.copy(source, destination)        
        # copy sig to msg directory
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = (two + ".sig")
        source = (os.path.join(currentDirectory, filenamepk))
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("MESSAGE")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = (two + ".sig")
        destination = (os.path.join(currentDirectory, filenamepk)) 
        shutil.copy(source, destination)        
        #delete ct
        os.remove("ct.txt")
        #delete two 
        filename = (two)
        os.remove(filename)
        #delete two + .gpg
        filename = (two + ".gpg")
        os.remove(filename)
        #delete two + .sig
        filename = (two + ".sig")
        os.remove(filename)
        #clear screen
        os.system('clear')
    elif choice==3:
        #clear screen
        os.system('clear')
        print("Menu 3 has been selected")
        os.system('python keygen.py')
        # copy pk.txt to frodo
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keysfrodo")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("pk" + one + ".txt")
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("pk" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(destination, source)
        # copy sk.txt to frodo
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keysfrodo")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("sk" + one + ".txt")
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("sk" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(destination, source)
        pause = (input("hit enter to continue: "))
        os.system('clear')
    elif choice==4:
        #clear screen
        os.system('clear')
        print("Menu 4 has been selected")
        os.system('python keygen.py')
        # copy pk.txt to falcon
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keysfalcon")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("pk" + one + ".txt")
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("pk" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(destination, source)
        # copy sk.txt to falcon
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keysfalcon")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = ("sk" + one + ".txt")
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = ("sk" + ".txt")
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(destination, source)
        pause = (input("hit enter to continue: "))
        os.system('clear')
    elif choice==5:
        print("Menu 5 has been selected")
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
        os.system('clear')
    else:
        # Any integer inputs other than values 1-5 we print an error message
        input("Wrong option selection. Enter any key to try again..")
        
