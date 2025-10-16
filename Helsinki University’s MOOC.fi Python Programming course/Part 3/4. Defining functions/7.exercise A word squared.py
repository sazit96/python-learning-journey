def squared(text, size):
    for i in range(size):
        for j in range(size):
            index = (i * size + j) % len(text)
            print(text[index], end="")
        print()



if __name__ == "__main__":
  squared("ab", 3)
  print()
  squared("aybabtu", 5)