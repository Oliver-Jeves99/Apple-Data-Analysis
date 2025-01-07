import pandas as pd
import numpy 

age = float(input("What is your age?"))

highest_heart_rate = 208 - (age * 0.7) 

# Needs to a raw string due to backslash
## Forgot to add index_col=False and confused me for a while 

df = pd.read_csv(r"C:\Users\Oliver\OneDrive\Documents\Apple Watch Data/General Health Data.csv",index_col=False) 

## needed troubleshooting
print(df['Active Energy (kJ)'].dtype)
print(df['Active Energy (kJ)'].isna().sum())  
print(df['Active Energy (kJ)'].unique())


print(df['Active Energy (kJ)'])
df = df.dropna(subset = ['Active Energy (kJ)'])

# need to change to kcal
df['Active Energy (kJ)'] = df['Active Energy (kJ)'] / 4.184

print(df)

## need to remove today ## I find this is the wrong way of doing it after this
cals_burned = df.drop(df.index[-1])['Active Energy (kJ)'].mean()
cals_burned = round(cals_burned, 2)


## Mistake here, this is removing the null bottom row and then removing the NOT null bottom row
df = df.dropna(subset = ['Apple Exercise Time (min)'])
## exercise_mins = df.drop(df.index[-1])['Apple Exercise Time (min)'].mean() not needed
exercise_mins = df['Apple Exercise Time (min)'].mean()

exercise_mins = round(exercise_mins, 2)

################ Moving forward I will just be removing the bottom row from the DF


## dropped it ## 
df.drop(df.index[-1])
print(df)

################

##this will be averageing an average, which normally is not a good idea. But works in this case
heart_rate_avg = df['Heart Rate [Avg] (bpm)'].mean()

heart_rate_avg = round(heart_rate_avg, 2)

max_heart_rate = df ['Heart Rate [Max] (bpm)'].max()
differnt_in_maxes = highest_heart_rate - max_heart_rate
differnt_in_maxes = round(differnt_in_maxes, 2)


print("Average Kcals burned per day:" + " " + str(cals_burned))
print("Average minutes spent exercising per day:" + " " + str(exercise_mins))
print("")


print(differnt_in_maxes)
print(highest_heart_rate)

print("Average Daily Heart Rate:" + " " + str(heart_rate_avg) + " BPM") 
if differnt_in_maxes > 0:
    print("And your max heart rate was:" + " " + str(max_heart_rate)+ " BPM" + " which is " + str(differnt_in_maxes) + " BPM away from the max for your age")
elif differnt_in_maxes < 0:
    print("And your max heart rate was:" + " " + str(max_heart_rate)+ " BPM" + " which is " + str(abs(differnt_in_maxes)) + " BPM over the max for your age")
else:
    print("And your max heart rate was:" + " " + str(max_heart_rate)+ " BPM" + " which is the same as the max for your age!!")
    