#importing all libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#loading dataset
df= pd.read_csv(r'C:\Users\Tanvi Khadatkar\Documents\banking_dataset.csv',encoding='unicode escape')

#number of rows and columns
shape=df.shape
print("The number of rows and columns-",shape)

#examining data briefly
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
#printing distribution of all numeric columns briefly
overview=df.describe()
print("A brief overview of distribution of all numerical columns-\n ",overview)

#creating function for histogram
def histogram(df, column, xlabel, ylabel, title, binwidth, color): 
    try: 
        sns.displot(df[column], binwidth=binwidth, color=color)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.show()
    except Exception  as e:
        print(f"An error occured while plotting histogram graph {e}")
        
    
#creating function for barplot
def barplot(df, column, xlabel, ylabel, title, color):
    value_counts = df[column].value_counts()
    try: 
        plt.bar(value_counts.index, value_counts.values, color=color)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(rotation='vertical')
        plt.show()
    except Exception as e:
        print(f"An error occured while plotting bar graph {e}")
        
   
#creating function for boxplot
def boxplot(df,column,title):
    try:
        sns.boxplot(y=column,data=df)
        plt.title(title)
        plt.show()
    except Exception as e:
        print(f"An error occured while plotting box graph {e}")
        
        
  
    

#-	What is the distribution of age among the clients?
histogram(df,'age','Age','Number of clients',"Age Distribution",None,"cyan")
print("Some statistical insight into the distribution of age in clients-\n")
age_stats=df['age'].describe()
print(age_stats)

#-	How does the job type vary among the clients?
job_variance=df['job'].value_counts()
print(f"The job type among clients varies as- \n {job_variance}")
barplot(df,'job',"Job Type","Frequency","Job Variance","purple")

#dropping redundant column marital_status
df.drop(columns=['marital_status'],inplace=True)

#-	What is the marital status distribution of the clients?
marital_status=df['marital'].value_counts()
print(f"The marital distribution among clients is\n{marital_status}")
#dropping rows with missing values
df.dropna(subset=['marital'],inplace=True)
barplot(df,'marital',"Marital Status","Count","Marital Status Distribution","green")
#-	What is the level of education among the clients?
#dropping rows with missing values
df.dropna(subset=['education'],inplace=True)

education_status=df['education'].value_counts()
print(f"The level of education among clients varies as \n{education_status}\n")
from collections import Counter 
edu_dict=Counter(df['education'])
plt.pie(edu_dict.values(), labels = edu_dict.keys(), startangle = 90)
plt.title("Level of Education")
plt.show()

#-	What proportion of clients have credit in default?
df['default']=df['default'].replace({'yes':1,'no':0})
default_status=df['default'].value_counts(1).get(1,0)
pd.set_option('future.no_silent_downcasting', True)
print(f"The proportion of clients who have credit in default is {default_status}.\n")


#-	What is the distribution of average yearly balance among the clients?
print("Numerical display of distribution of average yearly balance amongst clients/n")
balance_stats=df['balance'].describe()
print(balance_stats)
boxplot(df,'balance','Box plot of average yearly balance')
#-	How many clients have housing loans?
df['housing']=df['housing'].replace({'yes':1,'no':0})
houseloan_status=df['housing'].value_counts().get(1,0)
print(f"The number of clients who have housing loan is {houseloan_status}.\n")

#How many clients have personal loans?
df['loan']=df['loan'].replace({'yes':1,'no':0})
personal_loan_status=df['loan'].value_counts().get(1,0)
print(f"The number of clients who have personal loan is {personal_loan_status}.\n")

#-	What are the communication types used for contacting clients during the campaign?
contact_type_status=df['contact'].value_counts()
print(f"The various communication types used for contacting clients during the campaign are {contact_type_status}")
from collections import Counter 
contact_dict=Counter(df['contact'])
plt.pie(contact_dict.values(), labels = contact_dict.keys(), startangle = 90)
plt.title("Communication Types")
plt.show()

#-	What is the distribution of the last contact day of the month?
print("Numerical display of distribution of last contact day of the month with clients/n")
lastdaycontact=df['day'].describe()
print(lastdaycontact)
boxplot(df,'day','Box plot of last contact day of month')


#-	How does the last contact month vary among the clients?
month_status=df['month'].value_counts()
print(f"The last contact month varies among clients as\n{month_status}")
barplot(df,'month',"Month","Count","Last Contact Month","olive")

#-	What is the distribution of the duration of the last contact?
boxplot(df,'duration',"Box plot of duration of last contact")
print("Numerical representation of the distribution of duration of last contact in clients-\n")
duration_stats=df['duration'].describe()
print(duration_stats)

#-	How many contacts were performed during the campaign for each client?
contacts_no_status=df['campaign'].value_counts()
print(f"The number of contacts for this campaign varies among clients as\n{contacts_no_status}")
histogram(df,'campaign',"Number of contacts","Frequency","No. of contacts current campaign",4,"coral")

#-	What is the distribution of the number of days passed since the client was last contacted from a previous campaign?
print("Numerical display of distribution of days passed since last contact from a previous campaign/n")
pdays_stats=df['pdays'].describe()
print(pdays_stats)
histogram(df,'pdays',"Days passed","Frequency","Days passed since last contact from previous campaign",None,'navy')

#-	How many contacts were performed before the current campaign for each client?
print("Numerical representation of the distribution of duration of number of contacts before current campaign-\n")
previous_stats=df['previous'].describe()
print(previous_stats)
previous_status=df['previous'].value_counts()
print(previous_status)
boxplot(df,'previous','Box plot of contacts prior current campaign')
#-	What were the outcomes of the previous marketing campaigns?

outcome_status=df['poutcome'].value_counts()
print("The overview of the outcome of the previous campaigns is",outcome_status)
barplot(df,'poutcome',"Outcome Status","Occurences","Previous Campaign Outcome","orange")

#-	What is the distribution of clients who subscribed to a term deposit vs. those who did not?
term_deposit=df['y'].value_counts()
print("The distribution of clients who subscribed to a term deposit vs. those who did not is-",term_deposit)
df.rename(columns={'y':'term_deposit'},inplace=True)
barplot(df,'term_deposit',"Status of Subscription","Count","Term Deposit Subscription","grey")
df['term_deposit']=df['term_deposit'].replace({'yes':1,'no':0})

#converting data type object to numeric int
df['default'] = pd.to_numeric(df['default'], errors='coerce')
df['housing'] = pd.to_numeric(df['housing'], errors='coerce')
df['loan'] = pd.to_numeric(df['loan'], errors='coerce')
df['term_deposit'] = pd.to_numeric(df['term_deposit'], errors='coerce')

#-	Are there any correlations between different attributes and the likelihood of subscribing to a term deposit?
numeric_df=df.select_dtypes(include=['int64','float64'])
corr_matrix=numeric_df.corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr_matrix,annot=True,cmap="YlOrRd",fmt='.2f')
plt.title('Correlation Matrix')
plt.show()

