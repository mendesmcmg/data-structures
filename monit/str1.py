st = input()
response = ''

st = st.split('WUB')

response = list(filter(None, st))
response = ' '.join(response)
print(response)