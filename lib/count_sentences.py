class MyString:
    def __init__(self, value=""):
        self.value = value

    def is_sentence(self):
        if self.value and self.value.endswith("."):
            return True
        return False

    def is_question(self):
        if self.value and self.value.endswith("?"):
            return True
        return False

    def is_exclamation(self):
        if self.value and self.value.endswith("!"):
            return True
        return False

    def count_sentences(self):
        sentences = self.value.split('.')
        sentences = [s for s in sentences if s]  # Remove empty strings
        return len(sentences)

# Testing the MyString class
if __name__ == "__main__":
    # Create an instance of MyString
    my_string = MyString()

    # Test is_sentence method
    print(my_string.is_sentence())  # Should print False

    # Test is_question method
    print(my_string.is_question())  # Should print False

    # Test is_exclamation method
    print(my_string.is_exclamation())  # Should print False

    # Test count_sentences method
    print(my_string.count_sentences())  # Should print 0

    # Update the value
    my_string.value = "Hello World."
    print(my_string.is_sentence())  # Should print True

    my_string.value = "How are you?"
    print(my_string.is_question())  # Should print True

    my_string.value = "Great job!"
    print(my_string.is_exclamation())  # Should print True

    my_string.value = "This is a test. This is a test too."
    print(my_string.count_sentences())  # Should print 2
