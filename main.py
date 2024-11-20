import pandas as pd
import matplotlib.pyplot as plt

def load_from_csv(file_csv):
    try:
        df = pd.read_csv(file_csv)
        return df
    except FileNotFoundError:
        print("Файл не знайдено.")
    except Exception as e:
        print(f"Помилка: {e}")

def save_to_csv(file_csv, df):
    try:
        df.to_csv(file_csv, index=False)
    except Exception as e:
        print(f"Помилка: {e}")


def add_order(df, name, number, data, sum_or, status):
    new_order = {"Ім'я клієнта": name, "Номер замовлення": number, "Дата замовлення": data, "Сума замовлення": sum_or, "Статус": status}
    df = df._append(new_order, ignore_index=True)
    return df

def edit_order(df, name, new_df):
    if name in df["Ім'я клієнта"].values:
        df.loc[df["Ім'я клієнта"] == name, list(new_df.key())] = list(new_df.values())
        return df
    else:
        print("Клієнта не знайдено")
        return df


def delete_order(df, name):
    if name in df["Ім'я клієнта"].values:
        return df.loc[df["Ім'я клієнта"] != name]
    else:
        print("Клієнта не знайдено")
        return df


def display_order(df):
    print(df)



def analyze_orders(orders):
    total_orders = len(orders)
    total_sum = orders['Сума замовлення'].sum()
    print(f"Загальна кількість замовлень: {total_orders}")
    print(f"Сумарна вартість замовлень: {total_sum:.2f} грн")

    status_counts = orders['Статус'].value_counts()
    print("\nКількість замовлень за статусом:")
    print(status_counts)

    max_order = orders.loc[orders['Сума замовлення'].idxmax()]
    print(f"\nЗамовлення з найбільшою сумою:\n{max_order}")


def visualize_orders(orders):
    status_counts = orders['Статус'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("Частка виконаних і невиконаних замовлень")
    plt.show()

    orders['Дата замовлення'] = pd.to_datetime(orders['Дата замовлення'])
    plt.figure(figsize=(10, 6))
    plt.hist(orders['Дата замовлення'].dt.date, bins=10, kde=False)
    plt.title("Кількість замовлень за датами")
    plt.xlabel("Дата")
    plt.ylabel("Кількість замовлень")
    plt.xticks(rotation=45)
    plt.show()



def menu():
    print('-'*25, "Меню", '-'*25)
    print("1. Завантажити файл")
    print("2. Додати нове замовлення")
    print("3. Оновити замовлення")
    print("4. Видалити замовлення")
    print("5. Показати всі замовлення")
    print("6. Аналіз замовлень")
    print("0. Вийти")

    while True:
        choice = input("Виберіть опцію: ")

        if choice == '1':
            file = input("Введіть назву файлу: ")
            df = load_from_csv(file)

            if df is not None:
                print("Файл успішно додано")
            else:
                print("Помилка")

        elif choice == '2':
            name = input("Введіть ім'я: ")
            try:
                number = int(input("Введіть номер замовлення: "))
            except ValueError as e:
                print(f"Помилка: {e}")
                continue
            data = input("Введіть дату замовлення: ")
            try:
                sum_ord = float(input("Введіть суму замовлення: "))
            except ValueError as e:
                print(f"Помилка: {e}")
                continue
            status = input("Введіть статус: ")
            if status not in ['Виконано', 'В процесі']:
                print("Неправильний ввід")
                continue
            df = add_order(df, name, number, data, sum_ord, status)
            print("Продукт додано")





if __name__ == '__main__':
    menu()
