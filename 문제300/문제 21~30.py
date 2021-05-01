# 문자열

# 021.
lettera = "python"
print(lettera[0],lettera[2])

# 022.
license_plate = "24가 2210"
print(license_plate[4:8])

# 023.
string = "홀짝홀짝홀짝"
print(string[0]+string[2]+string[4])

# 024.
string = "PYTHON"
print(string[ : :-1])

# 025.
phone_number = "010-1111-2222"
끝 = phone_number.split("-")
print(끝[0],끝[1],끝[2])

# 026.
phone_number = "010-1111-2222"
끝 = phone_number.split("-")
print(끝[0]+끝[1]+끝[2])

# 027.
url = "http://sharebook.kr"
도메인 = url.split(".")
print(도메인[1])

# 028.
# lang = "python"
# lang[0] = 'P'
# print(lang)
# 예상 결과
# 오류가 남

# 029.
string = "abcdef2a354a32a"
대문자 = string.replace("a","A")
print(대문자)

# 030.
string =  "abcd"
string.replace("b","B")
print(string)
# 예상 결과
# abcd
# 이유 : string을 변환한 것을 변수에 저장해야되서