from termanalyzer import TermAnalyzer


def main():
    directory = "./database"
    termAnalyzer = TermAnalyzer()
    termAnalyzer.analyzeDirectory(directory)
    termAnalyzer.printStats()


if __name__ == "__main__":
    main()
