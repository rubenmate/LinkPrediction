import csv

CSV_FILE = 'test_1.csv'
OUTPUT_FILE = 'submission_1.csv'

def read_links_from_csv(filename):
    links = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            link = {
                'node1': int(row[0].split('-')[0]),
                'node2': int(row[0].split('-')[1]),
                'prediction': predict_link()  # Call the predict_link() function
            }
            links.append(link)
    return links

def predict_link():
    # Perform your prediction logic here
    return True

def save_predictions_to_csv(links, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Predicted'])
        for link in links:
            writer.writerow([f"{link['node1']}-{link['node2']}", link['prediction']])

# Example usage
links = read_links_from_csv(CSV_FILE)
save_predictions_to_csv(links, OUTPUT_FILE)

