class Solution:
    def __init__(self, num_list):
    self.name = name
    self.num_list = num_list
    self.freq_dict = create_freq_dict()
    self.string_num = convert_to_string()

    def create_freq_dict(self):
        freq_dict = {}
        for num in num_list:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        return freq_dict
    
    def convert_to_string(self):
        pass