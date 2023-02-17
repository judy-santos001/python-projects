
def convert_to_morse(code):

  code = code.replace("A", ".-")
  code = code.replace("B", "-...")
  code = code.replace("C", ".-.-.")
  code = code.replace("D", "-..")
  code = code.replace("E", ".")
  code = code.replace("F", "..-.")
  code = code.replace("G", "--.")
  code = code.replace("H", "....")
  code = code.replace("I", "..")
  code = code.replace("J", ".---")
  code = code.replace("K", "-.-")
  code = code.replace("L", ".-..")
  code = code.replace("M", "--")
  code = code.replace("N", "-.")
  code = code.replace("O", "---")
  code = code.replace("P", ".--.")
  code = code.replace("Q", "--.-")
  code = code.replace("R", ".-.")
  code = code.replace("S", "...")
  code = code.replace("T", "-")
  code = code.replace("U", "..-")
  code = code.replace("V", "...-")
  code = code.replace("W", ".--")
  code = code.replace("X", "-..-")
  code = code.replace("Y", "-.--")
  code = code.replace("Z", "--..")

  return code

lock_code = input("Type anything :") 

morse = convert_to_morse(lock_code)
print(f"Morse code: {morse}")