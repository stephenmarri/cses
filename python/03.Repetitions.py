user_input = input('')
longest = 0
streak = 0
prev = ''

for chr in user_input:
    if chr == prev:
        streak += 1
    else:
        longest = max(longest, streak)
        streak = 1
    prev = chr
print(max(longest, streak))
