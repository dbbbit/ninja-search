def gen_pages(current, max_page):

    def nature(x):
        if x >= 0: 
            return x

    return [x for x in map(nature, 
                            range(current-3, current) + range(current, current+4)) 
                if x is not None and x <= max_page]

if __name__ == "__main__":

    print(gen_pages(3,7))
