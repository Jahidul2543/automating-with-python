def main():
    print("  inside main def")
    print("__name__: " + __name__)

if __name__ == "__main__":
    main()
else:
    print("running from import")
    print("__name__: when runnig from other module" + __name__)
    

