import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import datetime

def generate_date_sequence(start_date_YYYYMMDD,num_days,cadence):

    start_date = datetime.datetime.strptime(start_date_YYYYMMDD,'%Y%m%d')
    end_date = start_date + datetime.timedelta(days=num_days)

    if cadence.lower() == "daily":
        return_series = pd.date_range(start_date,end_date,freq='D')
    elif cadence.lower() == "weekly":
        return_series = pd.date_range(start_date,end_date,freq='W')
    elif cadence.lower() == "biweekly":
        return_series = pd.date_range(start_date,end_date,freq='2W')
    elif cadence.lower() == "monthly":
        return_series = pd.date_range(start_date,end_date,freq='M')
    elif cadence.lower() == "quarterly":
        return_series = pd.date_range(start_date,end_date,freq='Q')
    elif cadence.lower() == "yearly":
        return_series = pd.date_range(start_date,end_date,freq='Y')

    return return_series

class ExpenseForecast:

    def __init__(self):

        #TODO assert consistency between accountset and budgetset

        pass

    def satisfice(self, budget_schedule_df, account_set_df):

        priority_1_budget_schedule_df = budget_schedule_df.loc[budget_schedule_df.Priority == 1, :]

        min_sched_date = min(budget_schedule_df.Date)
        max_sched_date = max(budget_schedule_df.Date)

        all_days = pd.date_range(min_sched_date, max_sched_date)

        date_only_df = pd.DataFrame(['Date',min_sched_date]).T

        accounts_only_df = pd.DataFrame( account_set_df.iloc[:,0:1] ).T
        accounts_only_df.reset_index(inplace=True,drop=True)
        accounts_only_df.columns = accounts_only_df.iloc[0]


        starting_zero_balances_df = pd.DataFrame([0]*account_set_df.shape[0]).T
        starting_zero_balances_df.reset_index(inplace=True,drop=True)
        starting_zero_balances_df.columns = accounts_only_df.iloc[0]

        accounts_only_df = pd.concat([accounts_only_df,starting_zero_balances_df]).T
        accounts_only_df.reset_index(drop=True,inplace=True)
        accounts_only_df.columns = [0,1]

        memo_only_df = pd.DataFrame(['Memo','']).T

        forecast_df = pd.concat([
            date_only_df,
            accounts_only_df,
            memo_only_df
            ])

        forecast_df = forecast_df.T
        forecast_df.columns = forecast_df.iloc[0,:]
        forecast_df = forecast_df[1:]
        forecast_df.reset_index(drop=True,inplace=True)

        #set initial values
        for i in range(0,account_set_df.shape[0]):
            row = account_set_df.iloc[i,:]
            forecast_df.iloc[0, 1 + i] = row.Balance


        for d in all_days:
            if d == forecast_df.iloc[0,0]:
                previous_date = d
                continue #we consider the starting balances finalized
            new_row_df = forecast_df[forecast_df.Date == previous_date].copy()
            new_row_df.Date = d

            relevant_budget_items_df = priority_1_budget_schedule_df.loc[ d == priority_1_budget_schedule_df.Date, : ]
            relevant_budget_items_df.sort_values(inplace=True, axis=0, by="Amount",ascending=False)

            # todo interest accruals. shouldnt happen every day as it does ats it is currently implemented
            for index, row in account_set_df.iterrows():
                index_of_relevant_column_balance = list(new_row_df.columns).index(row.Name)

                if row['APR'] == 0:
                    continue

                #todo if not an interest accrual day, continue

                days_since_billing_start_date = (d - row['Billing_Start_Dt']).days


                relevant_apr = row['APR']
                relevant_balance = new_row_df.iloc[0,index_of_relevant_column_balance]
                if row['Interest_Cadence'].lower() == 'daily':
                    new_balance = relevant_balance + ( relevant_balance * relevant_apr ) / 365.25
                elif row['Interest_Cadence'].lower() == 'monthly':

                    interest_accrual_days = generate_date_sequence(row['Billing_Start_Dt'].strftime('%Y%m%d'), days_since_billing_start_date + 10, 'monthly')
                    if d in interest_accrual_days:
                        new_balance = relevant_balance + ( relevant_balance * relevant_apr) / 30
                    else:
                        new_balance = relevant_balance
                elif row['Interest_Cadence'].lower() == 'yearly':
                    interest_accrual_days = generate_date_sequence(row['Billing_Start_Dt'].strftime('%Y%m%d'),
                                                                   days_since_billing_start_date + 10, 'yearly')
                    if d in interest_accrual_days:
                        new_balance = relevant_balance + (relevant_balance * relevant_apr)
                    else:
                        new_balance = relevant_balance
                else:
                    print('Undefined case in satisfice()')

                #print(str(d)+' Updating balance '+str(row.Name)+' '+str(relevant_balance)+' -> '+str(new_balance))
                new_row_df.iloc[0, index_of_relevant_column_balance] = new_balance

            #todo execute non-neogtiable transactions
            for budget_item in relevant_budget_items_df:
                #todo account selection HAS to depend on priority.
                pass

            previous_date = d
            forecast_df = pd.concat([forecast_df,new_row_df])


        updated_budget_schedule_df = budget_schedule_df.loc[budget_schedule_df.Priority != 1,:]
        updated_budget_schedule_df.sort_values(inplace=True, axis=0, by="Date")
        updated_budget_schedule_df.reset_index(inplace=True, drop=True)

        #account_set_df is returned unchanged. we depend on optimize logic to not violate boundaries by checking the forecast
        return [updated_budget_schedule_df, account_set_df, forecast_df]

    def optimize_next_choice(self,updated_budget_schedule_df,account_set_df,forecast_df):

        updated_account_set_df = account_set_df
        updated_forecast_df = forecast_df




        updated_budget_schedule_df.sort_values(inplace=True, axis=0, by="Date")
        updated_budget_schedule_df.reset_index(inplace=True, drop=True)

        return [updated_budget_schedule_df,account_set_df,forecast_df]



    def computeForecast(self,forecast_df):
        figure(figsize=(8, 6), dpi=80)
        for i in range(1,forecast_df.shape[1]-1):
            plt.plot(forecast_df['Date'], forecast_df.iloc[:,i],label=forecast_df.columns[i])

        ax = plt.subplot(111)
        box = ax.get_position()
        ax.set_position([box.x0, box.y0 + box.height * 0.1,
                         box.width, box.height * 0.9])

        # Put a legend below current axis
        ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
                  fancybox=True, shadow=True, ncol=2)

        #TODO a large number of accounts will require some adjustment here so that the legend is entirely visible

        min_date = min(forecast_df.Date).strftime('%Y-%m-%d')
        max_date = max(forecast_df.Date).strftime('%Y-%m-%d')
        plt.title('Forecast: '+str(min_date)+' -> '+str(max_date))
        plt.savefig('C:/Users/HumeD/Documents/outplot.png')


    def plotOutput(self,output_path):
        raise NotImplementedError
        pass
