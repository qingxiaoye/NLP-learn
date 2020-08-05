# -*- coding: utf-8 -*-
import json
from src.app.libs.knowledge.calculate_distance import paragraph_vector, distCos
from src.app.libs.knowledge.process import paragraph_process


def question_similar(question_type, question_paragraph, model):
    question_path = "/home/user/huanglhy/QIA_Serve_Production/heyi_kafka/src/app/libs/knowledge/question_vec.json"
    with open(question_path, "r", encoding="utf-8") as question_file:
        question_vec = json.load(question_file)
    question_contents = paragraph_process(question_paragraph)
    paragraph_vec = paragraph_vector(question_contents, model)
    for similar_question in question_vec[str(question_type)]:
        question_result = distCos(similar_question, paragraph_vec)
        print('提取到问题的概率: {}'.format(question_result))
        if question_result > 0.6:
            print('命中问题的概率: {}'.format(question_result))
            return question_result
        break


def answer_similar(question_type, agent_answer, model):
    answer_path = "/home/user/huanglhy/QIA_Serve_Production/heyi_kafka/src/app/libs/knowledge/answer_vec.json"
    with open(answer_path, "r", encoding="utf-8") as answer_file:
        answer_vec = json.load(answer_file)
    answer_contents = paragraph_process(agent_answer)
    answer_paragraph_vec = paragraph_vector(answer_contents, model)
    answer_result = distCos(answer_vec[str(question_type)], answer_paragraph_vec)
    print('坐席回答与标准答案之间的相似度: {}'.format(answer_result))
    if answer_result < 0.9:
        print('命中句子与标准答案之间的相似度: {}'.format(answer_result))
        return answer_result
