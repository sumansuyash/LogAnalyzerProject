import pandas as pd
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def analyze_logFile():
    # Use a breakpoint in the code line below to debug your script.
    print(f'Analyzing dataset.txt....')  # Press Ctrl+F8 to toggle the breakpoint.

    df = pd.read_csv('dataset.txt', sep='[||]', delimiter=None, header=None, engine='python')
    df = df.dropna(axis='columns')
    df.columns = range(df.shape[1])
    df = df.iloc[:, :-1]
    #print(df.info)

    df.columns = ['Time', 'Type', 'A', 'Service', 'B', 'ExceptionType']
    df2 = df[df.iloc[:, -1].str.contains("Exception")]
    #print(df2)

    df2['Time'] = pd.to_datetime(df2['Time'])
    #print(df2)

    df2 = df2.sort_values('Time')
    #print(df2)

    df3 = df2.groupby('ExceptionType')
    print(df3.size()) #Exception Count
    print(df3.groups) #Exception Position

    #print(df2.loc[9859,:])
    #print(df3.get_group(' ExceptionA '))
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    analyze_logFile()
