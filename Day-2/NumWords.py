def num_to_words(n):
    words = {
        '0': 'Zero', '1': 'One', '2': 'Two', '3': 'Three', '4': 'Four',
        '5': 'Five', '6': 'Six', '7': 'Seven', '8': 'Eight', '9': 'Nine'
    }
    for digit in str(n):
        print(words[digit], end=' ')
    print()
n = int(input("Enter a number: "))
num_to_words(n)