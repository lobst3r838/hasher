import hashlib
import argparse
import os


def check_functions(f):
    algorithms = ["MD5", "SHA1", "SHA224", "SHA256", "SHA384", "SHA512", "SHA3_224", "SHA3_256", "SHA3_384", "SHA3_512"]
    return True if f in algorithms else False


def enc_string(string, func):
    if func == "MD5":
        return hashlib.md5(string.encode()).hexdigest()
    elif func == "SHA1":
        return hashlib.sha1(string.encode()).hexdigest()
    elif func == "SHA224":
        return hashlib.sha224(string.encode()).hexdigest()
    elif func == "SHA256":
        return hashlib.sha256(string.encode()).hexdigest()
    elif func == "SHA384":
       return hashlib.sha384(string.encode()).hexdigest()
    elif func == "SHA512":
        return hashlib.sha512(string.encode()).hexdigest() 
    elif func == "SHA3_224":
        return hashlib.sha3_224(string.encode()).hexdigest() 
    elif func == "SHA3_256":
        return hashlib.sha3_256(string.encode()).hexdigest() 
    elif func == "SHA3_384":
        return hashlib.sha3_384(string.encode()).hexdigest() 
    elif func == "SHA3_512":
        return hashlib.sha3_512(string.encode()).hexdigest() 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dictionary", help="Input dictionary file", required=True)
    parser.add_argument("-f", "--function", help="Hash function. Choose one of these: MD5, SHA1, SHA224, SHA256, SHA384, SHA512, SHA3_224, SHA3_256, SHA3_384, SHA3_512", required=True)
    args = vars(parser.parse_args())
    
    dictionary = args["dictionary"]
    function = args["function"].upper()

    if check_functions(function):
        if os.path.isfile(dictionary):
            new_dict = os.path.splitext(dictionary)[0] + f"_{function}" + os.path.splitext(dictionary)[1]
            with open(new_dict, "w") as file_out:
                with open(dictionary, "r") as file_in:
                    for line in file_in.readlines():
                        digest = enc_string(line.strip(), function)
                        file_out.writelines(line.rstrip("\n") + ":" + digest + "\n")
        else:
            print(f"\n[ERRORE] File {dictionary} non trovato")
    else:
        print("\n [ERRORE] Funzione non trovata")