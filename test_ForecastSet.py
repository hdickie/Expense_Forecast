import pytest
import ForecastSet
import BudgetSet
import BudgetItem
import ExpenseForecast
import MilestoneSet
import AccountSet
import MemoRuleSet
import datetime

class TestForecastSet:

    # @pytest.mark.parametrize('core_budget_set,option_budget_set',
    #
    #                          [(BudgetSet.BudgetSet([]),BudgetSet.BudgetSet([]))]
    #
    #                          )
    # def test_ForecastSetConstructor(self,core_budget_set,option_budget_set):
    #     S = ForecastSet.ForecastSet(core_budget_set, option_budget_set)
    #
    # @pytest.mark.parametrize('core_budget_set,option_budget_set',
    #
    #                          [(BudgetSet.BudgetSet([BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'core 1')
    #
    #                                                 ]),
    #                            BudgetSet.BudgetSet([BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'core 1')
    #
    #                                                 ])),
    #
    #                           (BudgetSet.BudgetSet(
    #                               [BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'core 1')
    #
    #                                ]),
    #                            BudgetSet.BudgetSet(
    #                                [BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'core 1')
    #
    #                                 ])), #todo make this different from pervious test case
    #
    #                           ]
    #
    #                          )
    # def test_ForecastSetConstructor__expect_fail(self, core_budget_set, option_budget_set):
    #
    #     with pytest.raises(ValueError):
    #         S = ForecastSet.ForecastSet(core_budget_set, option_budget_set)
    #
    # @pytest.mark.parametrize('core_budget_set,option_budget_set',
    #
    #                          [(BudgetSet.BudgetSet([BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'core 1'),
    #                                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'core 2'),
    #                                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'core 3')
    #
    #                                                 ]),
    #                            BudgetSet.BudgetSet([BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1A'),
    #                                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1B'),
    #                                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1C'),
    #                                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2A'),
    #                                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2B'),
    #                                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2C')
    #                                                 ])),
    #
    #
    #                           ])
    # # def test_addScenario(self,core_budget_set,option_budget_set):
    # #     S = ForecastSet.ForecastSet(core_budget_set, option_budget_set)
    # #
    # #     S.addScenario(['.*A.*'])
    # #     S.addScenario(['.*B.*'])
    # #     S.addScenario(['.*C.*'])
    # #
    # #     print(S)
    #
    # @pytest.mark.parametrize('core_budget_set,option_budget_set',
    #
    #                          [(BudgetSet.BudgetSet(
    #                              [BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'core 1'),
    #                               BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'core 2'),
    #                               BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'core 3')
    #
    #                               ]),
    #                            BudgetSet.BudgetSet(
    #                                [BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1A'),
    #                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1B'),
    #                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1C'),
    #                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1D'),
    #                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2A'),
    #                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2B'),
    #                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2C'),
    #                                 BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2D')
    #                                 ])),
    #
    #                           ])
    # def test_addChoiceToAllForecasts(self,core_budget_set,option_budget_set):
    #     S = ForecastSet.ForecastSet(core_budget_set, option_budget_set)
    #
    #     scenario_A = ['.*A.*']
    #     scenario_B = ['.*B.*']
    #     scenario_C = ['.*C.*']
    #     scenario_D = ['.*D.*']
    #     S.addChoiceToAllForecasts(['A','B'],[scenario_A,scenario_B])
    #     S.addChoiceToAllForecasts(['C','D'],[scenario_C, scenario_D])
    #
    #     print(S)
    #
    # def test_str(self):
    #     raise NotImplementedError
    #
    # def test_renameForecast(self):
    #     raise NotImplementedError

    def test_update_date_range(self):
        start_date = datetime.datetime.now().strftime('%Y%m%d')
        end_date = '20240430'

        A = AccountSet.AccountSet([])
        B1 = BudgetSet.BudgetSet([])
        M = MemoRuleSet.MemoRuleSet([])

        B_optional = BudgetSet.BudgetSet([])
        B_optional.addBudgetItem(start_date, end_date, 1, 'daily', 10, 'Choice 1 Option A', False, False)
        B_optional.addBudgetItem(start_date, end_date, 1, 'daily', 10, 'Choice 1 Option B', False, False)
        B_optional.addBudgetItem(start_date, end_date, 1, 'daily', 10, 'Choice 2 Option C', False, False)
        B_optional.addBudgetItem(start_date, end_date, 1, 'daily', 10, 'Choice 2 Option D', False, False)

        A.createCheckingAccount('Checking', 5000, 0, 99999)
        B1.addBudgetItem(start_date, end_date, 1, 'daily', 10, 'food 1', False, False)
        M.addMemoRule('.*', 'Checking', 'None', 1)

        MS = MilestoneSet.MilestoneSet([], [], [])
        E1 = ExpenseForecast.ExpenseForecast(A, B1, M, start_date, end_date, MS)

        option_budget_set = BudgetSet.BudgetSet(
            [BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1A'),
             BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1B'),
             BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1C'),
             BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1D'),
             BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2A'),
             BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2B'),
             BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2C'),
             BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2D')
             ])

        S = ForecastSet.ForecastSet(E1, option_budget_set)
        S.addChoiceToAllForecasts(['A', 'B'], [['.*A.*'], ['.*B.*']])
        S.addChoiceToAllForecasts(['C', 'D'], [['.*C.*'], ['.*D.*']])
        S.initialize_forecasts()

        for k, v in S.initialized_forecasts.items():
            print(k,v.unique_id)
        S.update_date_range('20240101','20250101')
        print('---------')
        for k, v in S.initialized_forecasts.items():
            print(k,v.unique_id)

        assert False

    def test_ForecastSet_to_json(self):
        start_date = datetime.datetime.now().strftime('%Y%m%d')
        end_date = '20240430'

        A = AccountSet.AccountSet([])
        B1 = BudgetSet.BudgetSet([])
        M = MemoRuleSet.MemoRuleSet([])

        B_optional = BudgetSet.BudgetSet([])
        B_optional.addBudgetItem(start_date, end_date, 1, 'daily', 10, 'Choice 1 Option A', False, False)
        B_optional.addBudgetItem(start_date, end_date, 1, 'daily', 10, 'Choice 1 Option B', False, False)
        B_optional.addBudgetItem(start_date, end_date, 1, 'daily', 10, 'Choice 2 Option C', False, False)
        B_optional.addBudgetItem(start_date, end_date, 1, 'daily', 10, 'Choice 2 Option D', False, False)

        A.createCheckingAccount('Checking', 5000, 0, 99999)
        B1.addBudgetItem(start_date, end_date, 1, 'daily', 10, 'food 1', False, False)
        M.addMemoRule('.*', 'Checking', 'None', 1)

        MS = MilestoneSet.MilestoneSet([], [], [])
        E1 = ExpenseForecast.ExpenseForecast(A, B1, M, start_date, end_date, MS)

        option_budget_set = BudgetSet.BudgetSet(
                                   [BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1A'),
                                    BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1B'),
                                    BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1C'),
                                    BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 1D'),
                                    BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2A'),
                                    BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2B'),
                                    BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2C'),
                                    BudgetItem.BudgetItem('20000102', '20000102', 1, 'once', 10, 'option 2D')
                                    ])

        S = ForecastSet.ForecastSet(E1, option_budget_set)

        S.addChoiceToAllForecasts(['A', 'B'], [['.*A.*'], ['.*B.*']])
        S.addChoiceToAllForecasts(['C', 'D'], [['.*C.*'], ['.*D.*']])

        S_json = S.to_json()

        S2 = ForecastSet.from_json_string(S_json)

        # print('--------------')
        # print('--------------')
        # print('--------------')
        # print(S.to_json())
        # print('--------------')
        # print('--------------')
        # print('--------------')
        # print(S2.to_json())
        # print('--------------')
        # print('--------------')
        # print('--------------')

        with open('S.json','w') as f:
            f.writelines(S.to_json())

        with open('S2.json','w') as f:
            f.writelines(S2.to_json())


        assert S.base_forecast.to_json() == S2.base_forecast.to_json()
        assert S.option_budget_set.to_json() == S2.option_budget_set.to_json()
        assert S.forecast_set_name == S2.forecast_set_name

        # this doesn't work bc memory addresses
        # assert str(S.forecast_name_to_budget_item_set__dict) == str(S2.forecast_name_to_budget_item_set__dict)
        # assert str(S.initialized_forecasts) == str(S2.initialized_forecasts)
        # assert str(S.id_to_name) == str(S2.id_to_name)

        assert S.forecast_name_to_budget_item_set__dict.keys() == S2.forecast_name_to_budget_item_set__dict.keys()
        assert S.initialized_forecasts.keys() == S2.initialized_forecasts.keys()
        assert S.id_to_name.keys() == S2.id_to_name.keys()

        for k in S.forecast_name_to_budget_item_set__dict.keys():
            assert S.forecast_name_to_budget_item_set__dict[k].to_json() == S2.forecast_name_to_budget_item_set__dict[k].to_json()

        for k in S.initialized_forecasts.keys():
            assert S.initialized_forecasts[k].to_json() == S2.initialized_forecasts[k].to_json()

        for k in S.id_to_name.keys():
            assert S.id_to_name[k] == S2.id_to_name[k]

        assert S.to_json() == S2.to_json()

    def test_ForecastSet_writeToDatabase_empty_notRun(self):

        database_hostname = 'host.docker.internal'
        database_name = 'postgres'
        database_username = 'virtuoso_user'
        database_password = 'virtuoso_password'
        database_port = 5433
        username = 'virtuoso_user'

        start_date_YYYYMMDD = '20000101'
        end_date_YYYYMMDD = '20000201'

        A = AccountSet.AccountSet()
        A.createCheckingAccount('Checking',100,0,100000)

        B = BudgetSet.BudgetSet()
        M = MemoRuleSet.MemoRuleSet()
        MS = MilestoneSet.MilestoneSet()

        E = ExpenseForecast.ExpenseForecast(A,B,M,start_date_YYYYMMDD,end_date_YYYYMMDD,MS)
        S = ForecastSet.ForecastSet(base_forecast=E, option_budget_set=B)
        S.writeToDatabase(database_hostname, database_name, database_username, database_password, database_port,username)

        S2 = ForecastSet.initialize_forecast_set_from_database(set_id=S.unique_id,
                                                               username=username,
                                                               database_hostname=database_hostname,
                                                               database_name=database_name,
                                                               database_username=database_username,
                                                               database_password=database_password,
                                                               database_port=database_port)

        #this is gonna fail bc memory addresses
        #assert S.to_json() == S2.to_json()
        assert S.forecast_set_name == S2.forecast_set_name
        assert S.base_forecast.to_json() == S2.base_forecast.to_json()
        assert S.initialized_forecasts.keys() == S2.initialized_forecasts.keys()



        assert S.option_budget_set.getBudgetItems().to_string() == S2.option_budget_set.getBudgetItems().to_string()

        for unique_id, E in S.initialized_forecasts.items():
            assert E.forecast_df.to_json() == S.initialized_forecasts[unique_id].forecast_df.to_json()

        assert S.to_json() == S2.to_json()

        # Shouldn't this at least have core? Not sure.... Let's move on for now...
        # S_keys_list = list(S.forecast_name_to_budget_item_set__dict.keys())
        # assert len(S_keys_list) > 0
        #
        # S2_keys_list = list(S2.forecast_name_to_budget_item_set__dict.keys())
        # assert S_keys_list == S2_keys_list

    #while not really a valid business case, it is a technical edge case
    def test_ForecastSet_writeToDatabase_empty_Run(self):
        database_hostname = 'host.docker.internal'
        database_name = 'postgres'
        database_username = 'virtuoso_user'
        database_password = 'virtuoso_password'
        database_port = 5433
        username = 'virtuoso_user'

        start_date_YYYYMMDD = '20000101'
        end_date_YYYYMMDD = '20000201'

        A = AccountSet.AccountSet()
        A.createCheckingAccount('Checking', 100, 0, 100000)

        B = BudgetSet.BudgetSet()
        M = MemoRuleSet.MemoRuleSet()
        MS = MilestoneSet.MilestoneSet()

        E = ExpenseForecast.ExpenseForecast(A, B, M, start_date_YYYYMMDD, end_date_YYYYMMDD, MS)
        S = ForecastSet.ForecastSet(base_forecast=E, option_budget_set=B)
        S.runAllForecasts()
        S.writeToDatabase(database_hostname, database_name, database_username, database_password, database_port,
                          username)

        S2 = ForecastSet.initialize_forecast_set_from_database(set_id=S.unique_id,
                                                               username=username,
                                                               database_hostname=database_hostname,
                                                               database_name=database_name,
                                                               database_username=database_username,
                                                               database_password=database_password,
                                                               database_port=database_port)

        assert S.to_json() == S2.to_json()

    def test_ForecastSet_writeToDatabase_zeroChoices_NotRun(self):
        database_hostname = 'host.docker.internal'
        database_name = 'postgres'
        database_username = 'virtuoso_user'
        database_password = 'virtuoso_password'
        database_port = 5433
        username = 'virtuoso_user'

        start_date_YYYYMMDD = '20000101'
        end_date_YYYYMMDD = '20000201'

        A = AccountSet.AccountSet()
        A.createCheckingAccount('Checking', 100, 0, 100000)

        B = BudgetSet.BudgetSet()
        B.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 10, 'test txn', False,False)

        B_option = BudgetSet.BudgetSet()
        B_option.addBudgetItem(start_date_YYYYMMDD,end_date_YYYYMMDD,1,'daily',10,'test optional txn',False,False)

        M = MemoRuleSet.MemoRuleSet()
        M.addMemoRule('.*','Checking','None',1)

        MS = MilestoneSet.MilestoneSet()

        E = ExpenseForecast.ExpenseForecast(A, B, M, start_date_YYYYMMDD, end_date_YYYYMMDD, MS)
        S = ForecastSet.ForecastSet(base_forecast=E, option_budget_set=B_option)
        S.writeToDatabase(database_hostname, database_name, database_username, database_password, database_port,
                          username)

        S2 = ForecastSet.initialize_forecast_set_from_database(set_id=S.unique_id,
                                                               username=username,
                                                               database_hostname=database_hostname,
                                                               database_name=database_name,
                                                               database_username=database_username,
                                                               database_password=database_password,
                                                               database_port=database_port)

        # this is gonna fail bc memory addresses
        # assert S.to_json() == S2.to_json()
        assert S.forecast_set_name == S2.forecast_set_name
        assert S.base_forecast.to_json() == S2.base_forecast.to_json()
        assert S.initialized_forecasts.keys() == S2.initialized_forecasts.keys()

        assert S.option_budget_set.getBudgetItems().to_string() == S2.option_budget_set.getBudgetItems().to_string()

        assert S.to_json() == S2.to_json()

        #these would be None bc not run yet
        # for unique_id, E in S.initialized_forecasts.items():
        #     check_1 = E.forecast_df.to_json()
        #     check_2 = S.initialized_forecasts[unique_id].forecast_df.to_json()
        #     assert check_1 is not None
        #     assert check_2 is not None
        #     assert check_1 == check_2

    def test_ForecastSet_writeToDatabase_zeroChoices_Run(self):
        database_hostname = 'host.docker.internal'
        database_name = 'postgres'
        database_username = 'virtuoso_user'
        database_password = 'virtuoso_password'
        database_port = 5433
        username = 'virtuoso_user'

        start_date_YYYYMMDD = '20000101'
        end_date_YYYYMMDD = '20000201'

        A = AccountSet.AccountSet()
        A.createCheckingAccount('Checking', 1000, 0, 100000)

        B = BudgetSet.BudgetSet()
        B.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 10, 'test txn', False,False)

        B_option = BudgetSet.BudgetSet()
        B_option.addBudgetItem(start_date_YYYYMMDD,end_date_YYYYMMDD,1,'daily',10,'test optional txn',False,False)

        M = MemoRuleSet.MemoRuleSet()
        M.addMemoRule('.*','Checking','None',1)

        MS = MilestoneSet.MilestoneSet()

        E = ExpenseForecast.ExpenseForecast(A, B, M, start_date_YYYYMMDD, end_date_YYYYMMDD, MS)
        S = ForecastSet.ForecastSet(base_forecast=E, option_budget_set=B_option)
        S.runAllForecasts()
        S.writeToDatabase(database_hostname, database_name, database_username, database_password, database_port,
                          username)

        S2 = ForecastSet.initialize_forecast_set_from_database(set_id=S.unique_id,
                                                               username=username,
                                                               database_hostname=database_hostname,
                                                               database_name=database_name,
                                                               database_username=database_username,
                                                               database_password=database_password,
                                                               database_port=database_port)

        # this is gonna fail bc memory addresses
        # assert S.to_json() == S2.to_json()
        assert S.forecast_set_name == S2.forecast_set_name
        assert S.base_forecast.to_json() == S2.base_forecast.to_json()
        assert S.initialized_forecasts.keys() == S2.initialized_forecasts.keys()

        assert S.option_budget_set.getBudgetItems().to_string() == S2.option_budget_set.getBudgetItems().to_string()

        #these would be None bc not run yet
        # print('S.initialized_forecasts.keys():')
        # print(S.initialized_forecasts.keys())
        for unique_id, E in S.initialized_forecasts.items():
            print('Checking '+unique_id)
            check_1 = E.forecast_df.to_json()
            check_2 = S.initialized_forecasts[unique_id].forecast_df.to_json()
            assert check_1 is not None
            assert check_2 is not None
            assert check_1 == check_2
            # print(check_1)

        assert S.base_forecast.forecast_name == 'Core'

        assert S.to_json() == S2.to_json()

    def test_ForecastSet_writeToDatabase_oneChoice_Run(self):
        database_hostname = 'host.docker.internal'
        database_name = 'postgres'
        database_username = 'virtuoso_user'
        database_password = 'virtuoso_password'
        database_port = 5433
        username = 'virtuoso_user'

        start_date_YYYYMMDD = '20000101'
        end_date_YYYYMMDD = '20000201'

        A = AccountSet.AccountSet()
        A.createCheckingAccount('Checking', 1000, 0, 100000)

        B = BudgetSet.BudgetSet()
        B.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 10, 'test txn', False, False)

        B_option = BudgetSet.BudgetSet()
        B_option.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 2, 'option A', False, False)
        B_option.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 4, 'option B', False, False)

        M = MemoRuleSet.MemoRuleSet()
        M.addMemoRule('.*', 'Checking', 'None', 1)

        MS = MilestoneSet.MilestoneSet()

        E = ExpenseForecast.ExpenseForecast(A, B, M, start_date_YYYYMMDD, end_date_YYYYMMDD, MS)
        #print('Base Forecast id: '.ljust(40)+E.unique_id)
        S = ForecastSet.ForecastSet(base_forecast=E, option_budget_set=B_option)
        assert len(S.id_to_name) > 0 #1
        #print('S initial id: '.ljust(40) + S.unique_id)
        #print('S base forecast id: '.ljust(40) + S.base_forecast.unique_id)
        S.addChoiceToAllForecasts(['option A','option B'],[['.*option A.*'],['.*option B.*']])
        assert len(S.id_to_name) > 0 #2
        #print('S base forecast id (after add choice): '.ljust(40) + S.base_forecast.unique_id)
        #print('S id after add choice: '.ljust(40) + S.unique_id)
        S.runAllForecasts()
        assert len(S.id_to_name) > 0 #3
        #print('S base forecast id (after run): '.ljust(40) + S.base_forecast.unique_id)
        #print('S id after run: '.ljust(40) + S.unique_id)
        S.writeToDatabase(database_hostname, database_name, database_username, database_password, database_port,
                          username)
        #print('S base forecast id (after write): '.ljust(40) + S.base_forecast.unique_id)
        #print('S id after write: '.ljust(40) + S.unique_id)

        S2 = ForecastSet.initialize_forecast_set_from_database(set_id=S.unique_id,
                                                               username=username,
                                                               database_hostname=database_hostname,
                                                               database_name=database_name,
                                                               database_username=database_username,
                                                               database_password=database_password,
                                                               database_port=database_port)
        #print('S2 id (after load): '.ljust(40) + S2.unique_id)
        #print('S2 base forecast id (after load): '.ljust(40) + S2.base_forecast.unique_id)
        # this is gonna fail bc memory addresses
        # assert S.to_json() == S2.to_json()
        assert S.forecast_set_name == S2.forecast_set_name

        # print('################################################')
        # print(S.base_forecast.to_json())
        # print('################################################')
        # print(S2.base_forecast.to_json())
        # print('################################################')

        assert S.base_forecast.to_json() == S2.base_forecast.to_json()
        # print(' S.base_forecast.unique_id:'+S.base_forecast.unique_id)
        # print('S2.base_forecast.unique_id:'+S2.base_forecast.unique_id)
        #
        # print('S.initialized_forecasts.keys():')
        # print(S.initialized_forecasts.keys())
        #
        # print('S2.initialized_forecasts.keys():')
        # print(S2.initialized_forecasts.keys())
        assert S.initialized_forecasts.keys() == S2.initialized_forecasts.keys()

        assert S.option_budget_set.getBudgetItems().to_string() == S2.option_budget_set.getBudgetItems().to_string()

        # these would be None bc not run yet
        # print('S.initialized_forecasts.keys():')
        # print(S.initialized_forecasts.keys())
        for unique_id, E in S.initialized_forecasts.items():
            #print('Checking ' + unique_id)
            check_1 = E.forecast_df.to_json()
            check_2 = S.initialized_forecasts[unique_id].forecast_df.to_json()
            assert check_1 is not None
            assert check_2 is not None
            assert check_1 == check_2

        # print('####################################')
        # print(S.to_json())
        # print('####################################')
        # print(S2.to_json())
        # print('####################################')
        assert S.to_json() == S2.to_json()



    def test_ForecastSet_writeToDatabase_twoChoices_NotRun(self):
        database_hostname = 'host.docker.internal'
        database_name = 'postgres'
        database_username = 'virtuoso_user'
        database_password = 'virtuoso_password'
        database_port = 5433
        username = 'virtuoso_user'

        start_date_YYYYMMDD = '20000101'
        end_date_YYYYMMDD = '20000201'

        A = AccountSet.AccountSet()
        A.createCheckingAccount('Checking', 1000, 0, 100000)

        B = BudgetSet.BudgetSet()
        B.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 10, 'test txn', False, False)

        B_option = BudgetSet.BudgetSet()
        B_option.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 2, 'option A', False, False)
        B_option.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 4, 'option B', False, False)
        B_option.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 3, 'option C', False, False)
        B_option.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 6, 'option D', False, False)

        M = MemoRuleSet.MemoRuleSet()
        M.addMemoRule('.*', 'Checking', 'None', 1)

        MS = MilestoneSet.MilestoneSet()

        E = ExpenseForecast.ExpenseForecast(A, B, M, start_date_YYYYMMDD, end_date_YYYYMMDD, MS)
        # print('Base Forecast id: '.ljust(40)+E.unique_id)
        S = ForecastSet.ForecastSet(base_forecast=E, option_budget_set=B_option)

        S.addChoiceToAllForecasts(['option A', 'option B'], [['.*option A.*'], ['.*option B.*']])
        S.addChoiceToAllForecasts(['option C', 'option D'], [['.*option C.*'], ['.*option D.*']])

        S.writeToDatabase(database_hostname, database_name, database_username, database_password, database_port,
                          username)

        S2 = ForecastSet.initialize_forecast_set_from_database(set_id=S.unique_id,
                                                               username=username,
                                                               database_hostname=database_hostname,
                                                               database_name=database_name,
                                                               database_username=database_username,
                                                               database_password=database_password,
                                                               database_port=database_port)

        assert S.to_json() == S2.to_json()

    def test_ForecastSet_writeToDatabase_twoChoices_Run(self):
        database_hostname = 'host.docker.internal'
        database_name = 'postgres'
        database_username = 'virtuoso_user'
        database_password = 'virtuoso_password'
        database_port = 5433
        username = 'virtuoso_user'

        start_date_YYYYMMDD = '20000101'
        end_date_YYYYMMDD = '20000201'

        A = AccountSet.AccountSet()
        A.createCheckingAccount('Checking', 1000, 0, 100000)

        B = BudgetSet.BudgetSet()
        B.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 10, 'test txn', False, False)

        B_option = BudgetSet.BudgetSet()
        B_option.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 2, 'option A', False, False)
        B_option.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 4, 'option B', False, False)
        B_option.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 3, 'option C', False, False)
        B_option.addBudgetItem(start_date_YYYYMMDD, end_date_YYYYMMDD, 1, 'daily', 6, 'option D', False, False)

        M = MemoRuleSet.MemoRuleSet()
        M.addMemoRule('.*', 'Checking', 'None', 1)

        MS = MilestoneSet.MilestoneSet()

        E = ExpenseForecast.ExpenseForecast(A, B, M, start_date_YYYYMMDD, end_date_YYYYMMDD, MS)
        S = ForecastSet.ForecastSet(base_forecast=E, option_budget_set=B_option)

        S.addChoiceToAllForecasts(['option A', 'option B'], [['.*option A.*'], ['.*option B.*']])
        S.addChoiceToAllForecasts(['option C', 'option D'], [['.*option C.*'], ['.*option D.*']])
        S.runAllForecasts()
        S.writeToDatabase(database_hostname, database_name, database_username, database_password, database_port,
                          username)

        S2 = ForecastSet.initialize_forecast_set_from_database(set_id=S.unique_id,
                                                               username=username,
                                                               database_hostname=database_hostname,
                                                               database_name=database_name,
                                                               database_username=database_username,
                                                               database_password=database_password,
                                                               database_port=database_port)

        assert S.to_json() == S2.to_json()

    # def test_ForecastSet_writeToDatabase_expectError(self):
    #     raise NotImplementedError