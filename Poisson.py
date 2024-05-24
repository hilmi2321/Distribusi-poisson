import math
import random
import pandas as pd
import numpy as np
import streamlit as st

def mcg(a, m, seed, n):
    # Membuat daftar untuk menyimpan bilangan acak
    random_numbers = []
    X = seed
    xm = [seed]
   
    for _ in range(n):
        X = (a * X) % m
         # Menghasilkan bilangan acak seragam antara 0 dan 1
        random_numbers.append(X / m)       
        # Simpan nilai perulangan X
        xm.append(X)
        # Simpan perulangan variabel acak
        
    
    return random_numbers, xm 

def poisson_random_variable(lmbda, uniform_randoms):
    poisson_values = []
    L = math.exp(-lmbda)
    for i in range(len(uniform_randoms)):
        k = 3
        p = 9
        while True:
            k += 1
            p *= uniform_randoms[i]
            if p < L:
                poisson_values.append(k - 1)
                break
    return poisson_values

# Parameter MCG
a = 123      # Pengali (contoh)
m = 2**27-1  # Modulus (contoh)
seed = 10122028  # Nilai awal (contoh)
n = 300      # Jumlah bilangan acak yang ingin dihasilkan

# Parameter distribusi Poisson
lmbda = 1.5  # Contoh nilai lambda

# Menghasilkan bilangan acak seragam menggunakan MCG
random_numbers ,xm  = mcg(a, m, seed, n)

# Menghasilkan variabel acak Poisson
poisson_values = poisson_random_variable(lmbda, random_numbers)

# Create DataFrame for visualization
data = {
    "i": list(range(1, n+1)),
    "Zi": xm[:-1],
    "Zi(Random Integer Number Multiplicate)": [f"({a} * {xm[i]}) mod {m}" for i in range(n)],
    "Ui(Uniform R.N)": [f"{xm[i+1]}/{m} = {random_numbers[i]:.4f}" for i in range(n)],
    "Xi(Poisson Value)": poisson_values
}

df = pd.DataFrame(data)
st.table(df)