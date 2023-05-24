import csv

input_file = 'test_1.csv'
output_file = 'submission_1.csv'

def read_links_from_csv(filename):
    links = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            link = row[0]
            links.append(link)
    return links

def save_predictions_to_csv(links, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Predicted'])
        for link in links:
            writer.writerow([link, 'False'])

# Example usage
links = read_links_from_csv(input_file)
save_predictions_to_csv(links, output_file)

