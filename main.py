import networkx as nx
import csv

GEXF_FILE = 'social_network_training_1.gexf'
INPUT_FILE = 'test_1.csv'
OUTPUT_FILE = 'submission_1.csv'

def read_links_from_csv(filename):
    links = []
    G = nx.read_gexf(GEXF_FILE)  # Load the graph from GEXF file

    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            node1 = int(row[0].split('-')[0])
            node2 = int(row[0].split('-')[1])
            link = {
                'node1': node1,
                'node2': node2,
                'prediction': predict_link(G, node1, node2)  # Call the predict_link() function
            }
            links.append(link)
    return links

def predict_link(G, node1, node2):
    neighbors1 = set(G.neighbors(str(node1)))
    neighbors2 = set(G.neighbors(str(node2)))

    common_neighbors = neighbors1.intersection(neighbors2)
    
    if len(common_neighbors) > 0:
        return True  # Predict link exists if common neighbors exist

    return False  # Predict link does not exist if no common neighbors

def save_predictions_to_csv(links, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Id', 'Predicted'])
        for link in links:
            writer.writerow([f"{link['node1']}-{link['node2']}", link['prediction']])

# Example usage
links = read_links_from_csv(INPUT_FILE)
save_predictions_to_csv(links, OUTPUT_FILE)

