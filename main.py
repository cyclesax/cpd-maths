import argparse
import hello

# Small function as start point ... like other languages

def main():
    print("in main function")
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test')
    parser.add_argument('-a', '--addtest')
    parser.add_argument('-v', dest='verbose', action='store_true')
    args = parser.parse_args()
    print(args)
    hello.test("called from main")
    
    # Now we can respond to whatever we received 
    
# special value allows us to work out how we were called and if we are
# the starting file then we can call a function called main(), like
# other languages
if __name__ == "__main__":
    main()