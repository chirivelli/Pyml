# input_xml = input()
input_xml = '''

            '''

def parse_root_level_tags(xml_str):
    tags = {}

    curr = xml_str.replace(" ", "").replace("\n", "")

    while curr:
        if curr[0] != '<': return curr

        tag = ''

        for i in range(1, len(curr)):
            if curr[i] == '>':
                tag = curr[1:i]
                break
        tag_start = 2 + len(tag)
        tag_end = curr.index('</' + tag + '>')

        val_str = curr[tag_start:tag_end]
        val = parse_root_level_tags(val_str)

        if tag in tags:
            val0 = tags[tag]
            tags[tag] = [val0]
            tags[tag].append(val)
        else:
            tags[tag] = val
        
        curr = curr[tag_end + len(tag) + 3:]

    return tags


root_tags = parse_root_level_tags(input_xml)

print(root_tags)