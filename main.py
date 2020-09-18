#Author: Brendan Corso bvc5434@psu.edu

def digit_sum(n):
  if (n == 0):
    return 0
  else:
    return (n % 10) + digit_sum(n // 10)


def run():
  number = int(input("Enter an int: "))
  sum = digit_sum(number)
  print(f"sum of digits of {number} is {sum}.")

if __name__ == "__main__":
  run()