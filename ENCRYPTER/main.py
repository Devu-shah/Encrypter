import string as st

class Encrypter: 
    def setting1(text):

        if text == '':
            print("Please Try again!!")
            text = str(input("Enter a String to Encrypt: "))
            Encrypter.setting1(text)

        else:
            l = []
            excrypted_list = []
            all_num_list = []
            print("Ignore the Square Brackets\n")
            for char in text:
                for x in range(0,len(st.printable)):  
                    if char == st.printable[x]:
                        l.append(x)

            for b in l: 
                for j in range(0,len(l)):
                    if j%2==0:
                        all_num_list.append(int(l[j])+1)
                    elif j%2==1:
                        all_num_list.append(int(l[j])-1)

            final_nums = int(len(all_num_list)/len(text))

            for n in all_num_list[0:final_nums]:
                excrypted_list.append(st.printable[n])

            for a in excrypted_list:
                print(str(a),end='')

    def main():
        text = str(input("Enter a String to Encrypt: "))
        Encrypter.setting1(text)

class Decrypter:
    def setting1(text):
        if text == '':
            print("Please Try again!!")
            text = str(input("Enter a String to Encrypt: "))
            Encrypter.setting1(text)

        else:
            l = []
            excrypted_list = []
            all_num_list = []
            print("Ignore the Square Brackets\n")
            for char in text:
                for x in range(0,len(st.printable)):  
                    if char == st.printable[x]:
                        l.append(x)

            for b in l: 
                for j in range(0,len(l)):
                    if j%2==0:
                        all_num_list.append(int(l[j])-1)
                    elif j%2==1:
                        all_num_list.append(int(l[j])+1)

            final_nums = int(len(all_num_list)/len(text))

            for n in all_num_list[0:final_nums]:
                excrypted_list.append(st.printable[n])

            for a in excrypted_list:
                print(str(a),end='')

    def main():
        text = str(input("Enter a String to Decrypt: "))
        Decrypter.setting1(text)

ask_option = str(input("What do you want to do with this encrypter-decrypter app. \nEnter e for Encrypting a string and d to decrypt:\n "))

while ask_option.lower() != '':

    if ask_option.lower() == "e":
        Encrypter.main()
        ask_option = str(input("\n\nWhat do you want to do with this encrypter-decrypter app. \nEnter e for Encrypting a string and d to decrypt:\n "))

    elif ask_option.lower() == "d":
        Decrypter.main()
        ask_option = str(input("\n\nWhat do you want to do with this encrypter-decrypter app. \nEnter e for Encrypting a string and d to decrypt:\n "))

    else:
        print("error: ")
        ask_option = str(input("\n\nWhat do you want to do with this encrypter-decrypter app. \nEnter e for Encrypting a string and d to decrypt:\n "))