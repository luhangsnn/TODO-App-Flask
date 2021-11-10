import pygsheets
import pandas as pd

#authorization
gc = pygsheets.authorize(service_file='./cs321-proj3-27cd9b62ae97.json')

# sample_list = [{'content': 'hHHHw', 'priority': 'High', 'tags': '#family #research', 'time': '2021-11-10, 00:38', 'due_date': '2021-11-03', 'id': 'hw0'}, {'content': 'sad', 'priority': 'Medium', 'tags': '#sda', 'time': '2021-11-10, 00:39', 'due_date': '2021-11-11', 'id': 'sad0'}]

def todolist_to_pd(to_do_list):
    '''takes in the to-do list dictionary from the main app file 
    and converts into pd'''
    df = pd.DataFrame.from_dict(to_do_list)
    df.drop("id", axis=1, inplace=True)

    df.columns = ["to-do", "priority", "tags", "time added", "due date"]
    return df

def to_gsheets(df):
    '''output dataframe into google spreadsheet'''
    sh = gc.open("CS321 project 3 To-do list")
    worksheet = sh[0]
    worksheet.clear()
    worksheet.set_dataframe(df, (1,1))

if __name__ == "__main__":
    df = todolist_to_pd(sample_list)
    to_gsheets(df)
