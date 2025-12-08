import pandas as pd
from tabulate import tabulate



def table_head():
    head=[] #['название 1', 'название 2', ....]
    column_number = 1
    while True:
        if column_number > 2:
            answer = input('Хотите больше колонок? Да/Нет')
            if answer.lower() == "да":
                pass
            elif answer.lower() == 'нет':
                break
        head.append(input(f'Введите название колонки {column_number} - '))
        column_number+=1
    return head

def table_body(head_length):
    body = []
    rows_number = 1
    while True:
        if rows_number > 2:
            answer = input('Хотите больше строк? Да/Нет')
            if answer.lower() == "да":
                pass
            elif answer.lower() == "нет":
                break
        row = []
        print(f'Кол-во строк: {rows_number}')

        for i in range(head_length):
            row.append(input(f'Введите значение ячейки {i+1} - '))
        body.append(row)
        rows_number+=1
    return body
def main():
    head=table_head()
    body=table_body(len(head))

    table = pd.DataFrame(body, columns=head)
    table.to_csv()
    print(tabulate(table, showindex=False, headers=head))


if __name__ == "__main__":
    main()
