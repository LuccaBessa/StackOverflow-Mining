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
    while restItems.__len__() < 200:
        restPage += 1
        restData = getData('rest', restPage)
        restItems += restData['items']

    print('Getting GRAPHQL data...')
    graphData = getData('graphql', 1)
    graphItems = graphData['items']
    # while graphData['quota_remaining'] > 0:
    while graphItems.__len__() < 200:
        graphPage += 1
        graphData = getData('graphql', graphPage)
        graphItems += graphData['items']

    print(restItems.__len__(), graphItems.__len__())

    generateCSV(restItems, 'rest')
    generateCSV(graphItems, 'graph')


if __name__ == "__main__":
    main()
