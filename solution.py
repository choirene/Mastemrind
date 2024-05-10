class Solution:
    def __init__(self, num_list):
        self.num_list = num_list
        self.freq_dict = self.create_freq_dict()
        self.string_num = self.convert_to_string()

    def create_freq_dict(self):
        freq_dict = {}
        for num in self.num_list:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        return freq_dict
    
    def convert_to_string(self):
        string_solution = ''
        for num in self.num_list:
            string_solution += str(num)
        return string_solution