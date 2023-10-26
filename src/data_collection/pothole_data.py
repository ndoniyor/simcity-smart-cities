from data_collector import DataCollector

ENDPOINT = 'x9wy-ing4'

def main():
    pothole_collector = DataCollector(ENDPOINT)
    df = pothole_collector.collect_data()
    pothole_collector.to_csv(df, 'nyc_pothole.csv')

if __name__ == '__main__':
    main()