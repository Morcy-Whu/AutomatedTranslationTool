from ProcessFile import ProcessFile

# pf = ProcessFile()
# pf.set_path(path = r"C:\Users\ericm\Desktop\Tem\Tem.txt")
# pf.read_txt()
# pf.print_content()
def getcontent(path = None):
    if path is None:
        pf = ProcessFile()
        pf.read_txt()
        return pf.get_content()
    else:
        pf = ProcessFile()
        pf.set_path(path = path)
        pf.read_txt()
        return pf.get_content()


