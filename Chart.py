import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def all_in_one(data):
    sns.set(style="whitegrid")
    data.plot(x='Date', y=['Surface Temp', 'Wind Speed', 'Pressure'])
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel('Value', fontsize=12, fontweight='bold')
    plt.title('All Details', fontsize=14, fontweight='bold')
    plt.legend()
    plt.tight_layout()
    plt.show()


def diff_graph(data):
    sns.set(style="whitegrid")
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(10, 8))

    plt.suptitle('All details in different  graphs ', fontsize=14, fontweight='bold')

    ax1.plot(data['Date'], data['Surface Temp'], color='b', label='Surface Temp')
    ax1.set_ylabel('Surface Temp', fontsize=12, fontweight='bold')
    ax1.legend()

    ax2.plot(data['Date'], data['Wind Speed'], color='g', label='Wind Speed')
    ax2.set_ylabel('Wind Speed', fontsize=12, fontweight='bold')
    ax2.legend()

    ax3.plot(data['Date'], data['Pressure'], color='r', label='Pressure')
    ax3.set_xlabel('Date', fontsize=12, fontweight='bold')
    ax3.set_ylabel('Pressure', fontsize=12, fontweight='bold')
    ax3.legend()

    x_ticks = data['Date'][::5]
    plt.xticks(x_ticks, rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


def single_graph(data, column_name):
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data[column_name])
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel(column_name, fontsize=12, fontweight='bold')
    plt.title(f'{column_name} Graph', fontsize=14, fontweight='bold')

    x_ticks = data['Date'][::10]
    plt.xticks(x_ticks, rotation=45)
    plt.tight_layout()
    plt.show()


def main():
    data = pd.read_csv("cleaned_data.csv")
    print("1. All details in one graph")
    print("2. All details in different graphs")
    print("3. Specific graph")

    graph = int(input("Enter Number: "))
    clear_screen()

    if graph == 1:
        all_in_one(data)
    elif graph == 2:
        diff_graph(data)
    elif graph == 3:
        print("1. Surface Temp Graph")
        print("2. Wind Speed Graph")
        print("3. Pressure Graph")
        graph_type = int(input("Enter Number: "))
        clear_screen()

        if graph_type == 1:
            single_graph(data, 'Surface Temp')
        elif graph_type == 2:
            single_graph(data, 'Wind Speed')
        elif graph_type == 3:
            single_graph(data, 'Pressure')


if __name__ == "__main__":
    main()
