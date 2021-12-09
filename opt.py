#Add later
def show_databases():
    data_base.show.all_info()
def show_database(var):
    data_base.show.all(var)
def show_lists(data_base=None):
    data_base.show.show_lists(data_base=data_base)
def show_row(data_base=None):
    data_base.show.show_row(data_base=data_base)