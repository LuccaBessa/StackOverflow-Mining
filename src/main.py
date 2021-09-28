from api.getData import getData
from utils.generateCSV import generateCSV
from dotenv import load_dotenv


def main():

    restPage = 1
    graphPage = 1

    load_dotenv()

    print('Getting REST data...')
    restData = getData('rest', 1)
    restItems = restData['items']
    # while restData['quota_remaining'] > 0:
    #     print('Quota remaining: ' + str(restData['quota_remaining']))
    #     restPage += 1
    #     restData = getRest(restPage)
    #     restItems += restData['items']

    print('Getting GRAPHQL data...')
    graphData = getData('graphql', 1)
    graphItems = graphData['items']
    # while graphData['quota_remaining'] > 0:
    #     print('Quota remaining: ' + str(graphData['quota_remaining']))
    #     graphPage += 1
    #     graphData = getRest(graphPage)
    #     restItems += restData['items']

    generateCSV(restItems, 'rest')
    generateCSV(graphItems, 'graph')


if __name__ == "__main__":
    main()
