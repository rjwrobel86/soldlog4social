#accepts "SoldLogExport.csv"
#outputs "fbsoldlog.csv" and "googsoldlog.csv"

import os
import pandas as pd
import numpy as np
import pandas as pd

data = pd.read_csv('SoldLogExport.csv')

data.columns

fbframe = data[['SoldDate', 'FirstName', 'LastName', 'Email', 'EmailAlt', 'EvePhone', 'DayPhone', 'CellPhone', 'PostalCode', 'State', 'FrontGross', 'BackGross', 'SoldNote', 'VehicleVIN', 'DealNumber']]
fbframe['Country'] = 'US'
fbframe['Event'] = 'Purchase'
fbframe['Currency'] = 'USD'
fbframe['Value'] = fbframe['FrontGross'] + fbframe['BackGross']
fbframe['Phone'] = '+1' + data['EvePhone'].astype(str)
fbframe['Phone2'] = '+1' + data['DayPhone'].astype(str)
fbframe['Phone3'] = '+1' + data['CellPhone'].astype(str)
fbframe['Email2'] = data['EmailAlt']

fbframe.drop(['EvePhone'], axis=1)
fbframe.drop(['DayPhone'], axis=1)
fbframe.drop(['CellPhone'], axis=1)
fbframe.drop(['EmailAlt'], axis=1)

fbframe = fbframe[['SoldDate','FirstName', 'LastName', 'Email', 'Email2', 'PostalCode', 'Phone', 'Phone2', 'Phone3', 'Country', 'State', 'Event', 'Value', 'Currency', 'VehicleVIN', 'DealNumber']]

fbframe.loc[(fbframe.Value <= 0),'Value']=1
fbframe.fillna(1, inplace=True)

fbframe['Phone'] = fbframe['Phone'].astype(str)
fbframe['Phone2'] = fbframe['Phone2'].astype(str)
fbframe['Phone3'] = fbframe['Phone3'].astype(str)

googframe = fbframe[['FirstName','LastName','Email','Phone','Country','PostalCode']]
googframe = googframe.rename({'FirstName':'First Name', 'LastName': 'Last Name','PostalCode':'Zip'}, axis=1)

fbframe.to_csv('fbsoldlog.csv', index=False)
googframe.to_csv('googsoldlog.csv', index=False)
