def get_header_block1(self, file_name):
    with open(file_name, 'r') as file:
        first_line = file.readline()
        header_blocks1 = first_line.split('}')[0]
        header_blocks1_value = (header_blocks1[1:].split(':'))[1]
        print header_blocks1_value

def get_position_header_blocks(self, header_string):
    dict_position = {}
    start_block1 = header_string.find('{')
    end_block1 = header_string.find('}')
    start_block2 = header_string.find('{', end_block1)
    end_block2 = header_string.find('}', end_block1 + 1)
    start_block3 = header_string.find('{', end_block2)
    end_block3 = header_string.find('}', end_block2 + 1)
    dict_position[1] = [start_block1+1, end_block1]
    dict_position[2] = [start_block2+1, end_block2]
    dict_position[3] = [start_block3+1, end_block3]
    return dict_position

def get_header_block1(self, file_name):
    with open(file_name, 'r') as file:
        first_line = file.readline()
    position_header_block1 = self.get_position_header_blocks(first_line)[1]
    header_block1 = first_line[position_header_block1[0]:position_header_block1[1]]
    return header_block1
