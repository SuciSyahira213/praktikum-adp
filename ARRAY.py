# Masukkan Rumus Rummus yang akan di gunakan yaitu f(x), g(x), dan h(x)
def f(x):
    if x >= 0:
        return 4*x**3 + 7*x - 5
    else:
        return 3*x**2 - 5*x + 1

def g(x):
    return (f(x)**2) - f(x)

def h(x):
    return f(x) * g(x)


# Code untuk melakukan perulangan input range n
def main():
    n = int(input("Input banyak data n: "))
    results = []
    
    for i in range(n):
        x = float(input(f"Input x ke {i + 1}: "))
        fx = f(x)
        gx = g(x)
        hx = h(x)
        results.append((i + 1, x, fx, gx, hx))
    
    print("\nOutput:")
    print("No |   x   |  f(x)  |  g(x)  |  h(x)")
    print("-----------------------------------------")
    for result in results:
        print(f"{result[0]:<3} | {result[1]:<5} | {result[2]:<6} | {result[3]:<6} | {result[4]:<6}")


    # Menanyakan input nilai x lagi
    while True:
        lagi = input("Input nilai x lagi? (Y/N): ").strip().upper()
        if lagi == 'Y':
            x_lagi = float(input("Input x: "))
            fx_lagi = f(x_lagi)
            gx_lagi = g(x_lagi)
            hx_lagi = h(x_lagi)
            print(f"\nHasil untuk x = {x_lagi}:")
            print(f"f(x) = {fx_lagi}, g(x) = {gx_lagi}, h(x) = {hx_lagi}")
        elif lagi == 'N':
            print("Terima kasih!")
            break
        else:
            print("Input tidak valid, silakan masukkan Y atau N.")
    
#Jalankan
main()