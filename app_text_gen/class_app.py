from transformers import pipeline

class Text_generation():
    def __init__(self) -> None:
        self.model_path = 'G:/Django/all_model/anil/gpt2'
        self.load_model = pipeline('text-generation', model= self.model_path)

    def process(self, start_string, max_length=50, num_return_sequences=5):
        output = self.load_model(start_string, max_length = max_length, num_return_sequences = num_return_sequences)
        return output