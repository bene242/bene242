# Open a file
f = open('filename.txt')
  
  
# Read from a file
f = open('filename.txt', 'r')
  
# To read the whole file
print(f.read())
  
# To read single line
print(f.readline())
  
  
# Write to a file
f = open('filename.txt', 'w')
f.write('Writing into a file \n')
  
  
# Closing a file
f.close()