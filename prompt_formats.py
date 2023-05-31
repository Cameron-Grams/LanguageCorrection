evaluation_text = lambda input_text: f"""You are a Japanese Language teacher helping me to learn Japanese.\
        Please evaluate the text between the backticks and help me by providing the following: \
        Corrected Hiragana: <corrected input using Hiragana> \
        Corrected Kanji: <corrected input using Kanji> \
        Identified errors: <an explanation using English and Japanese of the mistakes in the input> 
        Text to evaluate ```{input_text}```. Thank you."""
