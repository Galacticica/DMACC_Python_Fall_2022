from datetime import datetime
date_str = '09/19/2018'

date_object = datetime.strptime(date_str, '%m/%d/%Y').date()
print(type(date_object))
print(date_object)  # printed in default formatting
