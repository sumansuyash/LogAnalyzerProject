import pandas as pd
import os
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

logFiles = []

def analyze_logFile(filePath):
    # Use a breakpoint in the code line below to debug your script.
    print(f'\n********Analyzing {filePath}**********\n')  # Press Ctrl+F8 to toggle the breakpoint.

    df = pd.read_csv(filePath, sep='[||]', delimiter=None, header=None, engine='python')
    df = df.dropna(axis='columns')
    df.columns = range(df.shape[1])
    df = df.iloc[:, :-1]
    #print(df.info)

    df.columns = ['Time', 'Type', 'A', 'Service', 'B', 'ExceptionType']
    df['Time'] = df['Time'].astype('datetime64[ns]')
    df2 = df[df.iloc[:, -1].str.contains("Exception")]

    #df2['Time'] = pd.to_datetime(df2['Time'])

    df2 = df2.sort_values('Time')

    df2['ExceptionType']= [x.split(':')[0] for x in df2['ExceptionType'].to_list()]

    df3 = df2.groupby('ExceptionType')
    print(df3.size()) #Exception Count
    print(df3.groups) #Exception Position

    #print(df2.loc[9859,:])
    #print(df3.get_group(' ExceptionA '))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    for root, dirs, files in os.walk("C:\\Users\\Dunzen\\Desktop\\Task1"):
        for file in files:
            if file.__eq__('dataset.txt'):
                logFiles.append(os.path.join(root, file))
    print(logFiles)

    for file in logFiles:
        analyze_logFile(file)
