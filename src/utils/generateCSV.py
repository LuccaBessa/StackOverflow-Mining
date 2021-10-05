import csv
import os

headers = [
    'question_id',
    'user_id',
    'score',
    'view_count',
    'up_vote_count',
    'down_vote_count',
    'answer_count',
    'creation_date'
]


def generateCSV(json, filename):
    print("Generating " + filename + " CSV...")
    with open(filename + '.csv', 'x') as f:
        writer = csv.writer(f)

        writer.writerow(headers)

        for question in json:
            user_id = 'not informed' if question['owner'] == {
            } else question['owner']['user_id']

            writer.writerow([
                question['question_id'],
                user_id,
                question['score'],
                question['view_count'],
                question['up_vote_count'],
                question['down_vote_count'],
                question['answer_count'],
                question['creation_date']
            ])
