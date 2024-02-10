import data_collector

def main():
    data = data_collector.collect_single_zoo(1)
    print(data)

if __name__ == "__main__":
    main()