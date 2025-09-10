import numpy as np
import re
from test_model import (encoder_model, decoder_model, num_decoder_tokens, num_encoder_tokens, input_features_dict,
                        target_features_dict, reverse_target_features_dict, max_decoder_seq_length,
                        max_encoder_seq_length)


class ChatBot:

    negative_commands = []

    exit_commands = []

    def start_chat(self):
        pass

    def make_exit(self):
        pass

    def string_to_matrix(self):
        pass
