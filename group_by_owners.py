# Problem statement: Implement a group_by_owners function that:
    # i)Accepts a dictionary containing the file owner name for each file name.
    # ii) Returns a dictionary containing a list of file names for each owner name, in any order.

class GroupbyOwners:    
    @staticmethod
    def group_by_owners(files):

        group_dict = dict() # Dictionary containing file owner name for each file name
        group_list = list() # Returns a list of file names for each owner name
        for key, value in files.items():
            #fill value w.r.to names of owners
            temp = [value, key]
            group_list.append(temp)

        for i in group_list:
            if i[0] not in group_dict:
                #fill out new dictionary w.r.to list of file names
                group_dict[i[0]] = [i[1]]
            else:
                group_dict[i[0]].append(i[1])
        return group_dict

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(GroupbyOwners.group_by_owners(files))