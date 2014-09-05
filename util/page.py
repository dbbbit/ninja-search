def gen_pages(current, max_page):

    """
        current = 4
        max_page = 8

        return [1 2 3 4 5 6 7]
    """
    def filter(x):
        if x >= 0 and x <= max_page: 
            return x

        #: else will return None 

    return [x for x in map(filter, 
                            range(current-3, current) + range(current, current+4)) 
                if x is not None]

if __name__ == "__main__":

    print(gen_pages(4,8))
