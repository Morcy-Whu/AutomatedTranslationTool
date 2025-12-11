# ProcessFile.py

class ProcessFile:
    def __init__(self):
        """
        Initialize ProcessFile without requiring a path.
        Path must later be set using set_path().
        """
        self.path = r"D:\Applications\Pycharm Project\MarianMT\TxtFile\Test.txt"       # 初始为空，之后用 set_path() 设置
        self.content = ""    # 存储文件内容

    def set_path(self, path: str):
        """
        Set or update the path to the .txt file.

        Args:
            path (str): New path to the .txt file.
        """
        self.path = path

    def read_txt(self):
        """
        Read the text file from self.path and store its content in self.content.
        """

        if self.path == "":
            raise ValueError("Error: No file path set. Please call set_path(path) first.")

        if not self.path.lower().endswith(".txt"):
            raise ValueError("Error: Only .txt files can be processed.")

        try:
            with open(self.path, "r", encoding="utf-8") as f:
                self.content = f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: File not found -> {self.path}")

    def print_content(self):
        """
        Print the stored content.
        """
        if self.content == "":
            print("Warning: content is empty. Did you call read_txt()?")

        print("\n===== File Content Start =====\n")
        print(self.content)
        print("\n===== File Content End =====\n")

    def get_content(self):
        return self.content
