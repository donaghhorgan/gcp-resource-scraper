import argparse
import logging.config
import time
from datetime import datetime

import requests
import yaml
from google.cloud import firestore

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('config_file', help='The config file to load.')
    args = parser.parse_args()

    # Load YAML config
    with open(args.config_file) as f:
        config = yaml.safe_load(f)

    # Configure logging
    logging.config.dictConfig(config.get('logging', {}))
    logging.info('Running with config: %s', config)

    # Configure the Firestore client
    client = firestore.Client(project=config['gcp']['project'])
    collection = client.collection(config['gcp']['firestore']['collection'])

    # Loop forever
    while True:
        try:
            # Get the resource
            response = requests.get(**config['resource'])
            response.raise_for_status()
            response = response.json()

            # Push the resource to Firestore
            document_id = datetime.now().isoformat()
            document = collection.document(document_id)
            document.set(response)

            # Wait before trying again
            time.sleep(config.get('interval', 0))
        except KeyboardInterrupt:
            break
        except:
            logging.exception('An unexpected error occurred')
