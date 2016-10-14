class GetSandwich(object):

    def get_sandwich(self, sandwich_string):
        bread_len = len(str("bread"))
        first_bread_index = sandwich_string.find("bread")
        second_bread_index = sandwich_string.find("bread", first_bread_index + bread_len)
        sandwich_guts = sandwich_string[(first_bread_index + bread_len):second_bread_index]
        return sandwich_guts

