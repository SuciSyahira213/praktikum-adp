while True:
    password = input("Masukkan password: ")

    if len(password) < 8:
        print("Password minimal 8 karakter!\n")

    elif not any("a" <= c <= "z" for c in password):
        print("Password harus mengandung huruf kecil!\n")

    elif not any("A" <= c <= "Z" for c in password):
        print("Password harus mengandung huruf besar!\n")

    elif not any("0" <= c <= "9" for c in password):
        print("Password harus mengandung angka!\n")

    elif not any(c in "!@#$%^&*()_-+=[]{}|;:'\",.<>?/`~" for c in password):
        print("Password harus mengandung minimal 1 karakter khusus!\n")

    else:
        print("Password Valid! Selamat!\n")
        break