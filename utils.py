import openai
import tomllib


with open('config.toml', 'rb') as file:
    config = tomllib.load(file)

openai.api_key = config['openai']['key']
command_guilds = config['discord']['ids']['guilds']

def split_string_at_newlines(input_string, max_chunk_size=2000, split_str='\n\n') -> list[str]:
    input_length = len(input_string)
    chunks = []
    start = 0

    while start < input_length:
        end = start + max_chunk_size

        # Find the nearest '\n\n' before the end of the current chunk
        if end < input_length:
            end = input_string.rfind(split_str, start, end) + 2

            # If '\n\n' was not found within the chunk, search forward for the next '\n\n'
            if end == 1:
                end = input_string.find(split_str, start + max_chunk_size) + 2

                # If there's still no '\n\n', set the end to the end of the string
                if end == 1:
                    end = input_length

        chunks.append(input_string[start:end])
        start = end

    return chunks
