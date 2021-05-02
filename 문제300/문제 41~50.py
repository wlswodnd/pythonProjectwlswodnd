# 문자열

# 041.
ticker = "btc_krw"
대문자 = ticker.upper()
print(대문자)

# 042.
ticker = "BTC_KRW"
소문자 = ticker.lower()
print(소문자)

# 043.
문자열 = "hello"
변환 = 문자열[0].upper()
print(변환+문자열[1:5])

# 044.
file_name = "보고서.xlsx"
확인 = file_name.endswith("xlsx")
print(확인)

# 045.
file_name = "보고서.xlsx"
확인 = file_name.endswith("xlsx")
print(확인)

# 046.
file_name = "2020_보고서.xlsx"
확인 = file_name.startswith("2020")
print(확인)

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
