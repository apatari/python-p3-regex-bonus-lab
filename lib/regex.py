import re




my_pattern = r"[A-Z].+lovely\sday.+[\.\?]|[A-Z].+weather.+[\.\?]|[A-Z].+just.+[\.\?]"
my_regex = re.compile(my_pattern)

