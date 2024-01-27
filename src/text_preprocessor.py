class TextPreprocessor:
    """
    A class for preprocessing text data from a file.

    Attributes:
        file_path (str): Path to the text file to be processed.
        text (str): The loaded and preprocessed text.

    Methods:
        load_text: Load text from the specified file path into the 'text'
            attribute.
        remove_captions: Remove captions from the text.
        lowercase_and_tokenize: Convert all text to lowercase.
        add_new_line_after_punctuation: Add a new line after each punctuation
            mark in the predefined list.
        preprocess: Execute the complete preprocessing pipeline.
        get_processed_text: Get the preprocessed text.
    """
    def __init__(self, file_path):
        """
        Initialize TextPreprocessor with the provided file path.

        Args:
            file_path (str): Path to the text file to be processed.
        """
        self.file_path = file_path
        self.text = None

    def load_text(self):
        """
        Load text from the specified file path into the 'text' attribute.
        """
        with open(self.file_path, 'r', encoding='utf-8') as file:
            self.text = file.read()

    def remove_captions(self):
        """
        Remove captions from the text. Captions are lines in all uppercase
        with no alphabetic characters.
        """
        lines = self.text.split('\n')
        self.text = '\n'.join(
            line for line in lines
            if not line.isupper() or any(c.isalpha() for c in line)
        )

    def lowercase_and_tokenize(self):
        """
        Convert all text to lowercase.
        """
        self.text = self.text.lower()

    def add_new_line_after_punctuation(self):
        """
        Add a new line after each punctuation mark in the predefined list.
        """
        punctuation_marks = ['.', '!', '?']
        for mark in punctuation_marks:
            self.text = self.text.replace(mark, mark + '\n')

    def preprocess(self):
        """
        Execute the complete preprocessing pipeline: load text,
        remove captions, convert to lowercase, and add new lines.
        """
        self.load_text()
        self.remove_captions()
        self.lowercase_and_tokenize()
        self.add_new_line_after_punctuation()

    def get_processed_text(self):
        """
        Get the preprocessed text.

        Returns:
            str: The preprocessed text.
        """
        return self.text
