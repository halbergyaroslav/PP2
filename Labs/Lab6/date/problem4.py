from datetime import datetime

start_date = datetime.now()
end_date = datetime(2023,10,29,23,59,59)

print((end_date - start_date).total_seconds())