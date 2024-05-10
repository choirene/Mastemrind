class Number:
    def __init__(self, num_list=None, string_num=None):
        if num_list:
            self.num_list = num_list
            self.string_num = self.convert_to_string()
        elif string_num:
            self.string_num = string_num
            self.num_list = self.convert_to_num_list()
        self.freq_dict = self.create_freq_dict()

    def create_freq_dict(self):
        freq_dict = {}
        for num in self.num_list:
            if num not in freq_dict:
                freq_dict[num] = 1
            else:
                freq_dict[num] += 1
        return freq_dict
    
    def convert_to_string(self):
        string_num = ''
        for num in self.num_list:
            string_num += str(num)
        return string_num
    
    def convert_to_num_list(self):
        num_list = []
        for num in self.string_num:
            num_list.append(int(num))
        return num_list