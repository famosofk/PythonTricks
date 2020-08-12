
people = ['Dr. Christopher Brooks', 'Dr. Kevyn Collins-Thompson', 'Dr. VG Vinod Vydiswaran', 'Dr. Daniel Romero']

def split_name(obj):
    title = obj.split()[0]
    lastname = obj.split()[-1]
    return('{} {}').format(title, lastname)


print(list(map(split_name, people)))