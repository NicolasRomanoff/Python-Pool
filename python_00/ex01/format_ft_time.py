from datetime import datetime

now = datetime.now()
original_date = datetime(1970, 1, 1)

seconds = now - original_date

print(f'Seconds since January 1, 1970: \
    {"{:,}".format(seconds.total_seconds())} or \
    {"{:.2e}".format(seconds.total_seconds())} in scientific notation')
print(now.strftime("%b %d %Y"))
