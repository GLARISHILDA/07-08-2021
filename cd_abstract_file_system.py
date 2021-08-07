# Write a function that provides a change directory (cd) function for an abstract file system.

class Path:
    def __init__(self, path):
        self.current_path = path # Current path

    def cd(self, new_path): # cd function 
        parent = '..'
        separator = '/'

        # Absolute path        
        change_list = self.current_path.split(separator)
        
        new_list = new_path.split(separator)

        # Relative path
        for item in new_list:
            if item == parent:
                #delete the last item in list
                del change_list[-1]
            else:
                change_list.append(item)
                
        # Add "/" before each item in the list and print as string                    
        self.current_path = "/".join(change_list)
        return self.current_path

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)