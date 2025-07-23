import hashlib
# Used for Educational Purposes ONLY
# Followed a tutorial by Brandon Jacobson on Youtube
# https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/Ashley-Madison.txt

pass_filename = r"C:\Users\Trini\CyAnProjects\PasswordProjects\Ashley-Madison.txt"

password = "booomer"

enc_password = password.encode("utf-8")
password_hash = hashlib.md5(enc_password.strip()).hexdigest()

pass_file = open(pass_filename, "r")

for word in pass_file:
    enc_word = word.encode("utf-8")
    enc_hash = hashlib.md5(enc_word.strip()).hexdigest()

    if password_hash == enc_hash:
        print("This three-letter agency has been hacked. The password was " + word)
        quit()

print("The three letter agency has a strong password.")