students_file_name = "../dados/alunos.txt"

def ListSudentsFromCSVTextFile(fname):
    #fname = input("Enter filename: ")
    infile = open(fname,'r')
    for line in infile:
        line = line.rstrip('\n')
        print(line)


# ListSudentsFromCSVTextFile(students_file_name)

def SearchSudentsByNumber(fname, number_to_search):
    infile = open(fname, 'r')
    infile.readline()               #ignore the 1st line (heads)
    found = False
    for line in infile.readlines():
        line = line.rstrip('\n')
        data_vector = line.split(';')
        number = eval(data_vector[1])
        if (number == number_to_search):
            found = True
            break;
    if found:
        print("Student number %d found:" % (number_to_search))
        print(line)
    else:
        print("Student number %d not found:" % (number_to_search))

SearchSudentsByNumber(students_file_name, 1010955)


def SearchSudentsByName(fname, name_to_search):
    infile = open(fname, 'r')
    infile.readline()               #ignore the 1st line (heads)
    found = False
    data_vector = []
    for line in infile.readlines():
        line = line.rstrip('\n')
        data_vector = line.split(';')
        name = data_vector[0]
        if (name.find(name_to_search) >= 0):
            found = True
            break;
    if found:
        print("Student name %s found:" % (name_to_search))
        print(data_vector)
    else:
        print("Student name %s not found:" % (name_to_search))

SearchSudentsByName(students_file_name, "Manuel")
