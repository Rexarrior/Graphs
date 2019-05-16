import json
import time
import os
import sys
import requests
from serializers import *


def get_user_config(path):
    config = load_json(path)
    return config['user_id'], config['access_token']


def request_friends(user_id, access_token):
    url = 'https://api.vk.com/method/friends.get?user_id=' +\
            f'{user_id}&v=5.52&access_token={access_token}'
    response = requests.get(url).json()
    if ('error' in response):
        if response['error']['error_code'] == 15:
            return []  # empty for private user
        if response['error']['error_code'] == 5:
            print('wrong access token')
            exit()
        if response['error']['error_code'] == 18:
            return [] # empty for deleted user
    friend_ids = response['response']['items']
    return friend_ids


def fill_graph(graph, id2number_dict, access_token):
    counter = 0
    query_start_time = time.time()
    for user_id in id2number_dict:
        if counter == 3:
            time.sleep(1.5 - (time.time() - query_start_time))
            counter = 0
            query_start_time = time.time()
        friend_ids = request_friends(user_id, access_token)
        try:
            for friend_id in friend_ids:
                if friend_id in id2number_dict:
                    graph[id2number_dict[friend_id]].append(
                        id2number_dict[user_id])
        except KeyError as er:
            print(er)
        finally:
            counter += 1
    return graph


def get_graph_as_list(target_user_id, access_token):
    friend_ids = request_friends(target_user_id, access_token)
    id2number_dict = dict()
    number2id_dict = dict()
    graph = list()
    for i in range(len(friend_ids)):
        id2number_dict[friend_ids[i]] = i
        number2id_dict[i] = int(friend_ids[i])
        graph.append([])
    graph = fill_graph(graph, id2number_dict, access_token)
    return graph, number2id_dict


def get_and_save_graph(path_to_config, graph_save_path, id_map_save_path=''):
    user_id, access_token = get_user_config(path_to_config)
    graph, id_map = get_graph_as_list(user_id, access_token)
    save_json(graph_save_path, graph)
    if (id_map_save_path != ''):
        save_json(id_map_save_path, id_map)


if __name__ == "__main__":
    get_and_save_graph('data\\config.json',
                       'data\\graph.json',
                       'data\\id_map.json')
