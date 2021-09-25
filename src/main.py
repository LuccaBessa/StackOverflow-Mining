from api.getRest import getRest
from api.getGraph import getGraph
from utils.generateCSV import generateCSV


def main():
    restData = getRest()
    graphData = getGraph()

    generateCSV(restData, 'rest')
    generateCSV(graphData, 'graph')


if __name__ == "__main__":
    main()
