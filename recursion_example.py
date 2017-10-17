import sys

#-------------------------------------------------------------------
# Function Definition
#-------------------------------------------------------------------
def recursive_combinations(input_str, index, output, out_length):

  if index >= len(input_str):
    print (''.join(output)).rstrip(' ')
    return

  output[out_length] = input_str[index]
  output[out_length + 1] = ' '
  recursive_combinations(input_str, index + 1, output, out_length + 2)

  if index + 1 < len(input_str):
    recursive_combinations(input_str, index + 1, output, out_length + 1)

#-------------------------------------------------------------------
# Main
#-------------------------------------------------------------------
if len(sys.argv) == 1:
  print 'A numeric input string is required'
  sys.exit()

input_str = sys.argv[1]
if not input_str.isdigit():
  print 'The input string can only contain numeric characters'
  sys.exit()

recursive_combinations(input_str, 0, [''] * 100, 0)
