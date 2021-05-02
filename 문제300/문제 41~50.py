# 문자열

# 041.
ticker = "btc_krw"
print(ticker.upper())


# 042.
ticker = "BTC_KRW"
print(ticker.lower())


# 043.
문자열 = "hello"
print( 문자열.capitalize() )

# 044.
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))


# 045.
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx","xls")))


# 046.
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))


# 047.
a = "hello world"
나누기 = a.split(" ")

# 048.
ticker = "btc_krw"
나누기 = ticker.split(" ")

# 049.
data = "2020-05-01"
연도,월,일 = data.split("-")

# 050.
print("039490   ".rstrip())
