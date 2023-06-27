import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter

import scipy

f_enum = {
    "Ensino médio completo": 0,
    "Ensino médio incompleto": 1,
    "Ensino superior completo": 2,
    "Ensino superior incompleto": 3,

}

s_enum ={
    "inadimplente": 0,
    "adimplente": 1
}

def main():

    df = load_df()
    print_res_c(df)
    print_res_d(df)
    plot(df)

    
    
def print_res_c(df):
    print("===== C =====")
    print_var(df, "Idade")
    print_var(df, "Número de filhos")
    print_var(df, "Salários")
    print_var(df, "Anos na seguradora")
    print_var(df, "Custos do conserto")

def print_var(df, column_name):
    print(f"{column_name}:")
    print(f'Desvio-padrão           -> {df.loc[:, column_name].std()}')
    print(f'Média                   -> {df.loc[:, column_name].mean()}')
    print(f'Desvio médio            -> {np.mean(np.absolute(df.loc[:, column_name] - df.loc[:, column_name].mean()))}')
    ax = df.loc[:, column_name].std()/df.loc[:, column_name].mean()
    print(f'Coeficiente de variação -> {ax}')
    print()

def print_res_d(df):
    print("===== D =====")

    df_adi = df[df["Situação"] == 1]
    df_ina = df[df["Situação"] == 0]

    med_adi = df_adi["Salários"].mean()
    med_ina = df_ina["Salários"].mean()

    coe_var_adi = df_adi["Salários"].std()/med_adi
    coe_var_ina = df_ina["Salários"].std()/med_ina

    print(f"Média salarial adimplentes   -> {med_adi}")
    print(f"Média salarial inadimplentes -> {med_ina}")
    print()
    print(f"Coeficiente de variação adimplentes   -> {coe_var_adi}")
    print(f"Coeficiente de variação inadimplentes -> {coe_var_ina}")

def load_df():
    df = pd.read_excel('P_enviada.xlsx')

    for column_name in df.columns:
        match column_name:
            case "Situação":
                to_bool(df, column_name)
            case "Formação":
                to_enum(df, column_name, f_enum)
            case "Motorista de aplicativo":
                to_bool(df, column_name)
            case "Sinistros":
                to_bool(df, column_name)
    
    return df

def plot(df):
    fig, axs = plt.subplots(3, 3)

    axs[0][0].set_title("Situação")
    set_pie(df, "Situação", s_enum, axs[0][0])

    axs[0][1].set_title("Formação")
    set_pie(df, "Formação", f_enum, axs[0][1])

    axs[0][2].set_title("Idade")
    set_hist(df, "Idade", axs[0][2])

    axs[1][0].set_title("Número de filhos")
    set_hist(df, "Número de filhos", axs[1][0])
    
    axs[1][1].set_title("Salários")
    set_hist(df, "Salários", axs[1][1])
    
    axs[1][2].set_title("Anos na seguradora")
    set_hist(df, "Anos na seguradora", axs[1][2])
    
    axs[2][0].set_title("Motorista de aplicativo")
    set_pie(df, "Motorista de aplicativo", {'Sim': 1, 'Não': 0}, axs[2][0])
    
    axs[2][1].set_title("Sinistros")
    set_pie(df, "Sinistros", {'Sim': 1, 'Não': 0, "Não se sabe":2}, axs[2][1])
    
    axs[2][2].set_title("Custos do conserto")
    set_hist(df, "Custos do conserto", axs[2][2])

    plt.show()

def set_pie(df, column_name, enum, ax):
    my_dict = Counter(df[column_name])
    counter = len(df[column_name])
    inv_enum = {v: k for k, v in enum.items()}
    ax.pie(my_dict.values(), labels=[f"{inv_enum[x]} ({100*my_dict[x]/counter})%" for x in my_dict.keys()])

def set_hist(df, column_name, ax):
    ax.hist(df[column_name])
    ax.set_ylabel("Número de pessoas")

def to_bool(df, column_name):
    for line, item in enumerate(df[column_name]):
        if pd.isna(item):
            df.loc[line, column_name] = 2
            continue
        
        df.loc[line, column_name] = 0 if "0" in item else 1

def to_enum(df, column_name, enum):

    for line, item in enumerate(df[column_name]):
        if not pd.isna(item):
            df.loc[line, column_name] = enum[item]

if __name__ == "__main__":
    main()