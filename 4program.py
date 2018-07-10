import sys # <- module

class ArgumentHandler:
    def show_args(self):
        print sys.argv

# Main function
if __name__ == "__main__":
    a = ArgumentHandler()
    a.show_args()
