def show_magicians(focus_name):
    for focus in focus_name:
        print(focus.title())


def make_great(focus_name):
    for remov in focus_name:
        print(remov.title()+' Great')


focus_name=['ivan','petya', 'scoot']
focus = []
show_magicians(focus_name[:])



remov=[]
make_great(focus_name)


show_magicians(focus_name)

