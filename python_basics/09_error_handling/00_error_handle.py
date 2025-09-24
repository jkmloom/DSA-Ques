file = open('YouTube.txt', 'w') # if there is no file by this name then, it will be created (in write/w mode)

# conventional method in python
try:
    file.write('@jkmloom at GitHub')
finally:
    file.close()

# Updated method in python
with open('YouTube.txt', 'w') as file:
    file.write('@jkmloom at GitHub')